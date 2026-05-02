#!/usr/bin/env python3
"""
Digital Brain CADE - Extraction Pipeline v2
==============================================

Improved extraction with better market detection and entity recognition.
Uses regex patterns specific to CADE's Notas Técnicas format.
"""
import os
import re
import json
from pathlib import Path
from collections import defaultdict

MD_DIR = Path("~/brain_cade/md/").expanduser()
GRAPH_DIR = Path("~/brain_cade/graph/").expanduser()
GRAPH_DIR.mkdir(parents=True, exist_ok=True)

def extract_metadata(text: str, filename: str) -> dict:
    """Extract structured metadata from a CADE Nota Técnica."""
    # Decode filename to get nota number
    # Nota_T_cnica_n__XX_YYYY___Ato_de_Concentra__o_n__NNNN...
    m = re.search(r'n__(\d+)_?(\d{4})?', filename)
    nota_num = m.group(1) if m else "?"
    nota_year = m.group(2) if m and m.group(2) else ""
    
    entities = {}  # name -> {"type": ..., "source": ...}
    triples = []    # {"subject": ..., "predicate": ..., "object": ...}
    doc_id = f"NT_{nota_num}_{nota_year}" if nota_year else f"NT_{nota_num}"
    
    # Document-level triples
    entities[doc_id] = {"type": "Nota Técnica", "source": filename}
    
    # 1. Extract Process Number
    proc_patterns = [
        r'(\d{5}\.\d{6}/\d{4}-\d{2})',
        r'(\d{5}\.\d{5,6}/\d{4}[-\.]\d{2})',
    ]
    for pat in proc_patterns:
        for match in re.finditer(pat, text):
            proc = match.group(1)
            if proc not in entities:
                entities[proc] = {"type": "Processo", "source": filename}
                triples.append({"subject": doc_id, "predicate": "processo", "object": proc})

    # 2. Extract Year
    year_match = re.search(r'ANO\s*(?:DE\s*)?(\d{4})', text, re.IGNORECASE)
    if year_match:
        year = year_match.group(1)
        entities[year] = {"type": "Ano", "source": filename}
        triples.append({"subject": doc_id, "predicate": "ano", "object": year})
    elif nota_year:
        entities[nota_year] = {"type": "Ano", "source": filename}
        triples.append({"subject": doc_id, "predicate": "ano", "object": nota_year})

    # 3. Extract Requerentes/Companies - IMPROVED
    # Common patterns in CADE documents
    company_patterns = [
        # "X S.A. ("nickname")" with various quote styles
        r'([A-Z][A-Za-zàâãéêíóôõúç\s&\-\.]+(?:S\.A\.?|Ltda\.?|S/A|Inc\.?|SÀRS|Aktiengesellschaft))[\s]*[\(""\u201c\u201d]([^)""]+)\)?',
        # Companies with trade names in parentheses
        r'[\(«"][\s]*([A-Z][A-Za-zàâãéêíóôõúç\s&\-\.]{3,50})[\s]*[\)»"]',
        # "X S.A." without trade name
        r'([A-Z][A-Za-zàâãéêíóôõúç\s&\-]{2,50}(?:S\.A\.?|Ltda\.?|S/A))',
    ]
    
    seen_companies = set()
    for pat in company_patterns:
        for match in re.finditer(pat, text[:3000]):  # Focus on first 3000 chars (header)
            groups = match.groups()
            if len(groups) == 2:
                full_name = groups[0].strip().rstrip('.,;')
                trade_name = groups[1].strip().strip('"\'()')
                if len(full_name) > 4 and full_name not in seen_companies:
                    seen_companies.add(full_name)
                    entities[full_name] = {"type": "Empresa", "source": filename}
                    triples.append({"subject": doc_id, "predicate": "analisa", "object": full_name})
                    if trade_name and len(trade_name) > 1:
                        # Don't add trade name as separate entity, just note it
                        pass
            elif len(groups) == 1:
                name = groups[0].strip().rstrip('.,;')
                if len(name) > 4 and name not in seen_companies:
                    seen_companies.add(name)
                    entities[name] = {"type": "Empresa", "source": filename}
                    triples.append({"subject": doc_id, "predicate": "analisa", "object": name})
    
    # 4. Extract Markets - IMPROVED with broader patterns
    market_patterns = [
        # "mercado de X" / "mercado de X e Y"
        r'mercado\s+(?:de|da|dos|das|em|para)\s+([A-ZÀ-ÿa-zà-ÿ\s\-]+?)(?:\s*[\(\.],|\.|\n|;\s|e\s+o\s+mercado)',
        # "setor de X"
        r'setor\s+(?:de|da|dos|das|em)\s+([A-ZÀ-ÿa-zà-ÿ\s\-]+?)(?:\s*[\(\.],|\.|\n|;\s)',
        # "indústria de X"
        r'ind[úu]stria\s+(?:de|da|dos|das)\s+([A-ZÀ-ÿa-zà-ÿ\s\-]+?)(?:\s*[\(\.],|\.|\n|;\s)',
        # "segmento de X"
        r'segmento\s+(?:de|da|dos|das)\s+([A-ZÀ-ÿa-zà-ÿ\s\-]+?)(?:\s*[\(\.],|\.|\n|;\s)',
    ]
    
    seen_markets = set()
    for pat in market_patterns:
        for match in re.finditer(pat, text, re.IGNORECASE):
            market = match.group(1).strip().rstrip('.,;:')
            # Clean up market name
            market = re.sub(r'\s+', ' ', market)
            # Validate: at least 4 chars, starts with letter
            if len(market) >= 4 and market[0].isalpha() and market.lower() not in seen_markets:
                seen_markets.add(market.lower())
                entities[market] = {"type": "Mercado", "source": filename}
                triples.append({"subject": doc_id, "predicate": "mercado_relevante", "object": market})

    # 5. Extract Authors
    author_patterns = [
        r'(?:Autor[a]?|Relator[a]?|Diretor[a]?|Superintendente)[\s:]+([A-Z][A-Za-zàâãéêíóôõúç\s]+)',
        r'(?:DEE|DEAG|DFA|DCO)[\s/]+(?:de\s+)?([A-Z][A-Za-zàâãéêíóôõúç\s]+)',
    ]
    for pat in author_patterns:
        for match in re.finditer(pat, text, re.IGNORECASE):
            name = match.group(1).strip().rstrip('.,;:')
            if 4 < len(name) < 60 and name not in entities:
                entities[name] = {"type": "Autor", "source": filename}
                triples.append({"subject": name, "predicate": "autor_de", "object": doc_id})

    # 6. Extract Methodologies/Tests
    methods = {
        'GUPPI': r'GUPPI',
        'HHI': r'HHI|[\u00edÍ]ndice Herfindahl',
        'CPPI': r'CPPI',
        'SSNIP': r'SSNIP',
        'Regressão': r'[Rr]egress[\u00e3oã]o',
        'Elasticidade': r'[Ee]lasticidade',
        'Efeitos Unilaterais': r'[Ee]feitos?\s+[Uu]nilaterais?',
        'Efeitos Coordenados': r'[Ee]feitos?\s+[Cc]oordenados?',
        'Eficiências': r'[Ee]fici[\u00eaê]ncias?',
        'Concentração': r'[Cc]oncentra[\u00e7c][\u00e3o\u00f5es][\u00e3o]?es?',
        'Poder de Mercado': r'[Pp]oder\s+de\s+[Mm]ercado',
        'Barreiras à Entrada': r'[Bb]arreiras?\s+[\u00e0a]\s+[Ee]ntrada',
        'Preço': r'[Pp]re[\u00e7c]o',
        'Falha de Mercado': r'[Ff]alha\s+de\s+[Mm]ercado',
        'Cadeia Produtiva': r'[Cc]adeia\s+[Pp]rodutiva',
        'Upstream': r'[Uu]pstream',
        'Downstream': r'[Dd]ownstream',
    }
    for method_name, pattern in methods.items():
        if re.search(pattern, text):
            entities[method_name] = {"type": "Metodologia", "source": filename}
            triples.append({"subject": doc_id, "predicate": "aplica_metodologia", "object": method_name})

    # 7. Extract Operation Type
    op_types = {
        'Fusão': r'[Ff]us[\u00e3oã]o',
        'Aquisição': r'[Aa]quisi[\u00e7c][\u00e3oã]o',
        'Incorporação': r'[Ii]ncorpora[\u00e7c][\u00e3oã]o',
        'Joint Venture': r'[Jj]oint[\s\-]?[Vv]enture',
        'Cisão': r'[Cc]is[\u00e3oã]o',
        'Associação': r'[Aa]ssocia[\u00e7c][\u00e3oã]o',
    }
    for op_name, pattern in op_types.items():
        # Only in the first 1000 chars (header area)
        if re.search(pattern, text[:1000]):
            entities[op_name] = {"type": "Tipo de Operação", "source": filename}
            triples.append({"subject": doc_id, "predicate": "tipo_operacao", "object": op_name})

    # 8. Relationship: companies merged/acquired
    # Pattern: "X pretende adquirir", "aquisição de X por Y", "fusão entre X e Y"
    acquire_patterns = [
        (r'([A-Z][A-Za-z\s\.]+?S\.A\.?)\s+(?:pretende\s+)?(?:adquirir|comprar|incorporar)\s+([A-Z][A-Za-z\s\.]+?S\.A\.?)', "adquire"),
        (r'aquisi[\u00e7c][\u00e3oã]o\s+de\s+([A-Z][A-Za-z\s\.]+?S\.A\.?)\s+por\s+([A-Z][A-Za-z\s\.]+?S\.A\.?)', "adquirida_por"),
    ]
    for pat, pred in acquire_patterns:
        for match in re.finditer(pat, text[:2000]):
            buyer = match.group(1).strip()
            target = match.group(2) if pred == "adquire" else match.group(1).strip()
            acquirer = match.group(1).strip() if pred == "adquire" else match.group(2).strip()
            if len(buyer) > 4 and len(target) > 4:
                entities[buyer] = {"type": "Empresa", "source": filename}
                entities[target] = {"type": "Empresa", "source": filename}
                triples.append({"subject": acquirer, "predicate": "adquire", "object": target})

    return {"entities": entities, "triples": triples, "doc_id": doc_id}


def main():
    print("=" * 60)
    print("Digital Brain CADE - Structural Extraction v2")
    print("=" * 60)
    
    md_files = sorted(MD_DIR.glob("*.md"))
    content_files = [(f, f.read_text(encoding="utf-8")) for f in md_files if f.stat().st_size > 100]
    
    print(f"Found {len(content_files)} MD files with content")
    
    all_entities = {}
    all_triples = []
    all_docs = {}
    errors = 0
    
    for f, text in content_files:
        try:
            result = extract_metadata(text, f.name)
            doc_id = result["doc_id"]
            
            # Merge entities (dedup by name)
            for name, info in result["entities"].items():
                if name in all_entities:
                    # Keep the more descriptive source
                    if len(info.get("source", "")) > len(all_entities[name].get("source", "")):
                        all_entities[name]["source"] = info["source"]
                else:
                    all_entities[name] = info
            
            all_triples.extend(result["triples"])
            all_docs[doc_id] = {"num_triples": len(result["triples"]), "filename": f.name}
            
            nota = doc_id.replace("NT_", "")
            print(f"  ✓ {f.name[:60]:<60} {len(result['triples']):>4} triples | {nota}")
        except Exception as e:
            print(f"  ✗ {f.name}: {e}")
            errors += 1
    
    print(f"\n{'=' * 60}")
    print(f"EXTRACTION COMPLETE")
    print(f"{'=' * 60}")
    print(f"Documents processed: {len(content_files)}")
    print(f"Total triples: {len(all_triples)}")
    print(f"Unique entities: {len(all_entities)}")
    
    # Stats
    type_counts = defaultdict(int)
    for info in all_entities.values():
        type_counts[info["type"]] += 1
    print(f"\nEntity types:")
    for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")
    
    # Show top markets
    markets = [(n, i) for n, i in all_entities.items() if i["type"] == "Mercado"]
    markets.sort(key=lambda x: len([t for t in all_triples if t["object"] == x[0]]), reverse=True)
    print(f"\nTop markets detected:")
    for name, _ in markets[:10]:
        count = len([t for t in all_triples if t["object"] == name])
        print(f"  - {name} ({count} refs)")
    
    # Save
    with open(GRAPH_DIR / "entities.json", "w", encoding="utf-8") as f:
        json.dump(all_entities, f, ensure_ascii=False, indent=2)
    with open(GRAPH_DIR / "triples.json", "w", encoding="utf-8") as f:
        json.dump(all_triples, f, ensure_ascii=False, indent=2)
    with open(GRAPH_DIR / "documents.json", "w", encoding="utf-8") as f:
        json.dump(all_docs, f, ensure_ascii=False, indent=2)
    
    print(f"\nOutput saved to: {GRAPH_DIR}/")


if __name__ == "__main__":
    main()