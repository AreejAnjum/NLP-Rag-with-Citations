from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_answerable_question_returns_citation():
    body = client.post("/ask", json={"question": "refunds within days"}).json()
    assert body["refused"] is False
    assert body["citations"]


def test_unanswerable_question_is_refused():
    body = client.post("/ask", json={"question": "zebra quantum volcano"}).json()
    assert body["refused"] is True
    assert body["citations"] == []
