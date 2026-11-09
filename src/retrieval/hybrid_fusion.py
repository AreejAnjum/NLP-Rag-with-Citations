"""Reciprocal Rank Fusion."""
from src.schemas import ScoredChunk


def rrf(result_lists: list[list[ScoredChunk]], k: int = 60, top_k: int = 5) -> list[ScoredChunk]:
    fused: dict[str, float] = {}
    by_id = {}
    for results in result_lists:
        for rank, item in enumerate(results, start=1):
            cid = item.chunk.chunk_id
            by_id[cid] = item.chunk
            fused[cid] = fused.get(cid, 0.0) + 1.0 / (k + rank)
    ordered = sorted(fused.items(), key=lambda kv: kv[1], reverse=True)[:top_k]
    return [ScoredChunk(chunk=by_id[cid], score=score) for cid, score in ordered]
