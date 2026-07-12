from pydantic import BaseModel


class PromptRequest(BaseModel):
    user_id: int
    prompt: str


class ExplainRequest(BaseModel):
    user_id: int
    code: str