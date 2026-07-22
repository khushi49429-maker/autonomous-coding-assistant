import os
import httpx
from dotenv import load_dotenv

# Load environment variables
load_dotenv("backend/.env")

GITHUB_USERNAME = "khushi49429-maker"
TARGET_REPO = "autonomous-coding-assistant"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

async def get_repositories():
    """Fetch only the specified target repository formatted for app.py."""
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{TARGET_REPO}"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        
    if response.status_code == 200:
        repo_data = response.json()
        return [repo_data]  # Returns a list containing the repo dict
    else:
        # Fallback dictionary if API response fails
        return [{"name": TARGET_REPO}]