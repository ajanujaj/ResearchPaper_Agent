from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_community.embeddings import OllamaEmbeddings  # Using Ollama instead of OpenAI

# Load Ollama's local embedding model
embeddings = OllamaEmbeddings(model="nomic-embed-text")

def create_vector_store(chunks):
    """Converts text chunks into FAISS vector store using Ollama embeddings."""
    
    if not isinstance(chunks, list) or not all(isinstance(doc, Document) for doc in chunks):
        raise ValueError("Chunks must be a list of Document objects")

    # Extract text and metadata from Document objects
    texts = [doc.page_content for doc in chunks]  # Extract only text
    metadatas = [doc.metadata for doc in chunks]  # Extract metadata
    
    # Generate vector store using local Ollama embeddings
    vector_db = FAISS.from_texts(texts, embeddings, metadatas=metadatas)

    # Save the vector store locally
    vector_db.save_local("data/vectorstore/")  
    return vector_db

def load_vector_store():
    """Load the FAISS vector database from local storage using Ollama embeddings."""
    return FAISS.load_local("data/vectorstore/", embeddings, allow_dangerous_deserialization=True)

