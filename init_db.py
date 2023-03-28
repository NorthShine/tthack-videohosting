import asyncio

from src.db import database
from src.config import get_config
from src.models import User

base_settings = get_config()['base']


async def init_db():
    await database.connect()
    query = User.__table__.insert().values(
        username='admin',
        hashed_password=base_settings['admin_password'],
    )
    await database.execute(query)
    await database.disconnect()


if __name__ == '__main__':
    asyncio.run(init_db())
