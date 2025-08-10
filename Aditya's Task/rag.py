import os
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
import openai

class RAG:
    def __init__(self, persist_dir='./db'):
        self.persist = persist_dir
        use_openai = os.getenv("USE_OPENAI_EMBEDDINGS") == "1"

        if use_openai:
            self.model = None
        else:
            self.model = SentenceTransformer('all-MiniLM-L6-v2')

        # Use PersistentClient instead of Client for persistence
        self.client = chromadb.PersistentClient(
            path=self.persist
        )

        try:
            self.collection = self.client.get_collection('adgm')
        except Exception:
            self.collection = self.client.create_collection('adgm')

    def embed(self, text):
        if self.model:
            return self.model.encode(text).tolist()
        else:
            resp = openai.Embedding.create(
                model="text-embedding-3-small",
                input=text
            )
            return resp['data'][0]['embedding']

    def ingest_texts(self, docs):
        ids, texts, emb, metas = [], [], [], []
        for i, d in enumerate(docs):
            txt = d.get('text')
            ids.append(str(i))
            texts.append(txt)
            emb.append(self.embed(txt))
            metas.append({'source': d.get('source')})

        self.collection.add(
            ids=ids,
            metadatas=metas,
            documents=texts,
            embeddings=emb
        )

    def query(self, q, k=3):
        e = self.embed(q)
        results = self.collection.query(
            query_embeddings=[e],
            n_results=k
        )
        return [
            {'text': doc, 'source': meta.get('source')}
            for doc, meta in zip(results['documents'][0], results['metadatas'][0])
        ]
