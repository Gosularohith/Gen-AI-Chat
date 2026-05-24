import faiss
import numpy as np
from openai import OpenAI

class VectorStore:
    def __init__(self):
        self.client = OpenAI(api_key="YOUR_API_KEY")
        self.index = faiss.IndexFlatL2(1536)  # embedding dimension
        self.docs = []

    def add_document(self, text: str):
        emb = self.client.embeddings.create(model="text-embedding-3-small", input=text).data[0].embedding
        self.index.add(np.array([emb], dtype="float32"))
        self.docs.append({"text": text})

    def search(self, query: str, top_k=3):
        emb = self.client.embeddings.create(model="text-embedding-3-small", input=query).data[0].embedding
        D, I = self.index.search(np.array([emb], dtype="float32"), top_k)
        return [self.docs[i] for i in I[0]]
