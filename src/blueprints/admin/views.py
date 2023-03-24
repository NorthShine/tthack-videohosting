from fastapi import APIRouter

from src.db import database
from src.repositories import UserRepository

router = APIRouter(prefix='/admin')
user_repo = UserRepository(database)


@router.get('/users/{user_id}')
def get_user(user_id: int):
    return user_repo.get_user(user_id)


@router.get('/users/{username}')
def get_user_by_username(username: str):
    return user_repo.get_user_by_username(username)
