SYSTEM_PROMPT = (
    "Answer the question using only the numbered context passages. "
    "Cite every claim with its passage number in square brackets, for example [1]. "
    "If the passages do not contain the answer, say you cannot answer."
)


def build_prompt(question: str, passages: list[str]) -> str:
    context = "\n\n".join(f"[{i}] {p}" for i, p in enumerate(passages, start=1))
    return f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
