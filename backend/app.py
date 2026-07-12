from fastapi import FastAPI
from models import PromptRequest, ExplainRequest
from llm import generate_code, explain_code, review_code, fix_bug

app = FastAPI(
    title="Autonomous Coding Assistant",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Autonomous Coding Assistant API is Running!"
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


@app.post("/review-code")
def review(request: ExplainRequest):
    result = review_code(request.code)
    return {
        "review": result
    }


@app.post("/fix-bug")
def fix(request: ExplainRequest):
    result = fix_bug(request.code)
    return {
        "fixed_code": result
    }