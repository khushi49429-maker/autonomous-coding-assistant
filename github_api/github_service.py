import os
import httpx
from dotenv import load_dotenv

# Load environment variables
load_dotenv("backend/.env")

GITHUB_USERNAME = "khushi49429-maker"

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

async def get_repositories():
    """Fetch only the specified target repository formatted for app.py."""
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        
    if response.status_code == 200:
        repo_data = response.json()
        return repo_data  # Returns a list containing the repo dict
    else:
        return {
        "error": response.status_code,
        "message": response.text
    }







async def get_repository_files(owner: str, repo: str):

    url = f"https://api.github.com/repos/{owner}/{repo}/contents"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()

    return {
        "error": response.status_code,
        "message": response.text
    }
import base64


async def get_file_content(owner: str, repo: str, path: str):

    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
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
            file_content = base64.b64decode(
                data["content"]
            ).decode("utf-8")

            return file_content

    return {
        "error": response.status_code,
        "message": response.text
    }






