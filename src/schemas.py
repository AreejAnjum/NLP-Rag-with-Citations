"""Shared data contract between ingestion, retrieval, generation and the API."""
from typing import Optional

from pydantic import BaseModel, Field


class Chunk(BaseModel):
    chunk_id: str
    text: str
    source: str
    page: Optional[int] = None


class ScoredChunk(BaseModel):
    chunk: Chunk
    score: float


class Citation(BaseModel):
    id: int = Field(description="Number used in the answer, e.g. [1]")
    chunk_id: str
    source: str
    page: Optional[int] = None
    snippet: str


class AskRequest(BaseModel):
    question: str = Field(min_length=1)
    top_k: int = Field(default=5, ge=1, le=20)


class AskResponse(BaseModel):
    answer: str
    citations: list[Citation]
    refused: bool
    confidence: float
