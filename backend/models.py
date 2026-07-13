from pydantic import BaseModel


class PromptRequest(BaseModel):
    prompt: str
    user_id: int


class ExplainRequest(BaseModel):
    code: str
    user_id: int


class ChatRequest(BaseModel):
    message: str
    user_id: int