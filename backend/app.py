from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session

from models import PromptRequest, ExplainRequest, ChatRequest
from llm import generate_code, explain_code, review_code, fix_bug

from database.connection import SessionLocal
from database.models import User, ChatHistory
from auth import hash_password, verify_password


app = FastAPI(
    title="Autonomous Coding Assistant",
    version="1.0.0"
)


# ============================
# CORS
# ============================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# ============================
# AUTH MODELS
# ============================

class SignupRequest(BaseModel):
    username: str
    email: str
    password: str



class LoginRequest(BaseModel):
    email: str
    password: str




# ============================
# SAVE CHAT
# ============================

def save_chat(user_id, prompt, response):

    db: Session = SessionLocal()

    chat = ChatHistory(
        user_id=user_id,
        prompt=prompt,
        response=response
    )

    db.add(chat)
    db.commit()
    db.close()




# ============================
# BASIC ROUTES
# ============================

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




# ============================
# CODE GENERATION
# ============================

@app.post("/generate-code")
def generate(request: PromptRequest):

    result = generate_code(request.prompt)

    save_chat(
        request.user_id,
        request.prompt,
        result
    )

    return {
        "generated_code": result
    }




# ============================
# EXPLAIN CODE
# ============================

@app.post("/explain-code")
def explain(request: ExplainRequest):

    result = explain_code(request.code)

    save_chat(
        request.user_id,
        request.code,
        result
    )

    return {
        "explanation": result
    }




# ============================
# REVIEW CODE
# ============================

@app.post("/review-code")
def review(request: ExplainRequest):

    result = review_code(request.code)

    save_chat(
        request.user_id,
        request.code,
        result
    )

    return {
        "review": result
    }




# ============================
# FIX BUG
# ============================

@app.post("/fix-bug")
def fix(request: ExplainRequest):

    result = fix_bug(request.code)

    save_chat(
        request.user_id,
        request.code,
        result
    )

    return {
        "fixed_code": result
    }




# ============================
# MAIN CHAT API
# ============================

@app.post("/api/chat")
def chat(request: ChatRequest):

    message = request.message.strip()
    lower_message = message.lower()



    # Greeting detection
    if (
        lower_message.startswith("hi")
        or lower_message.startswith("hello")
        or lower_message.startswith("hey")
        or lower_message.startswith("good morning")
        or lower_message.startswith("good afternoon")
        or lower_message.startswith("good evening")
    ):


        result = (
            "Hello! 👋 I'm CodeMentor AI.\n\n"
            "I can help you with:\n"
            "• Writing code\n"
            "• Explaining programming concepts\n"
            "• Reviewing code\n"
            "• Fixing bugs\n\n"
            "Ask me anything about programming!"
        )


    # Explain
    elif "explain" in lower_message:

        result = explain_code(message)



    # Review
    elif "review" in lower_message:

        result = review_code(message)



    # Fix bugs
    elif "fix" in lower_message or "bug" in lower_message:

        result = fix_bug(message)



    # Generate code
    else:

        result = generate_code(message)




    save_chat(
        request.user_id,
        message,
        result
    )



    return {
        "response": result
    }




# ============================
# SIGNUP
# ============================

@app.post("/signup")
def signup(request: SignupRequest):

    db: Session = SessionLocal()


    existing_user = db.query(User).filter(
        User.email == request.email
    ).first()



    if existing_user:

        db.close()

        return {
            "message": "Email already registered"
        }



    hashed_password = hash_password(
        request.password
    )


    new_user = User(
        username=request.username,
        email=request.email,
        password=hashed_password
    )


    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    db.close()



    return {
        "message": "User created successfully",
        "user_id": new_user.id
    }




# ============================
# LOGIN
# ============================

@app.post("/login")
def login(request: LoginRequest):

    db: Session = SessionLocal()


    user = db.query(User).filter(
        User.email == request.email
    ).first()



    if not user:

        db.close()

        return {
            "message": "User not found"
        }




    if not verify_password(
        request.password,
        user.password
    ):

        db.close()

        return {
            "message": "Invalid password"
        }




    db.close()



    return {
        "message": "Login successful",
        "user_id": user.id
    }




# ============================
# CHAT HISTORY
# ============================

@app.get("/chat-history/{user_id}")
def get_chat_history(user_id: int):

    db: Session = SessionLocal()


    chats = db.query(ChatHistory).filter(
        ChatHistory.user_id == user_id
    ).all()



    result = []



    for chat in chats:

        result.append({
            "id": chat.id,
            "prompt": chat.prompt,
            "response": chat.response,
            "created_at": chat.created_at
        })



    db.close()



    return result