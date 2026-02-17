import streamlit as st
from rapidfuzz import process
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

# -----------------------------
# Hardcoded Q&A Dataset
# -----------------------------
DATASET = {
    "What does the eligibility verification agent (EVA) do?":
        "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections.",

    "What does the claims processing agent (CAM) do?":
        "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements.",

    "How does the payment posting agent (PHIL) work?":
        "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden.",

    "Tell me about Thoughtful AI's Agents.":
        "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others.",

    "What are the benefits of using Thoughtful AI's agents?":
        "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
}

QUESTIONS = list(DATASET.keys())


# -----------------------------
# Helper: Retrieve Best Match
# -----------------------------
def retrieve_answer(user_input):
    match, score, _ = process.extractOne(user_input, QUESTIONS)

    if score >= 70:
        return DATASET[match]

    return None  # triggers LLM fallback


# -----------------------------
# LLM Fallback
# -----------------------------
def llm_fallback(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful customer support assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"LLM error: {str(e)}"


# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Thoughtful AI Support Agent", page_icon="🤖")
st.title("🤖 Thoughtful AI – Customer Support Agent")

if "chat_history" in st.session_state:
    for role, msg in st.session_state.chat_history:
        st.chat_message(role).write(msg)
else:
    st.session_state.chat_history = []

user_input = st.chat_input("Ask me anything about Thoughtful AI...")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.chat_history.append(("user", user_input))

    # Try retrieving from dataset
    answer = retrieve_answer(user_input)

    if answer is None:
        answer = llm_fallback(user_input)

    st.chat_message("assistant").write(answer)
    st.session_state.chat_history.append(("assistant", answer))