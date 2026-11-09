# RAG with Citations

A retrieval-augmented question answering service that answers only from a public corpus, cites the passages it used, and refuses when nothing relevant is found. Includes a BM25 baseline and an evaluation suite with an unanswerable-question test and refusal rate.

**Live service:** _add URL here once deployed_
**Corpus:** _see [data/README.md](data/README.md)_

## Features

- Document parsing and chunking (fixed-size and sentence-aware strategies)
- Dense retrieval (vector store) and BM25 sparse baseline
- Optional hybrid fusion with Reciprocal Rank Fusion (RRF)
- Citation-grounded generation: every claim points to a retrieved chunk
- Refusal when retrieval confidence is below a threshold
- Evaluation: recall@k, MRR, citation correctness, refusal rate on unanswerable questions

## Quickstart

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env              # add your keys
uvicorn src.api.main:app --reload
```

Or with Docker:

```bash
docker build -t rag-citations .
docker run -p 8000:8000 --env-file .env rag-citations
```

## API

`POST /ask`

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the refund policy?", "top_k": 5}'
```

```json
{
  "answer": "Refunds are possible within 14 days [1].",
  "citations": [
    {"id": 1, "chunk_id": "doc1_003", "source": "policy.pdf", "page": 2, "snippet": "..."}
  ],
  "refused": false,
  "confidence": 0.82
}
```

When nothing relevant is found, `refused` is `true`, `answer` explains that the corpus has no answer, and `citations` is empty.

`GET /health` returns `{"status": "ok"}`.

## Architecture

```
question -> retrieval (BM25 | dense | hybrid) -> refusal check -> generation with citations -> response
                    ^
        ingestion: parse -> chunk -> embed -> index
```

See [docs/architecture.md](docs/architecture.md) for details and [docs/roles.md](docs/roles.md) for team ownership.

## Evaluation

```bash
python scripts/ingest.py
python scripts/evaluate.py --retriever bm25
python scripts/evaluate.py --retriever dense
python scripts/evaluate.py --retriever hybrid
```

Results are written to `results/`. Summary table:

| Retriever | recall@5 | MRR | citation correctness | refusal rate (unanswerable) |
|---|---|---|---|---|
| BM25 | TBD | TBD | TBD | TBD |
| Dense | TBD | TBD | TBD | TBD |
| Hybrid | TBD | TBD | TBD | TBD |

## Repository layout

```
data/          corpus description, raw files or download script, evaluation questions
src/           application code (ingestion, retrieval, generation, evaluation, api)
scripts/       thin command line entry points
tests/         unit and API tests
docs/          architecture and team roles
results/       committed evaluation outputs
```

## Contributing

Work on a feature branch, open a pull request, and request a review from the code owner of the folder (see `.github/CODEOWNERS`). CI runs the tests on every push.

## License

MIT, see [LICENSE](LICENSE).
