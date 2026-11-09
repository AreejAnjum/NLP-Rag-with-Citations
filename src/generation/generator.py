"""Real generator. TODO(generation owner): call the LLM, parse [n] markers, validate citations."""
import re


def extract_citation_ids(answer: str) -> set[int]:
    return {int(n) for n in re.findall(r"\[(\d+)\]", answer)}


def citations_are_valid(answer: str, num_passages: int) -> bool:
    ids = extract_citation_ids(answer)
    return bool(ids) and all(1 <= i <= num_passages for i in ids)
