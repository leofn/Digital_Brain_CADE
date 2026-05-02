#!/usr/bin/env python3
"""
Digital Brain CADE - Clean Normalization v2
=============================================

Conservative normalization that preserves valid entities while removing noise.
"""
import json
import re
from pathlib import Path
from collections import defaultdict, Counter

GRAPH_DIR = Path("~/brain_cade/graph/").expanduser()

def is_noise_entity(name: str, etype: str) -> bool:
    """Return True if this entity is clearly noise/fragment."""
    n = name.strip()
    
    # Too short to be meaningful
    min_len = {"Empresa": 4, "Mercado": 6, "Autor": 3, "Metodologia": 2, "Nota Técnica": 2}
    if len(n) < min_len.get(etype, 3):
        return True
    
    # Clearly a sentence fragment, not an entity
    sentence_fragments = [
        r'^possivelmente',
        r'^espera-se que',
        r'^em (decorrência|um futuro)',
        r'^a (oper|quisi|expans|comer)',
        r'^outras?\s',
        r'^lubrificantes\s',
        r'^preservativos\s',
        r'^comercializad',
        r'^à posição',
        r'^uma expansão',
        r'^em um futuro',
        r'Advs[:]',
        r'Natureza da operação',
        r'Setor econômico',
        r'aquisição de controle sobre',
        r'possibilitará ainda',
        r'possibilitar que',
    ]
    for pat in sentence_fragments:
        if re.search(pat, n, re.IGNORECASE):
            return True
    
    # Very long = likely a sentence, not entity name
    if len(n) > 120:
        return True
    
    # Market names that are full sentences
    if etype == "Mercado" and len(n) > 80:
        return True
    
    # Starts with lowercase letter = not a proper entity (except methodology terms)
    if etype != "Metodologia" and n[0].islower():
        return True
    
    return False


def canonicalize_company(name: str) -> str:
    """Get the canonical company name."""
    n = name.strip().rstrip('.,;')
    # Remove encoding artifacts
    n = n.replace('\u0000', 'ç').replace('\u00ad', '-')
    # Collapse whitespace
    n = re.sub(r'\s+', ' ', n)
    
    # Extract trade name from parentheses like ("xxx")
    # e.g. "Ipiranga Produtos de Petróleo S.A. (\"Ipiranga\")" 
    # Keep the full name but note the short form
    return n


def find_company_groups(entities: dict) -> dict:
    """Group similar company names together."""
    companies = [(n, i) for n, i in entities.items() if i["type"] == "Empresa"]
    
    # Build groups by extracting core trading names
    groups = {}  # canonical -> list of variants
    alias_map = {}  # variant -> canonical
    
    for name, info in companies:
        # Try to extract short name from trade-name pattern
        # "Company Full Name S.A. (\"Short\")" pattern
        trade_match = re.search(r'[\(""\u201c]([^)""\u201c]+)[\)""]\s*$', name)
        short_name = trade_match.group(1).strip('"\' ') if trade_match else None
        
        # The full name without trade name annotation
        base_name = name
        if trade_match:
            base_name = name[:trade_match.start()].strip().rstrip('(\u201c"').strip().rstrip(',').strip()
        
        # Check for known overlaps
        # Normalize: remove S.A., Ltda., etc for matching
        norm = re.sub(r'\s*S\.A\.?\s*\.?$', '', base_name)
        norm = re.sub(r'\s*Ltda\.?\s*$', '', norm)
        norm = re.sub(r'\s*S/A\s*$', '', norm)
        norm = norm.strip()
        
        # Check if this matches an existing group
        found = False
        for canonical, variants in groups.items():
            for v in variants:
                v_norm = re.sub(r'\s*S\.A\.?\s*\.?$', '', v)
                v_norm = re.sub(r'\s*Ltda\.?\s*$', '', v_norm)
                v_norm = re.sub(r'\s*S/A\s*$', '', v_norm).strip()
                if norm.lower() == v_norm.lower() or (short_name and short_name.lower() in v.lower()):
                    variants.append(name)
                    alias_map[name] = canonical
                    found = True
                    break
            if found:
                break
        
        if not found:
            canonical = base_name if base_name else name
            groups[canonical] = [name]
            alias_map[name] = canonical
    
    return groups, alias_map


def main():
    print("=" * 60)
    print("Digital Brain CADE - Clean Normalization v2")
    print("=" * 60)

    # Load RAW data (we need the original unnormalized data)
    # Re-run extraction first to get raw data
    import subprocess
    result = subprocess.run(
        ["/usr/bin/python3", str(Path("~/brain_cade/scripts/extract_triples.py").expanduser())],
        capture_output=True, text=True
    )
    # The extraction script already saves to entities.json and triples.json
    
    # Now load the fresh data
    with open(GRAPH_DIR / "entities.json", encoding="utf-8") as f:
        raw_entities = json.load(f)
    with open(GRAPH_DIR / "triples.json", encoding="utf-8") as f:
        raw_triples = json.load(f)

    print(f"Raw entities: {len(raw_entities)}")
    print(f"Raw triples: {len(raw_triples)}")

    # Step 1: Remove noise entities
    clean_entities = {}
    removed_entities = set()
    for name, info in raw_entities.items():
        if not is_noise_entity(name, info["type"]):
            clean_entities[name] = info
        else:
            removed_entities.add(name)
    
    print(f"\nAfter noise removal: {len(clean_entities)} entities (removed {len(removed_entities)} noisy)")

    # Step 2: Group similar companies
    groups, alias_map = find_company_groups(clean_entities)
    print(f"Company groups: {len(groups)}")
    
    # Show groups with multiple members
    multi_groups = {k: v for k, v in groups.items() if len(v) > 1}
    if multi_groups:
        print(f"\nMerged company groups ({len(multi_groups)}):")
        for canonical, variants in multi_groups.items():
            print(f"  {canonical}")
            for v in variants:
                print(f"    ← {v}")

    # Step 3: Rebuild triples with normalized entity names
    clean_triples = []
    for t in raw_triples:
        subj = alias_map.get(t["subject"], t["subject"])
        obj = alias_map.get(t["object"], t["object"])
        
        # Skip triples referencing removed entities unless they're doc IDs
        if t["subject"] in removed_entities and not t["subject"].startswith("NT_"):
            continue
        if t["object"] in removed_entities and not t["object"].startswith("NT_"):
            continue
            
        clean_triples.append({
            "subject": subj,
            "predicate": t["predicate"],
            "object": obj
        })

    # Remove duplicate triples
    seen = set()
    final_triples = []
    for t in clean_triples:
        key = (t["subject"], t["predicate"], t["object"])
        if key not in seen:
            seen.add(key)
            final_triples.append(t)

    # Rebuild entity registry from final triples
    final_entities = {}
    for name, info in clean_entities.items():
        canonical = alias_map.get(name, name)
        if canonical not in final_entities:
            final_entities[canonical] = {**info, "aliases": []}
        if name != canonical:
            final_entities[canonical]["aliases"].append(name)
    
    # Add entities that appear only in triples (e.g., doc IDs, process numbers)
    for t in final_triples:
        for side in ["subject", "object"]:
            name = t[side]
            if name not in final_entities:
                # Infer type
                if name.startswith("NT_"):
                    final_entities[name] = {"type": "Nota Técnica", "source": ""}
                elif t["predicate"] == "processo":
                    final_entities[name] = {"type": "Processo", "source": ""}
                elif t["predicate"] == "ano":
                    final_entities[name] = {"type": "Ano", "source": ""}

    # Stats
    type_counts = Counter(info["type"] for info in final_entities.values())
    print(f"\n{'=' * 60}")
    print(f"FINAL RESULTS")
    print(f"{'=' * 60}")
    print(f"Entities: {len(final_entities)}")
    print(f"Triples: {len(final_triples)}")
    print(f"\nEntity types:")
    for t, c in type_counts.most_common():
        print(f"  {t}: {c}")

    # Top companies
    companies = [(n, i) for n, i in final_entities.items() if i["type"] == "Empresa"]
    company_connections = Counter()
    for t in final_triples:
        company_connections[t["subject"]] += 1
        company_connections[t["object"]] += 1
    companies.sort(key=lambda x: company_connections.get(x[0], 0), reverse=True)
    print(f"\nTop empresas:")
    for name, info in companies[:15]:
        print(f"  {name} ({company_connections.get(name, 0)} conexões)")
        if info.get("aliases"):
            for a in info["aliases"]:
                print(f"    ← {a}")

    # Top markets
    markets = [(n, i) for n, i in final_entities.items() if i["type"] == "Mercado"]
    market_connections = Counter()
    for t in final_triples:
        if t["subject"] in [m[0] for m in markets] or t["object"] in [m[0] for m in markets]:
            market_connections[t["subject"]] += 1
            market_connections[t["object"]] += 1
    markets.sort(key=lambda x: market_connections.get(x[0], 0), reverse=True)
    print(f"\nTop mercados:")
    for name, info in markets[:15]:
        print(f"  {name} ({market_connections.get(name, 0)} conexões)")

    # Save
    with open(GRAPH_DIR / "entities.json", "w", encoding="utf-8") as f:
        json.dump(final_entities, f, ensure_ascii=False, indent=2)
    with open(GRAPH_DIR / "triples.json", "w", encoding="utf-8") as f:
        json.dump(final_triples, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Clean data saved to {GRAPH_DIR}/")


if __name__ == "__main__":
    main()