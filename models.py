from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt: str

class ExplainRequest(BaseModel):
    code: str