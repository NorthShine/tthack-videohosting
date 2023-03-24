from typing import Optional

from fastapi import APIRouter

from src.db import database
from src.repositories import VideoRepository

router = APIRouter(prefix='/videos')
video_repo = VideoRepository(database)


@router.get('/')
def get_videos(
    q: Optional[str] = None,
    limit: Optional[int] = 10,
    page: Optional[int] = 1,
):
    return video_repo.get_videos(q, limit, page)
