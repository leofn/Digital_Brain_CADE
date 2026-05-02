#!/usr/bin/env python3
"""
Digital Brain CADE - Extraction Pipeline
=========================================

Extracts structured knowledge triples from CADE Notas Técnicas.

Two-phase approach:
1. STRUCTURAL: Parse metadata from document headers (nota number, year, 
   companies, process numbers, markets)
2. SEMANTIC: Use LLM to extract relationships from ementas and key sections

Output: JSON files in ~/brain_cade/graph/
  - entities.json: All entities with types
  - triples.json: All subject-predicate-object triples
  - documents.json: Per-document metadata summary
"""
import json
import re
import sys
from pathlib import Path
from datetime import datetime

MD_DIR = Path("~/brain_cade/md/").expanduser()
GRAPH_DIR = Path("~/brain_cade/graph/").expanduser()
GRAPH_DIR.mkdir(parents=True, exist_ok=True)


def extract_structural_metadata(text: str, filename: str) -> dict:
    """Phase 1: Extract metadata from document headers without LLM."""
    metadata = {
        "source_file": filename,
        "nota_number": None,
        "nota_year": None,
        "process_number": None,
        "process_type": None,
        "requerentes": [],
        " terceiros": [],
        "advogados": [],
        "mercados": [],
        "ementa": None,
        "autores": [],
        "departamento": None,
        "testes_metodologicos": [],
    }

    # Extract nota number and year
    nota_match = re.search(
        r'NOTA\s*T[ÉE]CNICA\s*[Nn][º°o\.]*\s*(\d{1,3})\s*/\s*(\d{4})',
        text, re.IGNORECASE
    )
    if nota_match:
        metadata["nota_number"] = int(nota_match.group(1))
        metadata["nota_year"] = int(nota_match.group(2))

    # Extract process number (format: 08700.XXXXXX/YYYY-XX or 08012.XXXXXX/YYYY-XX)
    process_matches = re.findall(
        r'(?:autos\s*n[º°o]*|processo\s*n[º°o]*|Ato\s*de\s*Concentra[çc][aãâ][oõ]?\s*n[º°o]*)\s*(\d{5}\.\d{6}/\d{4}-\d{2})',
        text, re.IGNORECASE
    )
    # Also try from filename
    if not process_matches:
        fn_match = re.search(r'(\d{5}_\d{6}_\d{4}_\d{2})', filename)
        if fn_match:
            process_matches = [fn_match.group(1).replace('_', '/')]

    if process_matches:
        metadata["process_number"] = process_matches[0]

    # Extract process type
    type_match = re.search(
        r'(Ato\s*de\s*Concentra[çc][aãâ][oõ]?\s+\w+)',
        text, re.IGNORECASE
    )
    if type_match:
        metadata["process_type"] = type_match.group(1).strip()

    # Extract requerentes (companies involved)
    req_section = re.search(
        r'Requerentes?\s*:\s*(.+?)(?:\n\n|\nEmenta|\nAdvogad)',
        text, re.IGNORECASE | re.DOTALL
    )
    if req_section:
        req_text = req_section.group(1)
        # Split by common separators
        companies = re.split(r'[;,\n]|(?:\s+e\s+)', req_text)
        companies = [c.strip().strip('""''""') for c in companies if len(c.strip()) > 3]
        # Clean up "(\"xxx\")" patterns
        cleaned = []
        for c in companies:
            # Remove quotes and parenthetical trade names
            c = re.sub(r'\(["\'](.+?)["\']\)', r'(\1)', c)
            c = c.strip(' .,;')
            if c:
                cleaned.append(c)
        metadata["requerentes"] = cleaned[:10]  # Cap at 10 to avoid noise

    # Extract ementa
    ementa_match = re.search(
        r'Ementa\s*:\s*(.+?)(?:\n\d+\.|\n\n|\n[A-Z][a-z])',
        text, re.IGNORECASE | re.DOTALL
    )
    if ementa_match:
        ementa = ementa_match.group(1).strip()
        # Truncate very long ementas
        if len(ementa) > 2000:
            ementa = ementa[:2000] + "..."
        metadata["ementa"] = ementa

    # Extract autores
    autor_match = re.search(
        r'(?:Autor(?:es)?|Elabora[çc][aãâ]o)\s*:\s*(.+?)(?:\n\n|\nSum[áa]rio|\nObjeto)',
        text, re.IGNORECASE | re.DOTALL
    )
    if autor_match:
        autores = re.split(r'[\n,;]', autor_match.group(1))
        autores = [a.strip() for a in autores if len(a.strip()) > 2]
        metadata["autores"] = autores[:5]

    # Extract departamento
    dep_match = re.search(
        r'Departamento\s*de\s*Estudos\s*Econ[oô]micos',
        text, re.IGNORECASE
    )
    if dep_match:
        metadata["departamento"] = "DEE/CADE"

    # Extract methodology keywords
    test_keywords = [
        "GUPPI", "UPP", "CPPI", "HHI", "SSNIP", "merger simulation",
        "regress[aãâ]o", "diff-in-diff", "diferen[çc]as-em-diferen[çc]as",
        "elasticidade", "herfindahl", "concentra[çc][aãâ]o",
        "efeitos unilaterais", "efeitos coordenados", "efici[eê]ncias",
        "barreira[s] de entrada", "poder de mercado", "pre[çc]o",
    ]
    found_tests = []
    for kw in test_keywords:
        if re.search(kw, text, re.IGNORECASE):
            found_tests.append(kw.replace('[aãâ]', 'a').replace('[çc]', 'c').replace('[eê]', 'e').replace('[oô]', 'o'))
    metadata["testes_metodologicos"] = list(set(found_tests))

    # Extract market segments mentioned
    market_patterns = [
        r'mercado(?:s)?\s+de\s+([\w\s]+?)(?:\.|,|;\n|e\s+mercado|nas\s|n[ao]s?\s+mercado)',
        r'setor(?:es)?\s+de\s+([\w\s]+?)(?:\.|,|;\n)',
    ]
    markets = set()
    for pattern in market_patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            m = match.group(1).strip().lower()
            if 5 < len(m) < 80:
                markets.add(m)
    metadata["mercados"] = list(markets)[:15]  # Cap

    return metadata


def metadata_to_triples(metadata: dict) -> list[dict]:
    """Convert structural metadata to knowledge triples."""
    triples = []
    doc_id = f"NT_{metadata.get('nota_number', '?')}_{metadata.get('nota_year', '?')}"

    # Document-level triples
    if metadata.get("nota_number"):
        triples.append({
            "subject": doc_id,
            "predicate": "tipo",
            "object": "Nota Técnica CADE"
        })

    if metadata.get("nota_year"):
        triples.append({
            "subject": doc_id,
            "predicate": "ano",
            "object": str(metadata["nota_year"])
        })

    if metadata.get("departamento"):
        triples.append({
            "subject": doc_id,
            "predicate": "departamento",
            "object": metadata["departamento"]
        })

    # Process number
    if metadata.get("process_number"):
        triples.append({
            "subject": doc_id,
            "predicate": "processo",
            "object": metadata["process_number"]
        })

    # Companies -> market relationships
    for req in metadata.get("requerentes", []):
        triples.append({
            "subject": req,
            "predicate": "requerente_em",
            "object": doc_id
        })

    # Markets
    for merc in metadata.get("mercados", []):
        triples.append({
            "subject": doc_id,
            "predicate": "analisa_mercado",
            "object": merc
        })
        for req in metadata.get("requerentes", []):
            triples.append({
                "subject": req,
                "predicate": "atua_em",
                "object": merc
            })

    # Methodology
    for test in metadata.get("testes_metodologicos", []):
        triples.append({
            "subject": doc_id,
            "predicate": "utiliza_metodologia",
            "object": test
        })

    # Authors
    for autor in metadata.get("autores", []):
        triples.append({
            "subject": autor,
            "predicate": "autor_de",
            "object": doc_id
        })

    return triples


def main():
    print("=" * 60)
    print("Digital Brain CADE - Structural Extraction")
    print("=" * 60)

    md_files = sorted(MD_DIR.glob("*.md"))
    content_files = [(f, f.stat().st_size) for f in md_files if f.stat().st_size > 100]

    print(f"Found {len(content_files)} MD files with content")

    all_metadata = []
    all_triples = []
    all_entities = {}

    for md_file, size in content_files:
        text = md_file.read_text(encoding="utf-8", errors="replace")
        metadata = extract_structural_metadata(text, md_file.name)
        triples = metadata_to_triples(metadata)

        all_metadata.append(metadata)
        all_triples.extend(triples)

        # Build entity registry
        doc_id = f"NT_{metadata.get('nota_number', '?')}_{metadata.get('nota_year', '?')}"
        if doc_id not in all_entities:
            all_entities[doc_id] = {"type": "Nota Técnica", "source": md_file.name}

        for req in metadata.get("requerentes", []):
            if req not in all_entities:
                all_entities[req] = {"type": "Empresa", "source": md_file.name}

        for merc in metadata.get("mercados", []):
            if merc not in all_entities:
                all_entities[merc] = {"type": "Mercado", "source": md_file.name}

        for test in metadata.get("testes_metodologicos", []):
            if test not in all_entities:
                all_entities[test] = {"type": "Metodologia", "source": md_file.name}

        for autor in metadata.get("autores", []):
            if autor not in all_entities:
                all_entities[autor] = {"type": "Autor", "source": md_file.name}

        print(f"  ✓ {md_file.name[:60]:<60} | {len(triples):>3} triples | {metadata.get('nota_number', '?')}/{metadata.get('nota_year', '?')}")

    # Save outputs
    with open(GRAPH_DIR / "documents.json", "w", encoding="utf-8") as f:
        json.dump(all_metadata, f, ensure_ascii=False, indent=2)

    with open(GRAPH_DIR / "triples.json", "w", encoding="utf-8") as f:
        json.dump(all_triples, f, ensure_ascii=False, indent=2)

    with open(GRAPH_DIR / "entities.json", "w", encoding="utf-8") as f:
        json.dump(all_entities, f, ensure_ascii=False, indent=2)

    # Stats
    print(f"\n{'=' * 60}")
    print(f"EXTRACTION COMPLETE")
    print(f"{'=' * 60}")
    print(f"Documents processed: {len(all_metadata)}")
    print(f"Total triples: {len(all_triples)}")
    print(f"Unique entities: {len(all_entities)}")

    # Entity type breakdown
    type_counts = {}
    for ent, info in all_entities.items():
        t = info["type"]
        type_counts[t] = type_counts.get(t, 0) + 1
    print(f"\nEntity types:")
    for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")

    # Top markets
    markets = [m for m, info in all_entities.items() if info["type"] == "Mercado"]
    if markets:
        print(f"\nTop markets detected:")
        for m in markets[:10]:
            print(f"  - {m}")

    print(f"\nOutput saved to: {GRAPH_DIR}/")


if __name__ == "__main__":
    main()