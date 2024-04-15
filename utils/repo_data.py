import nbformat
import requests
from functools import lru_cache


#For extracting repo data from ipynb files in the dataset
@lru_cache(maxsize=128)
def extract_code_data_ipynb(github_url, cell_type="code"):
    raw_url = github_url.replace("github.com", "raw.githubusercontent.com").replace(
        "/blob/", "/"
    )

    response = requests.get(raw_url)
    response.raise_for_status()  # Check for any request errors

    notebook_content = response.text

    notebook = nbformat.reads(notebook_content, as_version=nbformat.NO_CONVERT)

    python_code = None

    for cell in notebook.cells:
        if cell.cell_type == cell_type:
            if not python_code:
                python_code = cell.source
            else:
                python_code += "\n" + cell.source

    return python_code



@lru_cache(maxsize=128)
def extract_code_data_py(github_url):
    raw_url = github_url.replace("github.com", "raw.githubusercontent.com").replace(
        "/blob/", "/"
    )

    response = requests.get(raw_url)
    response.raise_for_status()  # Check for any request errors

    python_code = response.text

    return python_code