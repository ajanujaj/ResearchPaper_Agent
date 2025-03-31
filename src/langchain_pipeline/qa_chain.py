import ollama
from langchain.chains import RetrievalQA
from langchain.llms import Ollama
from src.langchain_pipeline.vector_store import load_vector_store
from src.config import OLLAMA_MODEL
from src.langraph_workflow.Agent_prompt import RESEARCH_PAPER_PROMPT
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.schema.runnable import RunnablePassthrough
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

def get_llm_response(query):
    """Use the Ollama LLM model to answer a research question."""
    vectorstore = load_vector_store()
    
    if not vectorstore:
        return "No vector database found. Please process research papers first."

    retriever = vectorstore.as_retriever()
    llm = Ollama(model=OLLAMA_MODEL) 

    docs = retriever.get_relevant_documents(query)
    context = "\n\n".join([doc.page_content for doc in docs]) if docs else "No relevant context found."

    # print(context)

    llm = Ollama(model=OLLAMA_MODEL)

    document_chain = create_stuff_documents_chain(llm, RESEARCH_PAPER_PROMPT)

    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    # response = retrieval_chain.invoke({"context": context, "question": query})
    response = retrieval_chain.invoke({"input": context, "question": query})

    return response