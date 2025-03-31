import streamlit as st
from run import process_paper, query_llm

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="LLM Research Paper Assistant",
    page_icon="📚",
    layout="wide"
)

# --- SIDEBAR ---
st.sidebar.title("📑 Research Paper Assistant")
st.sidebar.markdown("Process and query research papers using LLMs.")

# --- MAIN UI ---
st.title("🔍 LLM Research Paper Assistant")

# --- PROCESSING ARXIV PAPER ---
st.subheader("📜 Process ArXiv Paper")
arxiv_id = st.text_input("Enter ArXiv Paper ID:")
if st.button("📂 Process Paper", use_container_width=True):
    with st.spinner("🔄 Processing paper... Please wait!"):
        try:
            paper_summary = process_paper(arxiv_id)
            st.success("Paper Processed Successfully!")
            st.write(paper_summary)
        except Exception as e:
            st.error(f"⚠️ Error: {e}")

# --- QUERY ABOUT PAPER ---
st.markdown("---")  # Horizontal Line
st.subheader("💡 Ask a Question About the Paper")
query = st.text_input("🔎 Enter your question:")
if st.button("💬 Get Answer", use_container_width=True):
    with st.spinner("🤖 Thinking..."):
        try:
            answer = query_llm(query)
            st.success("✅ Answer Generated!")
            st.write(answer)
        except Exception as e:
            st.error(f"⚠️ Error: {e}")

# --- FOOTER ---
st.markdown("---")
st.markdown(
    "🔬 Built for **LLM Research** | Powered by **LangChain & Streamlit**",
    unsafe_allow_html=True
)
