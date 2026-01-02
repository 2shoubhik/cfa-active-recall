import os
from typing import List
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def embed_texts(
    texts: List[str],
    batch_size: int = 10
) -> List[List[float]]:
    """
    Generate embeddings safely by:
    - removing empty texts
    - batching requests
    """
    clean_texts = [t for t in texts if t and t.strip()]

    if not clean_texts:
        raise ValueError("No valid text chunks to embed.")

    all_embeddings = []

    for i in range(0, len(clean_texts), batch_size):
        batch = clean_texts[i:i + batch_size]

        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=batch
        )

        batch_embeddings = [item.embedding for item in response.data]
        all_embeddings.extend(batch_embeddings)

    return all_embeddings
