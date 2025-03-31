import os
# from langchain.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFLoader
# from lan
from src.utils import download_arxiv_paper

def load_paper(arxiv_id):
    """Load a research paper as text from arXiv."""
    pdf_path = download_arxiv_paper(arxiv_id)
    if not pdf_path:
        print("Failed to download paper")
        return None
    
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    
    return documents
