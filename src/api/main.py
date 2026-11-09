from fastapi import FastAPI

from src.api.routes import router

app = FastAPI(title="RAG with Citations", version="0.1.0")
app.include_router(router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
