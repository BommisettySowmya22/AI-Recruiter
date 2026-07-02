import faiss
import numpy as np

def build_index(embeddings):

    embeddings = np.array(embeddings).astype("float32")

    index = faiss.IndexFlatIP(embeddings.shape[1])

    index.add(embeddings)

    return index


def search(index, query_embedding, k=1000):

    scores, ids = index.search(
        np.array([query_embedding]).astype("float32"),
        k
    )

    return scores[0], ids[0]