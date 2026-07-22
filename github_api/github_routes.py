from fastapi import APIRouter
from github_api.github_service import (
    get_repositories,
    get_repository_files,
    get_file_content
)

github_router = APIRouter(
    prefix="/github",
    tags=["GitHub"]
)


@github_router.get("/repos")
async def fetch_repositories():
    return await get_repositories()


@github_router.get("/files/{owner}/{repo}")
async def fetch_repository_files(owner: str, repo: str):
    return await get_repository_files(owner, repo)


@github_router.get("/file-content/{owner}/{repo}/{path:path}")
async def fetch_file_content_route(
    owner: str,
    repo: str,
    path: str
):
    return await get_file_content(
        owner,
        repo,
        path
    )