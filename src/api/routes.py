from fastapi import APIRouter

from src.api.deps import get_generator, get_retriever
from src.config import settings
from src.pipeline import ask
from src.schemas import AskRequest, AskResponse

router = APIRouter()


@router.post("/ask", response_model=AskResponse)
def ask_endpoint(req: AskRequest) -> AskResponse:
    return ask(
        req.question,
        get_retriever(),
        get_generator(),
        top_k=req.top_k,
        threshold=settings.refusal_threshold,
    )
