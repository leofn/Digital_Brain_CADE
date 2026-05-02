#!/usr/bin/env python3
"""
Digital Brain CADE - Final Market Cleanup
Removes invalid market names (too short, generic words, sentence fragments).
"""
import json
from pathlib import Path

GRAPH_DIR = Path("~/brain_cade/graph/").expanduser()

# Known bad market names
NOISE_MARKETS = {
    "questão", "estudo", "requerentes", "Bebidas Ltda", "barras", "Reman",
    "origem e destino na metodologia de aritmética vertical",
    "Carbeto de Silício Metalúrgico multiplicada ao valor do Diversion Ratio calculado",
    "EAD por meio do exame dos",
    "Distribuição de Gasolina C na Região Nordeste",
}

def is_valid_market(name: str) -> bool:
    """Check if market name is a real market, not noise."""
    n = name.strip()
    if n.lower() in NOISE_MARKETS:
        return False
    # Must have at least one substantive word
    generic_words = {"de", "da", "dos", "das", "em", "para", "no", "na", "e", "ou", "a", "o", 
                     "foi", "que", "como", "se", "por", "com", "não", "uma", "um", "do", "da"}
    words = [w for w in n.split() if w.lower() not in generic_words]
    if len(words) < 2:
        return False
    # Starts with lowercase = probably noise
    if n[0].islower():
        return False
    # Check for sentence fragments  
    fragment_words = ["foi", "que", "como", "havia", "podia", "sendo", "estava", "havia",
                      "pode", "deveria", "seria", "haver", "pouca", "grande"]
    if any(w.lower() in fragment_words for w in words[:2]):
        return False
    return True

def main():
    with open(GRAPH_DIR / "entities.json", encoding="utf-8") as f:
        entities = json.load(f)
    with open(GRAPH_DIR / "triples.json", encoding="utf-8") as f:
        triples = json.load(f)

    # Find and remove invalid markets
    removed_markets = set()
    for name, info in list(entities.items()):
        if info["type"] == "Mercado" and not is_valid_market(name):
            removed_markets.add(name)
            del entities[name]
    
    # Clean up triples referencing removed markets
    clean_triples = []
    for t in triples:
        if t["subject"] in removed_markets or t["object"] in removed_markets:
            continue
        clean_triples.append(t)

    print(f"Removed {len(removed_markets)} noise markets:")
    for m in sorted(removed_markets):
        print(f"  ✗ {m}")

    # Show remaining markets
    markets = [(n, i) for n, i in entities.items() if i["type"] == "Mercado"]
    print(f"\nRemaining {len(markets)} markets:")
    for name, info in sorted(markets):
        conn = sum(1 for t in clean_triples if t["subject"] == name or t["object"] == name)
        print(f"  ✓ {name} ({conn} conexões)")

    with open(GRAPH_DIR / "entities.json", "w", encoding="utf-8") as f:
        json.dump(entities, f, ensure_ascii=False, indent=2)
    with open(GRAPH_DIR / "triples.json", "w", encoding="utf-8") as f:
        json.dump(clean_triples, f, ensure_ascii=False, indent=2)
    
    print(f"\nFinal: {len(entities)} entities, {len(clean_triples)} triples")

if __name__ == "__main__":
    main()