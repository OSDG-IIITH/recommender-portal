from typing import Dict

from pydantic import Field

from .base import Base, ObjectID, LikeEnum, CategoryEnum


class UserRating(Base):
    rating_id: ObjectID
    rating: float


class Like(Base):
    value: LikeEnum


class User(Base):
    id: ObjectID = Field(None, alias="_id")
    username: str
    first_login: str
    last_login: str
    ratings: Dict[str, Dict[ObjectID, UserRating]] = dict()
    likes: Dict[str, Dict[ObjectID, LikeEnum]] = dict()
