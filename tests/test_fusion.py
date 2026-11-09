from src.retrieval.hybrid_fusion import rrf
from src.schemas import Chunk, ScoredChunk


def sc(cid, score=1.0):
    return ScoredChunk(chunk=Chunk(chunk_id=cid, text=cid, source="s"), score=score)


def test_rrf_prefers_chunks_ranked_by_both_lists():
    fused = rrf([[sc("a"), sc("b")], [sc("b"), sc("c")]], top_k=3)
    assert fused[0].chunk.chunk_id == "b"
