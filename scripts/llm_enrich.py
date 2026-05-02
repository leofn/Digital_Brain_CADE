#!/usr/bin/env python3
"""
Digital Brain CADE - LLM-Enriched Market & Relation Extraction
================================================================

Extracts market names, M&A relations, and competitive concerns
from CADE Notas Técnicas using improved Portuguese regex patterns.
"""
import json
import re
from pathlib import Path
from collections import Counter, defaultdict

MD_DIR = Path("~/brain_cade/md/").expanduser()
GRAPH_DIR = Path("~/brain_cade/graph/").expanduser()
GRAPH_DIR.mkdir(parents=True, exist_ok=True)

def extract_md_metadata(text: str, filename: str) -> dict:
    """Extract nota number and year from filename."""
    m = re.search(r'n__(\d+)_?(\d{4})?', filename)
    nota_num = m.group(1) if m else "?"
    nota_year = m.group(2) if m and m.group(2) else ""
    doc_id = f"NT_{nota_num}_{nota_year}" if nota_year else f"NT_{nota_num}"
    return {"doc_id": doc_id, "nota_num": nota_num, "nota_year": nota_year}

def extract_markets(text: str, doc_id: str) -> list:
    """Extract relevant market names from text with improved patterns."""
    markets = []
    seen = set()
    
    # Pattern 1: "mercado relevante de X" / "mercado de X"
    patterns = [
        # Explicit "mercado relevante" mentions
        r'mercado\s+relevante\s+(?:de|da|dos|das|para|em)\s+([A-ZÀ-ÿa-zà-ÿ\s\-&,]+?)(?:\s*[,\.\(;]|\s+(?:e|na|no|para|com|que|com\s+base|conforme|segundo|conforme|tendo|tendo\s+como)|$)',
        # "mercado de X"  
        r'mercado\s+(?:de|da|dos|das|para|em)\s+([A-ZÀ-ÿa-zà-ÿ\s\-&,]+?)(?:\s*[,\.\(;]|\s+(?:e\s+o|na|no|para|com|que\s|conforme|segundo|tendo)|$)',
        # "setor de X"
        r'setor\s+(?:de|da|dos|das|em)\s+([A-ZÀ-ÿa-zà-ÿ\s\-&,]+?)(?:\s*[,\.\(;]|\s+(?:e|na|no|para|com|que\s|conforme)|$)',
        # "segmento de X"
        r'segmento\s+(?:de|da|dos|das|em)\s+([A-ZÀ-ÿa-zà-ÿ\s\-&,]+?)(?:\s*[,\.\(;]|\s+(?:e|na|no|para|com|que\s|conforme)|$)',
        # "indústria de X"
        r'ind[úu]stria\s+(?:de|da|dos|das|em)\s+([A-ZÀ-ÿa-zà-ÿ\s\-&,]+?)(?:\s*[,\.\(;]|\s+(?:e|na|no|para|com|que\s|conforme)|$)',
        # Specific CNAE patterns: "CNAE X - Y"
        r'CNAE\s+([\d\.]+\s*[-–]\s*[A-ZÀ-ÿ][A-Za-zà-ÿ\s\-&]+?)(?:\s*[,\.\(;]|\s+(?:e|na|no)|$)',
    ]
    
    for pat in patterns:
        for match in re.finditer(pat, text, re.IGNORECASE):
            market = match.group(1).strip()
            # Cleanup
            market = re.sub(r'\s+', ' ', market).strip()
            market = market.rstrip('.,;:)]')
            # Remove trailing conjunctions/articles
            market = re.sub(r'\s+(e|na|no|para|com|que|de\s+qualquer|conforme|segundo|tendo|com\s+base|segundo|esta|este|esta\s+nota|este\s+documento).*$', '', market, flags=re.IGNORECASE)
            market = market.strip()
            
            # Validate
            if len(market) < 5 or len(market) > 80:
                continue
            if market[0].islower() and market[0].isalpha():
                continue
            # Skip generic terms
            generic = {"mercado", "setor", "segmento", "indústria", "questão", "estudo", "requerentes",
                       "análise", "operação", "empresa", "grupo", "requerente"}
            if market.lower().strip() in generic:
                continue
                
            if market.lower() not in seen:
                seen.add(market.lower())
                markets.append(market)
    
    return markets

def extract_merger_relations(text: str, doc_id: str) -> list:
    """Extract M&A and competitive relations."""
    relations = []
    
    # Pattern: Company A adquire/incorpora/funde Company B
    merger_patterns = [
        (r'([A-Z][A-Za-zà-ÿ\s&\-\.]+?(?:S\.A|Ltda|S/A|Inc))\s+(?:pretende\s+)?(?:adquirir|comprar|incorporar|absorver)\s+(?:o\s+controle\s+da?\s+)?(?:o?\s+)?([A-Z][A-Za-zà-ÿ\s&\-\.]+?(?:S\.A|Ltda|S/A|Inc))', "adquire"),
        (r'fus[\u00e3oã]o\s+(?:entre|de)\s+([A-Z][A-Za-zà-ÿ\s&\-\.]+?(?:S\.A|Ltda|S/A|Inc))\s+(?:e|com)\s+([A-Z][A-Za-zà-ÿ\s&\-\.]+?(?:S\.A|Ltda|S/A|Inc))', "fusiona_com"),
        (r'incorpora[\u00e7c][\u00e3oã]o\s+(?:de|da)\s+([A-Z][A-Za-zà-ÿ\s&\-\.]+?(?:S\.A|Ltda|S/A|Inc))\s+(?:por|pela)\s+([A-Z][A-Za-zà-ÿ\s&\-\.]+?(?:S\.A|Ltda|S/A|Inc))', "incorporada_por"),
    ]
    
    for pat, pred in merger_patterns:
        for match in re.finditer(pat, text[:5000]):
            a = match.group(1).strip().rstrip('.,;')
            b = match.group(2).strip().rstrip('.,;')
            if len(a) > 4 and len(b) > 4:
                relations.append({"subject": a, "predicate": pred, "object": b})
    
    return relations

def extract_competitive_concerns(text: str, doc_id: str) -> list:
    """Extract competitive concerns from the document."""
    concerns = []
    concern_types = {
        "prejuízo à concorrência": r'preju[íi]zo\s+[àa]\s+concorr[eê]ncia',
        "efeitos unilaterais": r'efeitos?\s+unilaterais?',
        "efeitos coordenados": r'efeitos?\s+coordenados?',
        "barreiras à entrada": r'barreiras?\s+[àa]\s+entrada',
        "poder de mercado": r'poder\s+de\s+mercado',
        "participação relevante": r'participa[\u00e7c][\u00e3oã]o\s+relevante',
        "preço predatório": r'pre[\u00e7c]o\s+predat[\u00f3o]rio',
        "fechamento de mercado": r'fechamento\s+de\s+mercado',
        "discriminação de preços": r'discrimina[\u00e7c][\u00e3oã]o\s+de\s+pre[\u00e7c]os',
        "concentração horizontal": r'concentra[\u00e7c][\u00e3oã]o\s+horizontal',
        "concentração vertical": r'concentra[\u00e7c][\u00e3oã]o\s+vertical',
        "conglomerado": r'conglomerado',
    }
    
    for concern_name, pattern in concern_types.items():
        if re.search(pattern, text, re.IGNORECASE):
            concerns.append(concern_name)
    
    return concerns

def main():
    print("=" * 60)
    print("Digital Brain CADE - Market & Relation Enrichment")
    print("=" * 60)
    
    md_files = sorted(MD_DIR.glob("*.md"))
    content_files = [(f, f.read_text(encoding="utf-8")) for f in md_files if f.stat().st_size > 100]
    print(f"Processing {len(content_files)} MD files...\n")
    
    # Load existing graph data
    with open(GRAPH_DIR / "entities.json", encoding="utf-8") as f:
        existing_entities = json.load(f)
    with open(GRAPH_DIR / "triples.json", encoding="utf-8") as f:
        existing_triples = json.load(f)
    
    new_entities = dict(existing_entities)
    new_triples = list(existing_triples)
    
    all_markets = Counter()
    all_concerns = Counter()
    all_mergers = []
    docs_with_markets = 0
    
    for f, text in content_files:
        meta = extract_md_metadata(text, f.name)
        doc_id = meta["doc_id"]
        
        # 1. Extract markets
        markets = extract_markets(text, doc_id)
        if markets:
            docs_with_markets += 1
        for market in markets:
            all_markets[market] += 1
            if market not in new_entities:
                new_entities[market] = {"type": "Mercado", "source": f.name}
            new_triples.append({"subject": doc_id, "predicate": "mercado_relevante", "object": market})
        
        # 2. Extract merger relations
        relations = extract_merger_relations(text, doc_id)
        for rel in relations:
            all_mergers.append(rel)
            if rel["subject"] not in new_entities:
                new_entities[rel["subject"]] = {"type": "Empresa", "source": f.name}
            if rel["object"] not in new_entities:
                new_entities[rel["object"]] = {"type": "Empresa", "source": f.name}
            new_triples.append(rel)
        
        # 3. Extract competitive concerns
        concerns = extract_competitive_concerns(text, doc_id)
        for concern in concerns:
            all_concerns[concern] += 1
            if concern not in new_entities:
                new_entities[concern] = {"type": "Preocupação Concordrencial", "source": f.name}
            new_triples.append({"subject": doc_id, "predicate": "preocupacao", "object": concern})
    
    print(f"Markets found: {sum(all_markets.values())} mentions in {docs_with_markets}/{len(content_files)} docs")
    print(f"Unique markets: {len(all_markets)}")
    print(f"Merger relations: {len(all_mergers)}")
    print(f"Competitive concerns: {dict(all_concerns)}")
    
    print(f"\nTop 20 Markets:")
    for market, count in all_markets.most_common(20):
        print(f"  {market} ({count} docs)")
    
    print(f"\nTop Concerns:")
    for concern, count in all_concerns.most_common():
        print(f"  {concern}: {count} docs")
    
    # Deduplicate triples
    seen = set()
    final_triples = []
    for t in new_triples:
        key = (t["subject"], t["predicate"], t["object"])
        if key not in seen:
            seen.add(key)
            final_triples.append(t)
    
    print(f"\nTotal entities: {len(new_entities)} (was {len(existing_entities)})")
    print(f"Total triples: {len(final_triples)} (was {len(existing_triples)})")
    
    # Type breakdown
    type_counts = Counter(info["type"] for info in new_entities.values())
    for t, c in type_counts.most_common():
        print(f"  {t}: {c}")
    
    # Save enriched data
    with open(GRAPH_DIR / "entities.json", "w", encoding="utf-8") as f:
        json.dump(new_entities, f, ensure_ascii=False, indent=2)
    with open(GRAPH_DIR / "triples.json", "w", encoding="utf-8") as f:
        json.dump(final_triples, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Enriched data saved to {GRAPH_DIR}/")

if __name__ == "__main__":
    main()