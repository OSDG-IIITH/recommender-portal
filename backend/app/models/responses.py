from typing import List, Optional, Union

from .base import Base, ObjectID
from .category import Anime, Movie, Music, Show, Book
from .user import User, Like


class ResponseBase(Base):
    """Base return response"""
    success: bool = True
    error: Optional[List] = None


class ItemInResponse(ResponseBase):
    """Wrapper for category items"""
    data: Union[Anime, Movie, Music, Show, Book]


class ItemsInResponse(ResponseBase):
    """Wrapper for list of items"""
    data: List[Union[Anime, Movie, Music, Show, Book]] = list()

class UserInResponse(ResponseBase):
    data: User


class UsersInResponse(ResponseBase):
    data: List[UserInResponse] = list()


class LikeInResponse(ResponseBase):
    data: Like