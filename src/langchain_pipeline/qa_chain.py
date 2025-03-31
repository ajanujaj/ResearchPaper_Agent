import ollama
from langchain.chains import RetrievalQA
from langchain.llms import Ollama
from src.langchain_pipeline.vector_store import load_vector_store

def get_llm_response(query):
    """Use the Ollama LLM model to answer a research question."""
    vectorstore = load_vector_store()
    
    if not vectorstore:
        return "No vector database found. Please process research papers first."
    
    retriever = vectorstore.as_retriever()
    llm = Ollama(model="mistral")  # Change model as needed
    
    qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever)
    
    response = qa_chain.invoke(query)
    return response
