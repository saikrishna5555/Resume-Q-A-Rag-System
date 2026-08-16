from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from chunks import chunks

embedding_model=SentenceTransformer("all-minilm-l6-v2")
def embeddings():
    chunks_doc=chunks()
    text=[chunk.page_content for chunk in chunks_doc]
    embedding_vector=embedding_model.encode(text,normalize_embeddings=True)
    return embedding_vector
    # vectorstore
def vector_store():
    embe_vector=embeddings()
    dimensions=embe_vector.shape[1]
    index=faiss.IndexFlatL2(dimensions)
    index.add(
        np.array(embe_vector,dtype="float32")
    )
    return index

if __name__=="__main__":
    embeddings()
    vector_store()

