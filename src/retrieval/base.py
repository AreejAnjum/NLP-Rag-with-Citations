from typing import Protocol

from src.schemas import ScoredChunk


class Retriever(Protocol):
    def search(self, query: str, top_k: int = 5) -> list[ScoredChunk]: ...
