"""Load raw files (PDF, Markdown, TXT) and return plain text with metadata."""
from pathlib import Path


def load_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


# TODO(ingestion owner): add PDF parsing and page tracking.
