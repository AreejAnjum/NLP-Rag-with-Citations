"""Dense vector search. TODO(retrieval owner): query the vector store."""


class DenseRetriever:
    def search(self, query: str, top_k: int = 5):
        raise NotImplementedError
