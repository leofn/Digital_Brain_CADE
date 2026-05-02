#!/usr/bin/env python3
"""
Digital Brain CADE - Entity Normalization & Graph Cleanup
===========================================================

Phase 2: Clean up noisy entities from structural extraction.
- Remove fragment entities (too short, meaningless)
- Normalize company names (canonical form + aliases)
- Clean market names
- Rebuild graph files with cleaned data
"""
import json
import re
from pathlib import Path
from collections import defaultdict

GRAPH_DIR = Path("~/brain_cade/graph/").expanduser()

def is_valid_entity(name: str, etype: str) -> bool:
    """Filter out noisy/invalid entities."""
    # Minimum meaningful length per type
    min_lengths = {"Empresa": 5, "Mercado": 8, "Autor": 4, "Metodologia": 3, "Nota Técnica": 3}
    if len(name.strip()) < min_lengths.get(etype, 3):
        return False
    
    # Remove fragments that are clearly text fragments, not entities
    noise_patterns = [
        r'^[a-z]',  # Starts with lowercase (not a proper entity)
        r'possivelmente',
        r'espera-se',
        r' em (decorrência|um|decorrência)',
        r'^a (opera|quisi|expans|comer)',
        r'^outras?\.?Natureza',
        r'^lubrificantes',
        r'^preservativos',
        r'^comercializad',
        r'^à posição',
        r'^uma expansão',
        r'^em um futuro',
        r'S\.A\. Operadora$',
        r'Advs:',  # Lawyer info embedded
    ]
    for pattern in noise_patterns:
        if re.search(pattern, name, re.IGNORECASE):
            return False

    # Too many spaces = fragment
    if name.count(' ') > 15:
        return False
    
    # Starts with bullet or special char
    if name.startswith(('•', '-', ',', ';', '.', '(', '"')):
        # But allow parenthesized trade names like "Ipiranga"
        if not re.match(r'^"[^"]+"$', name):
            pass  # reject fragments starting with punctuation
    
    # Very short fragments like "S.A", "Ltda" alone
    if name.strip().rstrip('.') in ['S.A', 'S.A.', 'Ltda', 'S/A', 'Inc', 'Comércio', 'Indústria', 'Mercados']:
        return False
    
    # Fragment patterns that indicate broken extraction
    fragment_indicators = [
        'Operação Proposta',
        'Natureza da operação',
        'Setor econômico',
        'aquisição de controle',
    ]
    for frag in fragment_indicators:
        if frag.lower() in name.lower():
            return False

    return True


def normalize_company(name: str) -> tuple[str, str]:
    """Normalize company name to canonical form. Returns (canonical, alias)."""
    original = name
    
    # Remove trade name annotations like ("xxx") or (\"xxx\")
    # e.g. "Ipiranga Produtos de Petróleo S.A. (\"Ipiranga\")" -> "Ipiranga Produtos de Petróleo S.A."
    trade_name = None
    trade_match = re.search(r'[\(""\u201c\u201d]([^)""\u201c\u201d]+)[\)""]\s*$', name)
    if trade_match:
        trade_name = trade_match.group(1).strip('"\'')
        name = name[:trade_match.start()].strip().rstrip('(\u201c"').strip()
    
    # Remove trailing punctuation
    name = name.rstrip('.,;: ')
    
    # Clean encoding artifacts
    name = name.replace('\u0000', 'ç').replace('\u00ad', '-')
    
    # Remove excessive whitespace
    name = re.sub(r'\s+', ' ', name).strip()
    
    return name, original


def normalize_market(name: str) -> str:
    """Clean market names."""
    name = name.strip().rstrip(',.;')
    name = re.sub(r'\s+', ' ', name)
    # Remove trailing fragments
    name = re.sub(r'\s+foi a introdução.*$', '', name)
    name = re.sub(r'\s+junto às requerentes.*$', '', name)
    name = re.sub(r'\s+c na região.*$', '', name)
    return name[:100]  # Cap length


def main():
    print("=" * 60)
    print("Digital Brain CADE - Entity Normalization")
    print("=" * 60)

    # Load data
    with open(GRAPH_DIR / "entities.json", encoding="utf-8") as f:
        raw_entities = json.load(f)
    with open(GRAPH_DIR / "triples.json", encoding="utf-8") as f:
        raw_triples = json.load(f)
    with open(GRAPH_DIR / "documents.json", encoding="utf-8") as f:
        documents = json.load(f)

    # Phase 1: Filter invalid entities
    valid_entities = {}
    removed = 0
    for name, info in raw_entities.items():
        if is_valid_entity(name, info["type"]):
            valid_entities[name] = info
        else:
            removed += 1
    
    print(f"Filtered entities: {len(raw_entities)} → {len(valid_entities)} (removed {removed} noisy)")

    # Phase 2: Normalize company names and build alias map
    company_aliases = {}  # alias -> canonical
    normalized_entities = {}
    
    # Process companies separately for normalization
    for name, info in list(valid_entities.items()):
        if info["type"] == "Empresa":
            canonical, original = normalize_company(name)
            if canonical != name:
                company_aliases[name] = canonical
            if canonical not in normalized_entities:
                normalized_entities[canonical] = {**info, "aliases": [original]}
            else:
                normalized_entities[canonical].setdefault("aliases", []).append(original)
        else:
            if info["type"] == "Mercado":
                name = normalize_market(name)
            normalized_entities[name] = info

    # Phase 3: Rebuild triples with normalized names
    normalized_triples = []
    for t in raw_triples:
        subj = company_aliases.get(t["subject"], t["subject"])
        obj = company_aliases.get(t["object"], t["object"])
        
        # Skip triples with invalid entities
        if not is_valid_entity(subj, "Empresa") and t["subject"] in raw_entities and raw_entities[t["subject"]]["type"] == "Empresa":
            if not is_valid_entity(t["subject"], raw_entities[t["subject"]]["type"]):
                continue
        if not is_valid_entity(obj, "Empresa") and t["object"] in raw_entities and raw_entities[t["object"]]["type"] == "Empresa":
            if not is_valid_entity(t["object"], raw_entities[t["object"]]["type"]):
                continue
        
        # Skip triples with filtered-out entities
        subj_exists = subj in normalized_entities or subj.startswith("NT_")
        obj_exists = obj in normalized_entities or any(c in obj for c in "0123456789")
        
        new_triple = {
            "subject": subj,
            "predicate": t["predicate"],
            "object": obj
        }
        normalized_triples.append(new_triple)

    # Also clean markets in triples
    final_triples = []
    for t in normalized_triples:
        # Validate both subject and object still exist in entities or are doc IDs
        s_valid = t["subject"] in normalized_entities or t["subject"].startswith("NT_")
        o_valid = t["object"] in normalized_entities or t["object"].startswith("NT_")
        
        if s_valid or o_valid:  # Keep if at least one side is valid
            final_triples.append(t)

    # Stats
    type_counts = defaultdict(int)
    for name, info in normalized_entities.items():
        type_counts[info["type"]] += 1

    print(f"\nNormalized entities: {len(normalized_entities)}")
    print(f"Normalized triples: {len(final_triples)}")
    print(f"Company aliases: {len(company_aliases)}")
    print(f"\nEntity types after normalization:")
    for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")

    # Save normalized data
    with open(GRAPH_DIR / "entities_normalized.json", "w", encoding="utf-8") as f:
        json.dump(normalized_entities, f, ensure_ascii=False, indent=2)
    with open(GRAPH_DIR / "triples_normalized.json", "w", encoding="utf-8") as f:
        json.dump(final_triples, f, ensure_ascii=False, indent=2)

    # Also update the main files
    with open(GRAPH_DIR / "entities.json", "w", encoding="utf-8") as f:
        json.dump(normalized_entities, f, ensure_ascii=False, indent=2)
    with open(GRAPH_DIR / "triples.json", "w", encoding="utf-8") as f:
        json.dump(final_triples, f, ensure_ascii=False, indent=2)

    # Show top companies
    companies = [(n, i) for n, i in normalized_entities.items() if i["type"] == "Empresa"]
    companies.sort(key=lambda x: len(adj_count(x[0], final_triples)), reverse=True)
    print(f"\nTop empresas por conexões:")
    for name, info in companies[:10]:
        conn_count = len(adj_count(name, final_triples))
        print(f"  {name} ({conn_count} conexões)")

    print(f"\n✅ Dados normalizados salvos em {GRAPH_DIR}/")


def adj_count(entity, triples):
    """Count connections for an entity."""
    return [t for t in triples if t["subject"] == entity or t["object"] == entity]


if __name__ == "__main__":
    main()