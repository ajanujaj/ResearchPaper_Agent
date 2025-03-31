from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_text(documents):
    """Splits text from Document objects and returns new Document chunks."""
    
    if not isinstance(documents, list) or not all(isinstance(doc, Document) for doc in documents):
        raise ValueError("Input must be a list of Document objects")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

    # Extract text from documents and split
    chunks = []
    for doc in documents:
        split_texts = text_splitter.split_text(doc.page_content)  # Extract raw text
        chunks.extend([Document(page_content=chunk, metadata=doc.metadata) for chunk in split_texts])

    return chunks
