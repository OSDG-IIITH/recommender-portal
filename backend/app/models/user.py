from enum import IntEnum

from pydantic import SecretStr, Field
from typing import List

from bson.objectid import ObjectId

from .base import Base, ObjectID, LikeEnum


class UserRating(Base):
    rating_id: ObjectID
    rating: float


class Like(Base):
    category_id: ObjectID
    item_id: ObjectID
    value: LikeEnum


class User(Base):
    id: ObjectID = Field(ObjectId(), alias="_id")
    username: str
    password: SecretStr
    ratings: List[UserRating] = list()
    likes: List[Like] = list()
