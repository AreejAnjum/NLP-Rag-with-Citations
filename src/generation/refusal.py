"""Decide whether retrieval is good enough to answer."""
from src.schemas import ScoredChunk


def should_refuse(results: list[ScoredChunk], threshold: float) -> bool:
    if not results:
        return True
    return max(r.score for r in results) < threshold


REFUSAL_MESSAGE = "I could not find an answer to this question in the provided documents."
