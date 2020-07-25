from enum import Enum
from typing import List, Optional

from pydantic import AnyUrl, Field

from .base import Base, ObjectID, MusicEnum, VideoEnum, CategoryEnum


class Category(Base):
    """Category definiton"""
    id: CategoryEnum = Field(None, alias="_id")


class ItemBase(Base):
    """Base fields for any item"""
    id: ObjectID = Field(None, alias="_id")
    flags: List[str] = list()
    hidden: bool = False
    title: str
    link: AnyUrl
    year_release: int
    genres: List[str] = list()


class Show(ItemBase):
    """Shows category definition"""
    seasons: Optional[int]
    episode_length: Optional[int]
    season_length: Optional[int]
    streaming: Optional[List[VideoEnum]]


class Anime(Show):
    """Anime category defintion"""
    # NOTE update if any other fields required
    pass


class Movie(ItemBase):
    """Movie category definition"""
    language: Optional[str]
    director: Optional[str]
    streaming: Optional[List[VideoEnum]]


class Music(ItemBase):
    """Music category definiton"""
    artist: Optional[str]
    album: Optional[str]
    streaming: Optional[List[MusicEnum]]


class Book(ItemBase):
    author: Optional[str]
