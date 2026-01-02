from retrieval.search import search
from recall_engine.question_generator import generate_active_recall

query = "differences between public and private company valuation"

chunks = search(query, top_k=3)

output = generate_active_recall(chunks)

print(output)
