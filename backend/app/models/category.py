from enum import Enum

from pydantic import AnyUrl, Field
from typing import List, Optional, Set
from typing_extensions import Literal

from bson.objectid import ObjectId
from .base import Base, ObjectID


class Category(Base):
    """Category definiton"""
    _id: Literal['anime', 'movies', 'music', 'shows', 'books']


class ItemBase(Base):
    """Base fields for any item"""
    id: ObjectID = Field(ObjectId(), alias="_id")
    flags: List[str] = list()
    hidden: bool = False
    title: str
    url: AnyUrl
    year_release: int
    genres: Set[str] = set()


class Show(ItemBase):
    """Shows category definition"""
    seasons: int
    episode_length: int
    season_length: int
    streaming: Optional[Literal['netflix', 'hotstar', 'torrent',
                                'prime', 'youtube', 'other']] = 'netflix'


class Anime(Show):
    """Anime category defintion"""
    # NOTE update if any other fields required
    pass


class Movie(ItemBase):
    """Movie category definition"""
    language: str
    director: str
    streaming: Optional[Literal['netflix', 'hotstar', 'torrent',
                                'prime', 'youtube', 'other']]


class Music(ItemBase):
    """Music category definiton"""
    artist: str
    album: Optional[str]
    streaming = Optional[Literal['youtube', 'spotify', 'gaana',
                                 'prime', 'apple', 'saavn']]


class Book(ItemBase):
    author: str
