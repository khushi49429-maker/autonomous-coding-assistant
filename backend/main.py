import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai

# 1. FastAPI Initialize karein
app = FastAPI(title="autonomous-coding-assistant")

# 2. CORS Setup (Taaki frontend aur backend aapas mein communicate kar sakein)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Development ke liye allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Gemini API Configuration
# Note: Terminal mein pehle run karein: export GEMINI_API_KEY="your_actual_api_key"
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Data structure define karein jo frontend se aayega
class ChatQuery(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "CodeMentor AI Backend is running"}

# 4. Chat Endpoint (Yahan frontend se user ka message aayega)
@app.post("/api/chat")
async def chat_with_gemini(query: ChatQuery):
    try:
        # 3-second limit meet karne ke liye flash model best hai
        model = genai.GenerativeModel(
            model_name="gemini-2.0-flash-8b",
            system_instruction="You are CodeMentor AI, a helpful and expert programming assistant for students and beginners. Keep explanations crisp and provide correct code with syntax guidelines."
        )
        
        # Gemini ko request bhejein
        response = model.generate_content(query.message)
        
        return {"response": response.text}
        
    except Exception as e:
        return {"response": f"Sorry, backend pe kuch error aaya: {str(e)}"}