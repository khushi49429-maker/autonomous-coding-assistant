from pydantic import BaseModel
from backend.database import Base  # or from .database import Base


class PromptRequest(BaseModel):
    prompt: str
    user_id: int


class ExplainRequest(BaseModel):
    code: str
    user_id: int


class ChatRequest(BaseModel):
    message: str
    user_id: int