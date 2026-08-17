import os
from dotenv import load_dotenv
load_dotenv()
from langchain_community.document_loaders import PyPDFLoader

# laoding pdf doc from the folder
def document():
    loader=PyPDFLoader("../documents/SaiKrishna2026.pdf")
    doc=loader.load()
    return doc


if __name__=="__main__":
    document()