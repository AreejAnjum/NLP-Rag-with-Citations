"""Build the retriever and generator. Replace the demo corpus with the real indexes."""
from functools import lru_cache

from src.generation.mock import MockGenerator
from src.retrieval.sparse_search import BM25Retriever
from src.schemas import Chunk


@lru_cache
def get_retriever():
    demo = [
        Chunk(chunk_id="demo_000", text="Refunds are possible within 14 days of purchase.", source="demo.txt"),
        Chunk(chunk_id="demo_001", text="Support is available on weekdays from 9 to 17.", source="demo.txt"),
        Chunk(chunk_id="demo_002", text="Shipping takes three to five working days inside Germany.", source="demo.txt"),
        Chunk(chunk_id="demo_003", text="Orders can be cancelled until they have been shipped.", source="demo.txt"),
        Chunk(chunk_id="demo_004", text="Payment is accepted by card, bank transfer and invoice.", source="demo.txt"),
    ]
    return BM25Retriever(demo)


@lru_cache
def get_generator():
    return MockGenerator()
