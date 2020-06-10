from enum import IntEnum

from bson.objectid import ObjectId
from pydantic import Field

from .base import Base, ObjectID, RatingEnum


class Rating(Base):
    rating: float
    item_id: ObjectID
    username: str
