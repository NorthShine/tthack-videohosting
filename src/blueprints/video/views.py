from typing import Optional

from fastapi import APIRouter

from src.db import database
from src.repositories import VideoRepository
from src.schemas import VideoBase

router = APIRouter(prefix='/videos')
video_repo = VideoRepository(database)


@router.get('/')
async def get_videos(
    q: Optional[str] = None,
    limit: Optional[int] = 10,
    page: Optional[int] = 1,
):
    return await video_repo.get_videos(q, limit, page)


@router.get('/video/{pk}')
async def get_video(
    pk: int,
):
    return await video_repo.get_video(pk)


@router.put('/video/{pk}')
async def update_video(
    pk: int,
    video: VideoBase,
):
    return await video_repo.update_video(pk, video.dict())


@router.delete('/video/{pk}')
async def delete_video(
    pk: int,
):
    return await video_repo.delete_video(pk)
