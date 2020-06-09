from enum import IntEnum

from bson.objectid import ObjectId
from pydantic import Field

from .base import Base, ObjectID, RatingEnum


class Rating(Base):
    id: ObjectID = Field(None, alias="_id")
    rating: RatingEnum
    item_id: ObjectID
    user_id: ObjectID
