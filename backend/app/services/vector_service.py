import chromadb

from sentence_transformers import SentenceTransformer


class VectorService:

    def __init__(self):

        self.client = chromadb.PersistentClient(path="./chroma_db")

        self.collection = self.client.get_or_create_collection(
            name="interview_questions"
        )

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def add_question(self, question_id, question_text, metadata):

        embedding = self.model.encode(question_text).tolist()

        self.collection.add(
            ids=[str(question_id)],
            documents=[question_text],
            embeddings=[embedding],
            metadatas=[metadata],
        )

    def search_questions(self, query, limit=5):

        query_embedding = self.model.encode(query).tolist()

        results = self.collection.query(
            query_embeddings=[query_embedding], n_results=limit
        )

        return results

    def search_by_skill(self, skill, limit=5):

        results = self.search_questions(query=skill, limit=limit)

        return results
