# Team roles

| Role | Owner | Folders | Deliverables |
|---|---|---|---|
| Ingestion and storage | TBD | `src/ingestion/`, `data/`, `scripts/ingest.py` | Corpus choice and licence, parsing, chunking, vector index, BM25 index |
| Retrieval | TBD | `src/retrieval/` | Dense search, BM25 baseline, RRF fusion, retrieval metrics |
| Generation and safety | TBD | `src/generation/` | Prompts, citation formatting and validation, refusal logic |
| API and evaluation | TBD | `src/api/`, `src/evaluation/`, `scripts/evaluate.py`, Dockerfile | `POST /ask`, evaluation suite, unanswerable set, deployment |

## Interface agreements

- Retrieval returns `list[ScoredChunk]` and nothing else.
- Generation receives `ScoredChunk` items and returns an `AskResponse`.
- The API owner builds against the mock components in `src/generation/mock.py` until real ones land.
