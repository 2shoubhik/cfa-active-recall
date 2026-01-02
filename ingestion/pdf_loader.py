print("PDF loader script started")

from pathlib import Path
from pypdf import PdfReader


RAW_PDF_DIR = Path("data/raw_pdfs")


def load_pdf(pdf_name: str) -> dict:
    """
    Load a CFA PDF and extract text page by page.

    Returns:
        {
            "source": pdf_name,
            "pages": [
                {"page": 1, "text": "..."},
                ...
            ]
        }
    """
    pdf_path = RAW_PDF_DIR / pdf_name

    if not pdf_path.exists():
        raise FileNotFoundError(f"{pdf_name} not found in raw_pdfs")

    reader = PdfReader(pdf_path)

    pages = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        text = text.replace("\n", " ").strip()

        pages.append({
            "page": i + 1,
            "text": text
        })

    return {
        "source": pdf_name,
        "pages": pages
    }


if __name__ == "__main__":
    # quick test
    sample_pdf = next(RAW_PDF_DIR.iterdir()).name
    data = load_pdf(sample_pdf)
    print(f"Loaded {len(data['pages'])} pages from {sample_pdf}")
    print(data["pages"][0]["text"][:500])
