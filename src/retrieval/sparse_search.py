"""BM25 baseline."""
import re

from rank_bm25 import BM25Okapi

from src.schemas import Chunk, ScoredChunk


def _tokenize(text: str) -> list[str]:
    return re.findall(r"\w+", text.lower())


class BM25Retriever:
    def __init__(self, chunks: list[Chunk]):
        self.chunks = chunks
        self.index = BM25Okapi([_tokenize(c.text) for c in chunks])

    def search(self, query: str, top_k: int = 5) -> list[ScoredChunk]:
        scores = self.index.get_scores(_tokenize(query))
        ranked = sorted(range(len(self.chunks)), key=lambda i: scores[i], reverse=True)
        top = ranked[:top_k]
        best = max((scores[i] for i in top), default=0.0) or 1.0
        return [ScoredChunk(chunk=self.chunks[i], score=float(scores[i] / best)) for i in top]
