from pydantic import BaseModel
from backend.llm import review_code, fix_bug
from github_api.github_service import get_file_content


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
class GitHubReviewRequest(BaseModel):
    user_id: int
    owner: str
    repo: str
    path: str

@github_router.get("/repos/{user_id}")
async def fetch_repositories(user_id: int):

    return await get_repositories(user_id)


@github_router.get("/files/{user_id}/{owner}/{repo}")
async def fetch_repository_files(
    user_id: int,
    owner: str,
    repo: str
):

    return await get_repository_files(
        user_id,
        owner,
        repo
    )

@github_router.get("/file-content/{user_id}/{owner}/{repo}/{path:path}")
async def fetch_file_content_route(
    user_id: int,
    owner: str,
    repo: str,
    path: str
):

    return await get_file_content(
        user_id,
        owner,
        repo,
        path
    )

@github_router.post("/review-file")
async def review_file(request: GitHubReviewRequest):

    content = await get_file_content(
           request.user_id,
            request.owner,
            request.repo,
          request.path
    )

    if isinstance(content, dict):
        return content

    review = review_code(content)

    return {
        "file": request.path,
        "review": review
    }


# ==========================
# FIX FILE
# ==========================

@github_router.post("/fix-file")
async def fix_file(request: GitHubReviewRequest):

    content = await get_file_content(
         request.user_id,
         request.owner,
         request.repo,
         request.path
     )    

    if isinstance(content, dict):
        return content

    fixed = fix_bug(content)

    return {
        "file": request.path,
        "fixed_code": fixed
    }