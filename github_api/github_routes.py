from fastapi import APIRouter
from github_api.github_service import get_repositories

github_router = APIRouter(prefix="/github", tags=["GitHub"])

@github_router.get("/repos")
async def fetch_repositories():
    return await get_repositories()