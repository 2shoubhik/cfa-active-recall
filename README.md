# 📘 CFA Active Recall Engine

The CFA L2 exam is tough! Believe me, I know how brutal it can be to remember chunks of information from each of the 10 modules while managing other responsibilities in your life. 

As a fellow L2 candidate, I have created this fun study tool to help candidates (including myself) gear up for exam-style questions while going through the material. After not passing this exam in my initial attempt, I believe the strategy is to complement learning with practice questions throughout the duration of exam prep.

This AI project uses a **retrieval-augmented generation (RAG)** architecture to generate CFA-focused questions directly from official curriculum PDFs, ensuring all outputs are grounded in source material.

---

## 🎯 Why this project exists

CFA preparation is often inefficient:
- Passive reading isn't enough to remember several chunks of information
- Highlighting doesn’t expose weak areas
- Generic question banks don’t adapt to your gaps

This tool focuses on:
- **Active recall**
- **Exam-relevant reasoning**
- **Source-grounded questions**

The goal is not to replace studying — but to make studying **far more effective**.

---

## 🧠 How it works (high level)

1. **Curriculum ingestion**
   - CFA PDFs are parsed and cleaned
   - Text is chunked into concept-sized sections

2. **Semantic indexing**
   - Chunks are embedded using OpenAI embeddings
   - Stored in a FAISS vector database for fast retrieval

3. **Retrieval-first querying**
   - User queries retrieve only relevant curriculum text
   - Prevents hallucination and keeps outputs exam-accurate

4. **Question generation**
   - An LLM acts as a CFA examiner
   - Generates active recall questions grounded strictly in retrieved text

5. **Interactive UI**
   - Streamlit-based interface
   - Questions displayed with revealable answers and source references

---

## 🛠️ Tech stack

- **Python**
- **OpenAI API** (embeddings + generation)
- **FAISS** (vector search)
- **Streamlit** (interactive UI)

---

## ✅ Current features

- Semantic search across CFA curriculum content
- Active recall question generation
- Interactive Streamlit UI (non-terminal)
- Source-page attribution for each question

---

## 🚧 Planned features

- CFA-style MCQs with realistic distractors
- Difficulty levels (easy / exam / brutal)
- Multi-module curriculum support
- Weak-area tracking and revision prioritization

---

## ⚠️ Disclaimer

This project is for **educational purposes only**.  
It is not affiliated with, endorsed by, or connected to the CFA Institute.

---

## 👤 Author

Built by **Shoubhik Bhattacharya** as a personal project to explore applied AI systems and improve CFA exam preparation efficiency.
