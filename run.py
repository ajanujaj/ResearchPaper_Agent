from src.langchain_pipeline.load_papers import load_paper
from src.langchain_pipeline.text_processing import chunk_text
from src.langchain_pipeline.vector_store import create_vector_store
from src.langchain_pipeline.qa_chain import get_llm_response

def process_paper(arxiv_id):
    """Download, process, and store a research paper."""
    documents = load_paper(arxiv_id)
    if not documents:
        return "Error: Could not process the paper."
    
    chunks = chunk_text(documents)
    print(type(chunks))
    create_vector_store(chunks)
    return "Paper processed successfully."

def query_llm(question):
    """Ask a question and get an answer from the LLM."""
    return get_llm_response(question)

if __name__ == "__main__":
    # Example Usage
    arxiv_id = "2301.00001"  # Example ArXiv ID
    print(process_paper(arxiv_id))

    query = "What are the key findings of the paper?"
    print(query_llm(query))
