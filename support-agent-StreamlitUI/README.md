# Thoughtful AI – Customer Support Agent

This project implements a lightweight customer‑support AI Agent for answering common questions about **Thoughtful AI’s automation agents**.  
It uses:

- A **hardcoded Q&A dataset** for known questions  
- A **simple retrieval layer** (fuzzy matching)  
- A **fallback LLM response** for all other queries  
- A clean **Streamlit chat UI**


---

## 🚀 Features

- Conversational chat interface  
- Hardcoded knowledge base for Thoughtful AI  
- Fuzzy matching to find the closest predefined answer  
- Graceful fallback to an LLM (OpenAI, Anthropic, or any provider)  
- Error handling for unexpected inputs  
- Fully contained in a single Python file

 ![Thoughtful AI Customer Support Agent](./saslui.png)


---

## Architecture

```mermaid
flowchart LR
  A[User / Browser] --> B[Streamlit Chat UI]
  B --> C[Fuzzy Retrieval-rapidfuzz]
  C -->|score >= 70| D[Hardcoded Q&A Dataset]
  C -->|score < 70| E[LLM Fallback]
  E --> F[OpenAI Client-openai]
  F --> G[OpenAI API]
  D --> B
  G --> F
  F --> B
  subgraph Env
    H[.env -OPENAI_API_KEY]
    I[.venv / run.ps1 / requirements.txt]
  end
  H --> F
  I --> B
```

Notes:
- The app first attempts a local retrieval from the hardcoded dataset. If no confident match is found (threshold: 70), it falls back to the LLM.
- Secrets (API keys) are loaded from `.env`. The `run.ps1` script installs pinned dependencies from `requirements.txt` into the `.venv` and launches Streamlit.

---
**Built with AI**

Last Updated: February 17, 2026

---

