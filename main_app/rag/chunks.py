from langchain_text_splitters import RecursiveCharacterTextSplitter
from doc_loader import document
def chunks():
    doc=document()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n","\n","."," ",""])
    chunk=splitter.split_documents(doc)

    return chunk


if __name__=="__main__":
    chunks()