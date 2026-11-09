from src.generation.refusal import should_refuse
from src.schemas import Chunk, ScoredChunk


def sc(score):
    return ScoredChunk(chunk=Chunk(chunk_id="a", text="t", source="s"), score=score)


def test_refuses_on_empty_and_low_scores():
    assert should_refuse([], 0.3)
    assert should_refuse([sc(0.1)], 0.3)
    assert not should_refuse([sc(0.9)], 0.3)
