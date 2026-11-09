from src.ingestion.chunker import fixed_chunks


def test_chunks_cover_text_with_overlap():
    chunks = fixed_chunks("a" * 2000, source="x", size=800, overlap=100)
    assert len(chunks) >= 3
    assert chunks[0].chunk_id == "x_000"
