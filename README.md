conda deactivate
conda remove --name llm_research --all -y
conda create --name llm_research python=3.10 -y
conda activate llm_research
pip install --upgrade langchain langchain-community
python -c "import langchain_community; print('LangChain is working!')"
