from langchain_google_vertexai import VertexAIEmbeddings 
from utils.repo_data import (
    extract_code_data_ipynb,
    extract_code_data_py,
)
from config import DATASET_PATH
from langchain.schema.document import Document
from langchain.text_splitter import Language
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
import streamlit as st
from google.cloud import aiplatform

EMBEDDING_QPM = 100
EMBEDDING_NUM_BATCH = 5
TOP_K_NUM = 3

@st.cache_resource
def generate_code_strings(data_repo):
    code_strings = []
    for i in range(0, len(data_repo)):
        if data_repo[i].endswith(".ipynb"):
            content = extract_code_data_ipynb(data_repo[i], "code")
            doc = Document(
                page_content=content,
                metadata={"url": data_repo[i], "file_index": i},
            )
            code_strings.append(doc)
        elif data_repo[i].endswith(".py"):
            content = extract_code_data_py(data_repo[i])
            doc = Document(
                page_content=content,
                metadata={"url": data_repo[i], "file_index": i},
            )
            code_strings.append(doc)
    return code_strings


def get_retriever(code_strings):
    text_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON, chunk_size=1000, chunk_overlap=150
    )
    texts = text_splitter.split_documents(code_strings)

    embeddings = VertexAIEmbeddings(
        requests_per_minute=EMBEDDING_QPM,
        num_instances_per_batch=EMBEDDING_NUM_BATCH,
        model_name="textembedding-gecko@latest",
        project="896936970354"
    )

    db = FAISS.from_documents(texts, embeddings)

    retriever = db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": TOP_K_NUM},
    )
    return retriever