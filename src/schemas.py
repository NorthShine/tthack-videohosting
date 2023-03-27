import typing

from pydantic import BaseModel

from src.config import get_config


class Settings(BaseModel):
    authjwt_secret_key: str = get_config()['base']['secret_key']


class UserBase(BaseModel):
    username: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class UserPassword(BaseModel):
    password: str


class VideoBase(BaseModel):
    title: typing.Optional[str]
    description: typing.Optional[str]
    age_restrictions: typing.Optional[int]


class Video(VideoBase):
    id: int

    class Config:
        orm_mode = True


class VideoCreate(VideoBase):
    pass
