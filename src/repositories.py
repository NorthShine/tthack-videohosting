import typing

import bcrypt
from sqlalchemy.orm import Session

import src.models
import src.schemas
from src.config import get_config

salt = get_config()['base']['secret_key']


class BaseRepository:
    def __init__(self, db: Session):
        self.db = db


class UserRepository(BaseRepository):
    def get_user(self, user_id: int):
        return self.db.query(src.models.User).filter(src.models.User.id == user_id).first()

    def get_user_by_username(self, username: str):
        return self.db.query(src.models.User).filter(src.models.User.username == username).first()

    def create_user(self, user: src.schemas.UserCreate):
        hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), salt.encode('utf-8'))
        db_user = src.models.User(username=user.username, hashed_password=hashed_password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def verify_password(self, user: src.schemas.UserPassword, password: str):
        return bcrypt.hashpw(password.encode('utf-8'), salt) == user.password


class VideoRepository(BaseRepository):
    def get_video(self, video_id: int):
        return self.db.query(src.models.Video).filter(src.models.Video.id == video_id).first()

    def get_video_by_title(self, title: str):
        return self.db.query(src.models.Video).filter(src.models.Video.title == title).first()

    def create_video(self, video: src.schemas.VideoCreate):
        db_video = src.models.User(
            title=video.title,
            description=video.description,
            age_restrictions=video.age_restrictions,
        )
        self.db.add(db_video)
        self.db.commit()
        self.db.refresh(db_video)
        return db_video

    def get_videos(self, limit: int = 10, offset: int = 0, filters: typing.Optional[dict] = None):
        query = self.db.query(src.models.Video)
        if limit:
            query = query.limit(limit)
        if offset:
            query = query.offset(offset)
        if filters:
            query = query.filter_by(**filters)
        return query
