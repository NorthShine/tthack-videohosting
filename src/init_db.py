from src.repositories import UserRepository
from src.schemas import UserCreate
from src.db import SessionLocal
from src.config import get_config


def init_db():
    user_repo = UserRepository(SessionLocal())
    user = UserCreate(
        username='admin',
        password=get_config()['base']['admin_password'],
    )
    user_repo.create_user(user)


if __name__ == '__main__':
    init_db()
