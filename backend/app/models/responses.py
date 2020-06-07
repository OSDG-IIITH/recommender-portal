from typing import List, Optional, Union, Dict

from .base import Base, ObjectID
from .category import Anime, Movie, Music, Show, Book, Category
from .user import User, Like


class ResponseBase(Base):
    """Base return response"""
    success: bool = True
    error: Optional[List]
    data: Optional[Union[List, Dict[str, str]]]


class ItemInResponse(ResponseBase):
    """Wrapper for category items"""
    data: Union[Anime, Movie, Music, Show, Book]


class ItemsInResponse(ResponseBase):
    """Wrapper for list of items"""
    data: List[Union[Anime, Movie, Music, Show, Book]] = list()


class UserInResponse(ResponseBase):
    data: User


class UsersInResponse(ResponseBase):
    data: List[User] = list()


class LikeInResponse(ResponseBase):
    """Response wrapper for like object"""
    data: Like
    category_id: str
    item_id: ObjectID


class CategorysInResponse(ResponseBase):
    data: List[Category]
