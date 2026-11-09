"""Glue: retrieve, refuse if weak, otherwise generate with citations."""
from src.generation.refusal import REFUSAL_MESSAGE, should_refuse
from src.schemas import AskResponse


def ask(question: str, retriever, generator, top_k: int, threshold: float) -> AskResponse:
    results = retriever.search(question, top_k=top_k)
    confidence = max((r.score for r in results), default=0.0)
    if should_refuse(results, threshold):
        return AskResponse(answer=REFUSAL_MESSAGE, citations=[], refused=True, confidence=confidence)
    answer, citations = generator.answer(question, results)
    return AskResponse(answer=answer, citations=citations, refused=False, confidence=confidence)
