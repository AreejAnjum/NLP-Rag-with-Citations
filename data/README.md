# Data

## Corpus

Describe the public corpus here: name, source URL, licence, number of documents, and how to download it. Prefer a download script over committing large files.

## Evaluation questions

- `eval/answerable.jsonl`: questions with the expected source chunk ids.
- `eval/unanswerable.jsonl`: questions the corpus cannot answer, used to measure the refusal rate.

Format of each line:

```json
{"id": "a001", "question": "...", "expected_chunk_ids": ["doc1_003"]}
```

Write at least 30 answerable and 15 unanswerable questions.
