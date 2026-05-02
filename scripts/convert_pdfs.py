#!/usr/bin/env python3
"""
Re-convert empty/failed MD files from PDFs using pymupdf4llm.
Falls back to markitdown if pymupdf fails.
"""
import sys
import subprocess
from pathlib import Path

def convert_with_pymupdf(pdf_path: str) -> str | None:
    """Try pymupdf4llm first - handles both text and image-based PDFs."""
    try:
        import pymupdf4llm
        md_text = pymupdf4llm.to_markdown(pdf_path)
        if md_text and len(md_text.strip()) > 50:
            return md_text
    except Exception as e:
        print(f"  pymupdf4llm error: {e}", file=sys.stderr)
    return None

def convert_with_pymupdf_raw(pdf_path: str) -> str | None:
    """Try raw pymupdf text extraction as fallback."""
    try:
        import pymupdf
        doc = pymupdf.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text() + "\n\n"
        doc.close()
        if text and len(text.strip()) > 50:
            return text
    except Exception as e:
        print(f"  pymupdf raw error: {e}", file=sys.stderr)
    return None

def convert_with_markitdown(pdf_path: str) -> str | None:
    """Try markitdown CLI as last resort."""
    try:
        result = subprocess.run(
            ["markitdown", pdf_path],
            capture_output=True, text=True, timeout=120
        )
        if result.returncode == 0 and result.stdout and len(result.stdout.strip()) > 50:
            return result.stdout
    except Exception as e:
        print(f"  markitdown error: {e}", file=sys.stderr)
    return None

def main():
    raw_dir = Path("~/brain_cade/raw/notas/").expanduser()
    md_dir = Path("~/brain_cade/md/").expanduser()
    md_dir.mkdir(parents=True, exist_ok=True)

    # Find all MDs that are empty/tiny
    empty_mds = []
    for md in sorted(md_dir.glob("*.md")):
        if md.stat().st_size < 100:
            pdf_path = raw_dir / (md.stem + ".pdf")
            if pdf_path.exists():
                empty_mds.append((md, pdf_path))

    # Also find PDFs with no MD at all
    pdf_stems = {f.stem for f in raw_dir.glob("*.pdf")}
    md_stems = {f.stem for f in md_dir.glob("*.md")}
    missing = pdf_stems - md_stems
    for stem in missing:
        pdf_path = raw_dir / (stem + ".pdf")
        md_path = md_dir / (stem + ".md")
        if pdf_path.exists():
            empty_mds.append((md_path, pdf_path))

    print(f"Found {len(empty_mds)} PDFs to (re-)convert\n")

    success = 0
    failed = 0

    for md_path, pdf_path in empty_mds:
        print(f"Converting: {pdf_path.name} ({pdf_path.stat().st_size/1024:.0f} KB)")
        
        # Try converters in order of quality
        md_text = convert_with_pymupdf(str(pdf_path))
        if md_text is None:
            md_text = convert_with_pymupdf_raw(str(pdf_path))
        if md_text is None:
            md_text = convert_with_markitdown(str(pdf_path))

        if md_text:
            md_path.write_text(md_text, encoding="utf-8")
            print(f"  ✓ Saved {len(md_text):,} chars to {md_path.name}")
            success += 1
        else:
            # Write a placeholder so we know it failed
            md_path.write_text(f"[CONVERSION FAILED - PDF may be image-only/scanned]\nSource: {pdf_path.name}\n", encoding="utf-8")
            print(f"  ✗ FAILED - could not extract text")
            failed += 1

    print(f"\n=== RESULTS ===")
    print(f"Success: {success}")
    print(f"Failed:  {failed}")
    print(f"Total:   {len(empty_mds)}")

    # Summary of all MDs
    all_mds = list(md_dir.glob("*.md"))
    content_count = sum(1 for m in all_mds if m.stat().st_size > 100)
    print(f"\nTotal MD files with content: {content_count}/{len(all_mds)}")

if __name__ == "__main__":
    main()