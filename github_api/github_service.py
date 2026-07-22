import httpx
import base64

from backend.database.connection import SessionLocal
from backend.database.models import User


async def get_user_github_token(user_id: int):

    db = SessionLocal()

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    db.close()

    if user and user.github_token:
        return user.github_token

    return None



async def get_repositories(user_id: int):

    token = await get_user_github_token(user_id)

    if not token:
        return {
            "error": "GitHub not connected"
        }


    url = "https://api.github.com/user/repos"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }


    async with httpx.AsyncClient() as client:

        response = await client.get(
            url,
            headers=headers
        )


    if response.status_code == 200:
        return response.json()


    return {
        "error": response.status_code,
        "message": response.text
    }



async def get_repository_files(
        user_id: int,
        owner: str,
        repo: str
):

    token = await get_user_github_token(user_id)


    url = f"https://api.github.com/repos/{owner}/{repo}/contents"


    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }


    async with httpx.AsyncClient() as client:

        response = await client.get(
            url,
            headers=headers
        )


    if response.status_code == 200:
        return response.json()


    return {
        "error": response.status_code,
        "message": response.text
    }



async def get_file_content(
        user_id: int,
        owner: str,
        repo: str,
        path: str
):

    token = await get_user_github_token(user_id)


    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"


    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }


    async with httpx.AsyncClient() as client:

        response = await client.get(
            url,
            headers=headers
        )


    if response.status_code == 200:

        data = response.json()

        if "content" in data:

            return base64.b64decode(
                data["content"]
            ).decode("utf-8")


    return {
        "error": response.status_code,
        "message": response.text
    }