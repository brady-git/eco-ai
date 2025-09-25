from pydantic import BaseModel, Field

class AskRequest(BaseModel):
    question: str = Field(..., min_length=1)
    metadata: dict | None = None

class AskResponse(BaseModel):
    answer: str
    metadata: dict | None = None
