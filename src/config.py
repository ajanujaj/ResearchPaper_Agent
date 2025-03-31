import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Ollama Model Name
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")  # Change to your preferred model

# Vector DB Path
VECTOR_DB_PATH = "data/vectorstore/faiss_index"

# Chunking Parameters
CHUNK_SIZE = 512
CHUNK_OVERLAP = 50