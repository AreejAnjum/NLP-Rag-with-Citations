# Architecture

## Pipeline

1. **Ingestion** parses raw documents, splits them into chunks with metadata (source, page, chunk id), embeds them, and builds a vector index and a BM25 index.
2. **Retrieval** returns the top-k chunks using BM25, dense search, or hybrid fusion (RRF). An optional cross-encoder reranker can be added later.
3. **Refusal check** compares the best retrieval score to a threshold. Below the threshold, the service refuses and returns no citations.
4. **Generation** prompts the LLM with the question and numbered chunks, and requires citations in the form `[n]`. Citations that do not map to a retrieved chunk are rejected.
5. **API** exposes `POST /ask` and `GET /health`.

## Shared contract

All modules exchange the models in `src/schemas.py` (`Chunk`, `ScoredChunk`, `Citation`, `AskRequest`, `AskResponse`). Change these only through a pull request that every owner reviews.

## Design decisions

Record decisions here with date and reason, for example the chosen chunk size, embedding model, and refusal threshold.
