#!/usr/bin/env python3
"""
Digital Brain CADE - Normalization v3
======================================

Conservative cleanup: remove clear noise, normalize company names 
using a curated alias system, and rebuild the graph.

Key principle: better to keep slightly messy entities than lose real data.
"""
import json
import re
from pathlib import Path
from collections import Counter, defaultdict

GRAPH_DIR = Path("~/brain_cade/graph/").expanduser()


def is_noise(name: str, etype: str) -> bool:
    """Only remove clearly broken fragments."""
    n = name.strip()
    
    # Too short = fragment
    if len(n) < 4: return True
    if etype == "Empresa" and len(n) < 5: return True
    if etype == "Mercado" and len(n) < 8: return True
    
    # Clearly a sentence, not an entity
    noise_phrases = [
        "possivelmente", "espera-se", "em decorrência", "a operação proposta",
        "outras.", "lubrificantes", "preservativos", "comercializadas",
        "à posição", "uma expansão", "em um futuro", "Natureza da operação",
        "Setor econômico", "aquisição de controle sobre", "possibilitará ainda",
        "possibilitar que", "Advs:", "aquisição de controle sobre a linha",
    ]
    for phrase in noise_phrases:
        if phrase.lower() in n.lower(): return True
    
    # Too long = sentence, not entity name (except Nota Técnica)
    max_len = {"Empresa": 100, "Mercado": 100, "Autor": 60, "Metodologia": 50}
    if len(n) > max_len.get(etype, 120): return True
    
    # Starts with lowercase (not a proper noun, except methodology)
    if etype not in ("Metodologia",) and n[0].islower(): return True
    
    # Bullet points
    if n.startswith(("•", "·", "- ")): return True
    
    # Trailing fragment indicators
    if re.search(r'(foi a introdução|junto às requerentes|c na região)', n): return True
    
    return False


def normalize_company(name: str) -> str:
    """Clean up company name."""
    n = name.strip()
    # Remove leading bullets/whitespace
    n = re.sub(r'^[\s•·\-]+\s*', '', n)
    # Remove embedded lawyer info
    n = re.sub(r'\s*Advs?:\s*.*$', '', n)
    # Encode fix
    n = n.replace('\u0000', 'ç').replace('\u00ad', '-')
    # Collapse whitespace
    n = re.sub(r'\s+', ' ', n).strip()
    # Remove trailing punctuation
    n = n.rstrip('.,;:')
    return n


def normalize_market(name: str) -> str:
    """Clean up market name."""
    n = name.strip().rstrip('.,;')
    n = re.sub(r'\s+', ' ', n)
    # Remove fragment tails
    for stop in ['foi a introdução', 'junto às requerentes', 'c na região', 'na região nordeste']:
        if stop in n:
            n = n[:n.index(stop)].strip()
    return n[:100].strip()


# Known company normalization map (manually curated from CADE data)
COMPANY_ALIASES = {
    # Ipiranga
    "Ipiranga Produtos de Petróleo S.A. (\"Ipiranga\")": "Ipiranga",
    "Ipiranga Produtos de Petróleo S.A.": "Ipiranga",
    # Kroton
    "•  Kroton Educacional S.A. (\"Kroton\")": "Kroton Educacional",
    "Kroton Educacional S.A. (\"Kroton\")": "Kroton Educacional",
    "Kroton Educacional S.A.": "Kroton Educacional",
    # Prosegur
    "Prosegur  Brasil  S.A.  Transportadora  de  Valores  e": "Prosegur Brasil",
    "Prosegur  Brasil  Transportadora  de  Valores": "Prosegur Brasil",
    "Prosegur Brasil S.A. Transportadora de Valores": "Prosegur Brasil",
    "(\"Prosegur\")": "Prosegur Brasil",
    # Transvip
    "(\"Transvip\")": "Transvip",
    "Transvip  -  Transporte  de  Valores": "Transvip",
    # CETIP/B3
    "(\"CETIP\")": "CETIP",
    "CETIP S.A. – Mercados Organizados": "CETIP",
    "BM&FBOVESPA S.A. – Bolsa de Valores": "B3 (BM&FBOVESPA)",
    "Futuros (\"BVMF\")": "B3 (BM&FBOVESPA)",
    # Lactalis
    "Lactalis do Brasil – Comércio": "Lactalis do Brasil",
    "Dairy Partners Americanas Brasil Ltda": "Dairy Partners Americas",
    "Dairy Partners Americanas Nordeste – Produtos Alimentícios Ltda": "Dairy Partners Americas Nordeste",
    # Localiza/Unidas
    "Companhia de Locação das Américas (Unidas)": "Unidas",
    "Localiza Rent a Car S.A": "Localiza",
    # USIMINAS/CSN
    "(USIMINAS)": "Usiminas",
    "Usinas  Siderúrgicas  de  Minas  Gerais  S/A": "Usiminas",
    "Companhia  Siderúrgica  Nacional  (CSN)": "CSN (Companhia Siderúrgica Nacional)",
    # Bunge
    "Bunge Alimentos S.A": "Bunge Alimentos",
    # Hypermarcas/Reckitt
    "Reckitt Benckiser": "Reckitt Benckiser",
    "Hypermarcas S.A. Advs: Paola Pugliese": "Hypermarcas",
    # House/transport
    "Casa Bahia Comercial Ltda": "Casa Bahia",
    "Casa de": "Casa & Vídeo",  # likely truncated
    # Iberia/TAM/Latam
    "Iberia Líneas Aéreas de Espana": "Iberia",
    "Sociedad UnipersonaI (Iberia)": "Iberia",
    "TAM Linhas Aéreas S.A. (TAM)": "LATAM (TAM)",
    # Owens-Illinois
    "Owens-Illinois do Brasil": "Owens-Illinois do Brasil",
    "Nadir Figueiredo Indústria": "Nadir Figueiredo",
    # Security companies
    "Vigilância  Patrimonial  Ltda": "Vigilância Patrimonial",
    "Segurança": "Segurança (genérico)",  # disambiguate
    "Segurança  S.A": "Segurança (genérico)",
    # Transport
    "União  Transporte  Interestadual  de  Luxo  S.A.  (UTIL)": "UTIL (União Transporte)",
    "Expresso": "Expresso (genérico)",
    # Continental
    "Continental Aktiengesellschaft (\"Continental\")": "Continental",
    # Veyance
    "Inc. (\"Veyance\")": "Veyance Technologies",
    "Veyance": "Veyance Technologies",
    "Technologies": "Veyance Technologies",
}


def main():
    print("=" * 60)
    print("Digital Brain CADE - Normalization v3")
    print("=" * 60)

    # Load data
    with open(GRAPH_DIR / "entities.json", encoding="utf-8") as f:
        entities = json.load(f)
    with open(GRAPH_DIR / "triples.json", encoding="utf-8") as f:
        triples = json.load(f)

    print(f"Input: {len(entities)} entities, {len(triples)} triples")

    # Step 1: Remove noise
    clean_entities = {}
    removed = 0
    for name, info in entities.items():
        if not is_noise(name, info["type"]):
            clean_entities[name] = info
        else:
            removed += 1
    print(f"Noise removed: {removed} entities")

    # Step 2: Normalize entities using alias map + rules
    normalized_entities = {}
    entity_map = {}  # old_name -> new_name
    
    for name, info in clean_entities.items():
        new_name = name
        etype = info["type"]
        
        # Apply curated aliases first
        if name in COMPANY_ALIASES:
            new_name = COMPANY_ALIASES[name]
        elif etype == "Empresa":
            new_name = normalize_company(name)
        elif etype == "Mercado":
            new_name = normalize_market(name)
        
        if new_name != name:
            entity_map[name] = new_name
        
        if new_name in normalized_entities:
            # Merge aliases
            existing = normalized_entities[new_name]
            if "aliases" not in existing:
                existing["aliases"] = []
            if name not in existing.get("aliases", []) and name != new_name:
                existing["aliases"].append(name)
            # Keep richer source info
            if len(info.get("source", "")) > len(existing.get("source", "")):
                existing["source"] = info["source"]
        else:
            normalized_entities[new_name] = {**info}
            if name != new_name:
                normalized_entities[new_name]["aliases"] = [name]

    # Step 3: Remap triples
    final_triples = []
    seen_triples = set()
    for t in triples:
        subj = entity_map.get(t["subject"], t["subject"])
        obj = entity_map.get(t["object"], t["object"])
        
        # Skip triples referencing removed noise entities
        if t["subject"] not in entities and t["subject"] not in clean_entities and not t["subject"].startswith("NT_"):
            continue
        if t["object"] not in entities and t["object"] not in clean_entities and not t["object"].startswith("NT_"):
            continue
            
        key = (subj, t["predicate"], obj)
        if key not in seen_triples:
            seen_triples.add(key)
            final_triples.append({"subject": subj, "predicate": t["predicate"], "object": obj})

    # Ensure doc IDs and other structural entities exist
    for t in final_triples:
        for side in ["subject", "object"]:
            name = t[side]
            if name not in normalized_entities:
                if name.startswith("NT_"):
                    normalized_entities[name] = {"type": "Nota Técnica", "source": ""}
                elif t["predicate"] == "processo":
                    normalized_entities[name] = {"type": "Processo", "source": ""}
                elif t["predicate"] == "ano":
                    normalized_entities[name] = {"type": "Ano", "source": ""}

    # Stats
    type_counts = Counter(info["type"] for info in normalized_entities.values())
    
    print(f"\n{'=' * 60}")
    print(f"RESULTS")
    print(f"{'=' * 60}")
    print(f"Clean entities: {len(normalized_entities)}")
    print(f"Clean triples: {len(final_triples)}")
    print(f"\nEntity types:")
    for t, c in type_counts.most_common():
        print(f"  {t}: {c}")

    # Top entities by connections
    conn = Counter()
    for t in final_triples:
        conn[t["subject"]] += 1
        conn[t["object"]] += 1

    for etype in ["Empresa", "Mercado", "Nota Técnica", "Metodologia"]:
        top = [(n, conn.get(n, 0)) for n, i in normalized_entities.items() if i["type"] == etype]
        top.sort(key=lambda x: -x[1])
        if top:
            print(f"\nTop {etype}s:")
            for name, c in top[:8]:
                aliases = normalized_entities[name].get("aliases", [])
                alias_str = f" ← {', '.join(aliases[:2])}" if aliases else ""
                print(f"  {name} ({c} conexões){alias_str}")

    # Save
    with open(GRAPH_DIR / "entities.json", "w", encoding="utf-8") as f:
        json.dump(normalized_entities, f, ensure_ascii=False, indent=2)
    with open(GRAPH_DIR / "triples.json", "w", encoding="utf-8") as f:
        json.dump(final_triples, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Saved to {GRAPH_DIR}/")


if __name__ == "__main__":
    main()