"""Run the evaluation. TODO(evaluation owner): plug in the real retrievers and the live API."""
import argparse
import json
from pathlib import Path

from src.evaluation.metrics import refusal_rate


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--retriever", default="bm25", choices=["bm25", "dense", "hybrid"])
    args = parser.parse_args()
    unanswerable = read_jsonl(Path("data/eval/unanswerable.jsonl"))
    print(f"retriever={args.retriever} unanswerable_questions={len(unanswerable)}")
    print("Wire the pipeline in, then report refusal_rate on this set:", refusal_rate([]))
