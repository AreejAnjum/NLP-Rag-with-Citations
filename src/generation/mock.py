"""Mock generator so the API and evaluation can be built before the LLM is wired in."""
from src.schemas import Citation, ScoredChunk


class MockGenerator:
    def answer(self, question: str, results: list[ScoredChunk]) -> tuple[str, list[Citation]]:
        top = results[0].chunk
        citation = Citation(
            id=1,
            chunk_id=top.chunk_id,
            source=top.source,
            page=top.page,
            snippet=top.text[:200],
        )
        return f"{top.text[:160]} [1]", [citation]
