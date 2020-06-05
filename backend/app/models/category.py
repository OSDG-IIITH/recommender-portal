from enum import Enum

from pydantic import AnyUrl, Field
from typing import List, Optional, Set

from bson.objectid import ObjectId
from .base import Base, ObjectID, MusicEnum, VideoEnum, CategoryEnum


class Category(Base):
    """Category definiton"""
    _id: CategoryEnum


class ItemBase(Base):
    """Base fields for any item"""
    id: ObjectID = Field(None, alias="_id")
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
    streaming: Optional[VideoEnum]


class Anime(Show):
    """Anime category defintion"""
    # NOTE update if any other fields required
    pass


class Movie(ItemBase):
    """Movie category definition"""
    language: str
    director: str
    streaming: Optional[VideoEnum]


class Music(ItemBase):
    """Music category definiton"""
    artist: str
    album: Optional[str]
    streaming: Optional[MusicEnum]


class Book(ItemBase):
    author: str
