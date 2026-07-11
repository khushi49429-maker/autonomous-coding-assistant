from fastapi import FastAPI
from models import PromptRequest, ExplainRequest
from services import generate_code, explain_code

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "CodeMentor AI Backend Running"
    }

@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }

@app.post("/generate-code")
def generate(request: PromptRequest):
    result = generate_code(request.prompt)
    return {
        "generated_code": result
    }

@app.post("/explain-code")
def explain(request: ExplainRequest):
    result = explain_code(request.code)
    return {
        "explanation": result
    }