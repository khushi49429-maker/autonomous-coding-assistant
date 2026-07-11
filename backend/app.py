from fastapi import FastAPI

app = FastAPI(
    title="Autonomous Coding Assistant",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Autonomous Coding Assistant API is Running!"
    }