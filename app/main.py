from fastapi import FastAPI
from .settings import settings
from .models import AskRequest, AskResponse
from .rag import answer_question

app = FastAPI(title="eco-ai", version="0.1.0")

@app.get("/healthz")
def healthz():
    return {"status": "ok", "env": settings.APP_ENV}

@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    answer, meta = answer_question(req.question, req.metadata or {})
    return AskResponse(answer=answer, metadata=meta)
