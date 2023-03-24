import asyncio

import bcrypt

from src.db import database
from src.config import get_config
from src.models import User

base_settings = get_config()['base']


async def init_db():
    await database.connect()
    salt = base_settings['secret_key']
    hashed_password = bcrypt.hashpw(base_settings['admin_password'].encode('utf-8'), salt.encode('utf-8'))
    query = User.__table__.insert().values(
        username='admin',
        hashed_password=str(hashed_password),
    )
    await database.execute(query)
    await database.disconnect()


if __name__ == '__main__':
    asyncio.run(init_db())
