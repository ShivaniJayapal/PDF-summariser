import streamlit as st
from utils import load_pdf_text, summarize_pdf
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="AI PDF Summarizer", layout="centered")

# Custom styling
st.markdown("""
    <style>
    body {
        background-color: #000;
    }
    .main {
        background-color: #000;
        color: white;
    }
    h1 {
        color: #FFD700;
        text-align: center;
        font-size: 3rem;
        text-shadow: 0 0 15px #FFD700;
    }
    p {
        text-align: center;
        color: #ccc;
        font-size: 1.1rem;
    }
    .stButton>button {
        background-color: #FFD700;
        color: #000;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px 20px;
        margin-top: 10px;
        box-shadow: 0 0 15px #FFD700;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>📄 AI PDF Summarizer</h1>", unsafe_allow_html=True)
st.markdown("<p>Summarize your PDF using OpenAI and LangChain.</p>", unsafe_allow_html=True)

# Upload and Summarize
uploaded_file = st.file_uploader("Upload PDF File", type=["pdf"])

if uploaded_file:
    st.success(f"{uploaded_file.name} uploaded.")
    if st.button("✨ Summarize"):
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("Generating summary..."):
            pages = load_pdf_text("temp.pdf")
            summary = summarize_pdf(pages, openai_api_key)

        st.subheader("📌 Summary")
        st.write(summary)
