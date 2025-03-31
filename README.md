# **LLM QA Research Project**

This project is a **Question-Answering (QA) system** built using **LangChain**, **Ollama**, and **Retrieval-Augmented Generation (RAG)** techniques. It processes research papers and provides insightful responses to user queries.

---

## **Installation & Setup**

### **1️⃣ Create & Activate Conda Environment**
```bash
conda deactivate
conda remove --name llm_research --all -y
conda create --name llm_research python=3.10 -y
conda activate llm_research
pip install -r requirements.txt
pip install --upgrade langchain langchain-community
python -c "import langchain_community; print('LangChain is working!')"
```

#### project structure
```bash
LLM_QA_RP/
│── README.md               # Project documentation
│── run.py                  # Main script to run the QA system
│── requirements.txt        # List of dependencies
│── app.py                  # run using streamlit
│
├── src/langchain_pipeline/
│   ├── qa_chain.py          # Core LangChain pipeline for retrieval and answering
│   ├── text_prepocessing.py 
│   ├── vector_store.py      
│   ├── load_papers.py      
├── src/langchain_workflow/
│   ├── Agent_prompt.py 
├── src/utils.py
├── src/config.py
```

#### To modify the template. 
```bash
src/langraph_workflow/Agent_prompt.py
```