"""Evaluation metrics."""


def recall_at_k(retrieved_ids: list[str], expected_ids: list[str], k: int) -> float:
    if not expected_ids:
        return 0.0
    hits = len(set(retrieved_ids[:k]) & set(expected_ids))
    return hits / len(expected_ids)


def reciprocal_rank(retrieved_ids: list[str], expected_ids: list[str]) -> float:
    for rank, cid in enumerate(retrieved_ids, start=1):
        if cid in expected_ids:
            return 1.0 / rank
    return 0.0


def refusal_rate(refused_flags: list[bool]) -> float:
    return sum(refused_flags) / len(refused_flags) if refused_flags else 0.0
