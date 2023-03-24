import sqlalchemy as sa

from src.db import Base


class User(Base):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    username = sa.Column(sa.String, unique=True, index=True)
    hashed_password = sa.Column(sa.String)


class Video(Base):
    __tablename__ = "videos"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    title = sa.Column(sa.String)
    description = sa.Column(sa.String)
    age_restrictions = sa.Column(sa.Integer, default=0)
    url = sa.Column(sa.String)
