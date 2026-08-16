from embedding import embeddings,vector_store,embedding_model
import numpy as np
from chunks import chunks

def ask_question(query:str):
    query_embeddings=embedding_model.encode([query],normalize_embeddings=True)
    index=vector_store()
    distance,indices=index.search(
        np.array(query_embeddings,dtype="float32"),
        k=4
    )

    rectrieved_doc=[]
    chunks_data=chunks()
    for ind in indices[0]:
        if 0 <= int(ind) < len(chunks_data):
            rectrieved_doc.append(chunks_data[int(ind)].page_content)

    context = "\n".join(rectrieved_doc)
    return context

