from backend.database.connection import SessionLocal
from backend.database.models import User

import os
from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
import requests
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()


GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")


# Step 1: Redirect user to GitHub login
@router.get("/github/login")
def github_login(user_id: int):

    github_url = (
        "https://github.com/login/oauth/authorize"
        f"?client_id={GITHUB_CLIENT_ID}"
        "&scope=repo"
        f"&state={user_id}"
    )

    return RedirectResponse(github_url)



# Step 2: GitHub sends code back
@router.get("/github/callback")
def github_callback(code: str, state: str = None):

    if state is None:
        raise HTTPException(
            status_code=400,
            detail="User state missing"
        )

    user_id = int(state)


    response = requests.post(
        "https://github.com/login/oauth/access_token",
        headers={
            "Accept": "application/json"
        },
        data={
            "client_id": GITHUB_CLIENT_ID,
            "client_secret": GITHUB_CLIENT_SECRET,
            "code": code
        }
    )


    data = response.json()


    if "access_token" not in data:
        raise HTTPException(
            status_code=400,
            detail="GitHub authentication failed"
        )


    token = data["access_token"]


    # Get GitHub user information
    github_user = requests.get(
        "https://api.github.com/user",
        headers={
            "Authorization": f"Bearer {token}"
        }
    ).json()


    github_username = github_user["login"]



    # Save token in database
    db = SessionLocal()

    try:

        user = db.query(User).filter(
            User.id == user_id
        ).first()


        if user:

            user.github_token = token
            user.github_username = github_username

            db.commit()


    finally:

        db.close()



    return RedirectResponse(
        url="http://127.0.0.1:5500/frontend/chat.html?github=connected"

)