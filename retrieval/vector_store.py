import json
from pathlib import Path

import faiss
import numpy as np

from retrieval.embeddings import embed_texts


VECTOR_DIR = Path("data/vector_store")
VECTOR_DIR.mkdir(parents=True, exist_ok=True)


def build_vector_store(chunk_file: Path):
    print("Loading chunks...")

    with open(chunk_file, "r") as f:
        data = json.load(f)

    chunks = data["chunks"]
    texts = [c["text"] for c in chunks if c["text"].strip()]

    print(f"Embedding {len(texts)} chunks...")
    embeddings = embed_texts(texts)

    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))

    faiss.write_index(index, str(VECTOR_DIR / "cfa.index"))

    with open(VECTOR_DIR / "metadata.json", "w") as f:
        json.dump(chunks, f, indent=2)

    print(f"✅ Vector store built with {len(texts)} chunks")


if __name__ == "__main__":
    chunk_path = Path("data/processed_chunks/5.6 Private Company Valuation.json")
    build_vector_store(chunk_path)
