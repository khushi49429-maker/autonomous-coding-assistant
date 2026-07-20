import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai


api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# FastAPI Initialize
app = FastAPI(title="autonomous-coding-assistant")

# -----------------------
# Signup and Login Models
# -----------------------

class SignupRequest(BaseModel):
    username: str
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


@app.post("/signup")
async def signup(user: SignupRequest):
    return {
        "message": "Signup successful"
    }


@app.post("/login")
async def login(user: LoginRequest):
    return {
        "message": "Login successful",
        "user_id": 1
    }


# -----------------------
# CORS Setup
# -----------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------
# Gemini API Configuration
# -----------------------

genai.configure(
    api_key=api_key
)

# -----------------------
# Chat Request Model
# -----------------------

class ChatQuery(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "status": "CodeMentor AI Backend is running"
    }


# -----------------------
# Chat Endpoint
# -----------------------

@app.post("/api/chat")
async def chat_with_gemini(query: ChatQuery):
    try:

        model = genai.GenerativeModel(
            "gemini-1.5-flash",
            system_instruction="""
            You are CodeMentor AI, a helpful and expert programming assistant
            for students and beginners. Keep explanations short and provide
            correct code examples with proper syntax.
            """
        )

        response = model.generate_content(
            query.message
        )

        return {
            "response": response.text
        }

    except Exception as e:
        return {
            "response": f"Sorry, backend pe kuch error aaya: {str(e)}"
        }