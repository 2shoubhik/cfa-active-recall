import os
from typing import List, Dict
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


ACTIVE_RECALL_PROMPT = """
You are a CFA Institute examiner.

You are given official CFA study text excerpts below.
Your task is to generate ACTIVE RECALL QUESTIONS that test conceptual understanding.

RULES:
- Use ONLY the provided text
- Do NOT introduce external knowledge
- Each question must be directly answerable from the text
- Focus on WHY, COMPARE, and EXPLAIN type questions
- Avoid rote definition questions

For each question:
- Provide the question
- Provide a short ideal answer
- Cite the page numbers used

OUTPUT FORMAT (JSON ONLY):
{
  "active_recall_questions": [
    {
      "question": "...",
      "ideal_answer": "...",
      "source_pages": [x, y]
    }
  ]
}
"""


def generate_active_recall(chunks: List[Dict], num_questions: int = 3) -> Dict:
    """
    Generate active recall questions from retrieved CFA chunks.
    """

    context = ""
    for c in chunks:
        context += f"\n[Pages {c['pages']}]\n{c['text']}\n"

    user_prompt = f"""
CFA TEXT:
{context}

Generate {num_questions} high-quality active recall questions.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": ACTIVE_RECALL_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
