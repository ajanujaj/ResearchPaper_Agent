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


LLM_QA_RP/
│── README.md               # Project documentation
│── run.py                  # Main script to run the QA system
│── requirements.txt         # List of dependencies
│
├── src/langchain_pipeline/
│   ├── qa_chain.py          # Core LangChain pipeline for retrieval and answering
│   ├── prompt_template.py   # Contains the prompt structure for the LLM
│   ├── retriever.py         # Manages document retrieval
│
├── data/                    # Stores research papers (if applicable)
└── tests/                   # Unit tests for QA pipeline


#### To modify the template. 
src/langraph_workflow/Agent_prompt.py