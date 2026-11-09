"""Chunking strategies. Start with fixed size, compare with sentence-aware."""
from src.schemas import Chunk


def fixed_chunks(
    text: str, source: str, size: int = 800, overlap: int = 120, page: int | None = None
) -> list[Chunk]:
    if overlap >= size:
        raise ValueError("overlap must be smaller than size")
    chunks: list[Chunk] = []
    step = size - overlap
    for i, start in enumerate(range(0, max(len(text), 1), step)):
        piece = text[start : start + size].strip()
        if piece:
            chunks.append(
                Chunk(chunk_id=f"{source}_{i:03d}", text=piece, source=source, page=page)
            )
    return chunks
