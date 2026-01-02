import sys
from pathlib import Path
import json

# Add project root to Python path
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

import streamlit as st

from retrieval.search import search
from recall_engine.question_generator import generate_active_recall


st.set_page_config(page_title="CFA Active Recall", layout="centered")

st.title("📘 CFA Active Recall Engine")
st.write("Generate exam-focused active recall questions from CFA content.")

query = st.text_input(
    "What do you want to revise?",
    placeholder="e.g. public vs private company valuation"
)

num_questions = st.slider(
    "Number of active recall questions",
    min_value=1,
    max_value=5,
    value=3
)

if st.button("Generate Active Recall"):
    if not query.strip():
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Retrieving CFA content and generating questions..."):
            chunks = search(query, top_k=3)
            output = generate_active_recall(chunks, num_questions=num_questions)

        st.subheader("🧠 Active Recall Questions")
        try:
            parsed = json.loads(output)
            questions = parsed["active_recall_questions"]
            
            for i, q in enumerate(questions, 1):
                st.markdown(f"### ❓ Question {i}")
                st.write(q["question"])
                
                with st.expander("💡 Reveal Ideal Answer"):
                    st.write(q["ideal_answer"])
                    st.caption(f"Source pages: {q['source_pages']}")
                    
        except Exception as e:
            st.error("Could not parse AI output.")
            st.text(output)
