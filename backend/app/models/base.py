from datetime import datetime, timezone
from enum import IntEnum, Enum

from pydantic import BaseConfig, BaseModel
from bson.objectid import ObjectId


class CategoryEnum(str, Enum):
    anime = 'anime'
    books = 'books'
    movies = 'movies'
    music = 'music'
    shows = 'shows'


class MusicEnum(str, Enum):
    youtube = 'youtube'
    spotify = 'spotify'
    gaana = 'gaana'
    prime = 'prime'
    apple = 'apple'
    saavn = 'saavn'


class VideoEnum(str, Enum):
    netflix = 'netflix'
    hotstar = 'hotstar'
    torrent = 'torrent'
    prime = 'prime'
    youtube = 'youtube'
    other = 'other'


class LikeEnum(IntEnum):
    """Like options"""
    dislike = -1
    like = 1


class RatingEnum(IntEnum):
    """Rating options"""
    very_horrible = 1
    horrible = 2
    very_bad = 3
    bad = 4
    neutral = 5
    decent = 6
    good = 7
    very_good = 8
    excellent = 9
    amazing = 10


class ObjectID(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(str(v)):
            return ValueError(f"Not a valid ObjectId: {v}")
        return ObjectId(str(v))


class Base(BaseModel):
    class Config(BaseConfig):
        allow_population_by_alias = True
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda dt: dt.replace(tzinfo=timezone.utc)
            .isoformat()
            .replace("+00:00", "Z"),
            ObjectId: ObjectID,

        }
