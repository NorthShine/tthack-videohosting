import typing

import bcrypt

from src.models import User as UserModel, Video as VideoModel
import src.schemas
from src.config import get_config

salt = get_config()['base']['secret_key']


class BaseRepository:
    def __init__(self, db):
        self.db = db


class UserRepository(BaseRepository):
    async def get_user(self, user_id: int):
        return await self.db.fetch_one(
            UserModel.select().where(UserModel.c.id == user_id)
        )

    async def get_user_by_username(self, username: str):
        return await self.db.fetch_one(
            UserModel.select().where(UserModel.c.username == username)
        )

    async def verify_password(self, user_id: int, password: str):
        user = await self.get_user(user_id)
        return bcrypt.hashpw(password.encode('utf-8'), salt.encode('utf-8')) == user.hashed_password

    async def create_user(self, user: src.schemas.UserCreate):
        hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), salt.encode('utf-8'))
        query = UserModel.__table__.insert().values(
            username=user.username,
            hashed_password=str(hashed_password),
        )
        return await self.db.execute(query)


class VideoRepository(BaseRepository):
    async def get_video(self, video_id: int):
        return await self.db.fetch_one(
            VideoModel.select().where(VideoModel.c.id == video_id)
        )

    async def create_video(self, video: src.schemas.VideoCreate):
        query = VideoModel.insert().values(
            title=video.title,
            description=video.description,
            age_restrictions=video.age_restrictions,
        )
        return await self.db.execute(query)

    async def get_videos(self, q: typing.Optional[str] = None, limit: int = 10, page: int = 1):
        query = VideoModel.select()
        if q:
            query = query.filter(VideoModel.c.title.ilike(f'%{q}%'))
        if limit:
            query = query.limit(limit)
        if page:
            query = query.offset((page - 1) * limit)
        return await self.db.fetch_all(
            query.order_by(VideoModel.c.id.desc())
        )
