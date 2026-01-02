import json
from pathlib import Path
import faiss
import numpy as np

from retrieval.embeddings import embed_texts

VECTOR_DIR = Path("data/vector_store")


def search(query: str, top_k: int = 3):
    index = faiss.read_index(str(VECTOR_DIR / "cfa.index"))

    with open(VECTOR_DIR / "metadata.json", "r") as f:
        metadata = json.load(f)

    query_embedding = embed_texts([query])[0]

    D, I = index.search(
        np.array([query_embedding]).astype("float32"),
        top_k
    )

    results = []
    for idx in I[0]:
        chunk = metadata[idx]
        if chunk["text"].strip():
            results.append(chunk)


    return results


if __name__ == "__main__":
    query = "differences between public and private company valuation"
    results = search(query)

    for i, r in enumerate(results, 1):
        print(f"\nResult {i} (pages {r['pages']}):\n")
        print(r["text"][:500])
