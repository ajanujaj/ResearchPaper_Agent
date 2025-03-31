import os
import arxiv
import requests

def download_arxiv_paper(arxiv_id, save_dir="data/papers"):
    """Download a research paper from arXiv as a PDF."""
    os.makedirs(save_dir, exist_ok=True)
    paper = next(arxiv.Search(id_list=[arxiv_id]).results())
    pdf_url = paper.pdf_url
    response = requests.get(pdf_url)
    
    if response.status_code == 200:
        file_path = os.path.join(save_dir, f"{arxiv_id}.pdf")
        with open(file_path, "wb") as f:
            f.write(response.content)
        return file_path
    return None
