from enum import IntEnum

from pydantic import SecretStr, Field
from typing import List, Dict

from bson.objectid import ObjectId

from .base import Base, ObjectID, LikeEnum


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
    ratings: List[UserRating] = list()
    likes: Dict[str, Dict[ObjectID, LikeEnum]] = dict()
