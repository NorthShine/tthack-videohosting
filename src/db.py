import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import get_config

config_data = get_config()
login = config_data['postgresql']['login']
password = config_data['postgresql']['password']
url = config_data['postgresql']['url']
name = config_data['postgresql']['name']

DATABASE_URL = f'postgres://{login}:{password}@{url}/{name}'
engine = sa.create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
