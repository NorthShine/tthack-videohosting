import databases
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

from src.config import get_config

DATABASE_URL = get_config()['postgresql']['url']
database = databases.Database(DATABASE_URL)
engine = sa.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata = sa.MetaData(bind=engine)
Base = declarative_base(metadata=metadata)
