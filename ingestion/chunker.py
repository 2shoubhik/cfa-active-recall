import json
from pathlib import Path
from typing import List, Dict

from ingestion.pdf_loader import load_pdf


PROCESSED_DIR = Path("data/processed_chunks")
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def simple_chunk(pages: List[Dict], max_chars: int = 1500) -> List[Dict]:
    """
    Chunk pages into roughly concept-sized blocks.
    """
    chunks = []
    current_text = ""
    start_page = pages[0]["page"]

    for page in pages:
        if len(current_text) + len(page["text"]) <= max_chars:
            current_text += " " + page["text"]
        else:
            chunks.append({
                "text": current_text.strip(),
                "pages": [start_page, page["page"] - 1]
            })
            current_text = page["text"]
            start_page = page["page"]

    if current_text:
        chunks.append({
            "text": current_text.strip(),
            "pages": [start_page, pages[-1]["page"]]
        })

    return chunks


def process_pdf(pdf_name: str):
    data = load_pdf(pdf_name)
    pages = data["pages"]

    chunks = simple_chunk(pages)

    output = {
        "source": pdf_name,
        "num_chunks": len(chunks),
        "chunks": chunks
    }

    out_file = PROCESSED_DIR / f"{pdf_name.replace('.pdf','')}.json"
    with open(out_file, "w") as f:
        json.dump(output, f, indent=2)

    print(f"Saved {len(chunks)} chunks to {out_file}")


if __name__ == "__main__":
    pdf_name = "5.6 Private Company Valuation.pdf"
    process_pdf(pdf_name)
