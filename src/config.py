"""Central settings read from environment variables."""
import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    retriever: str = os.getenv("RETRIEVER", "hybrid")
    top_k: int = int(os.getenv("TOP_K", "5"))
    refusal_threshold: float = float(os.getenv("REFUSAL_THRESHOLD", "0.25"))
    llm_provider: str = os.getenv("LLM_PROVIDER", "openai")
    llm_model: str = os.getenv("LLM_MODEL", "")
    embedding_model: str = os.getenv(
        "EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2"
    )


settings = Settings()
