"""Index the corpus. TODO(ingestion owner)."""
from pathlib import Path

from src.ingestion.chunker import fixed_chunks
from src.ingestion.parser import load_text_file

RAW = Path("data/raw")

if __name__ == "__main__":
    total = 0
    for path in sorted(RAW.glob("*.txt")):
        total += len(fixed_chunks(load_text_file(path), source=path.name))
    print(f"Chunked {total} chunks. Index building is not implemented yet.")
