from typing import Optional

import aiofiles
from fastapi import APIRouter, UploadFile

from src.db import database
from src.repositories import VideoRepository
from src.schemas import VideoBase, VideoCreate
from src.config import get_config

router = APIRouter(prefix='/videos')
video_repo = VideoRepository(database)
media_directory = get_config()['base']['media_directory']


@router.get('/')
async def get_videos(
    q: Optional[str] = None,
    limit: Optional[int] = 10,
    page: Optional[int] = 1,
):
    return await video_repo.get_videos(q, limit, page)


@router.post('/create')
async def create_video(video: VideoCreate):
    return await video_repo.create_video(video)


@router.post('/upload')
async def upload_video(video: UploadFile):
    async with aiofiles.open(f'{media_directory}/{video.filename}', 'wb') as file:
        await file.write(await video.read())


@router.get('/{pk}')
async def get_video(pk: int):
    return await video_repo.get_video(pk)


@router.put('/{pk}')
async def update_video(
    pk: int,
    video: VideoBase,
):
    return await video_repo.update_video(pk, video.dict())


@router.delete('/{pk}')
async def delete_video(pk: int):
    return await video_repo.delete_video(pk)
