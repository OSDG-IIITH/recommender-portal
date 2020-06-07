from typing import Dict, List, Union

from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient

from ..models.base import ObjectID
from ..models.category import Anime, Category, Movie, Music, Show, Book
from ..models.responses import (CategorysInResponse, ItemInResponse,
                                ItemsInResponse, ResponseBase)
from ..utils.mongodb import get_database
from ..utils.token import verify_token
from ..models.base import CategoryEnum

router = APIRouter()


@router.get("/{category_id}", response_model=ItemsInResponse, tags=["fetch"])
async def get_category_route(category_id: str,
                             db: AsyncIOMotorClient = Depends(get_database)) -> ItemsInResponse:
    """Get the items under a given category"""
        
    loader = None
    if category_id == CategoryEnum.movies.value:
        loader = Movie
    if category_id == CategoryEnum.anime.value:
        loader = Anime
    if category_id == CategoryEnum.music.value:
        loader = Music
    if category_id == CategoryEnum.shows.value:
        loader = Show
    if category_id == CategoryEnum.books.value:
        loader = Book
    if category_id in CategoryEnum.__members__:
        items = [loader(**item) async for item in db[category_id]["data"].find()]
        return ItemsInResponse(data=items)
    else:
        return ItemsInResponse(success=False, error=[f"Invalid category {category_id}"])

@router.get("/{category_id}/{item_id}", response_model=ItemInResponse, tags=["fetch", "item"])
async def get_category_item_route(category_id: str, item_id: ObjectID,
                                  db: AsyncIOMotorClient = Depends(get_database)) -> ItemInResponse:
    """Get the details about a particular item"""
    # TODO: add particular item fetching
    return {"success": True}


@router.post("/{category_id}", response_model=ItemInResponse, dependencies=[Depends(verify_token)], tags=["add"])
async def add_item_route(category_id: str, item: Union[Movie, Anime, Show, Music],
                         db: AsyncIOMotorClient = Depends(get_database)) -> ItemInResponse:
    """Add item to a given category"""
    # TODO add item to db
    return {"success": True}


@router.patch("/{category_id}/{item_id}", response_model=ItemInResponse, dependencies=[Depends(verify_token)], tags=["update"])
async def update_item_route(category_id: str, item_id: ObjectID,
                            db: AsyncIOMotorClient = Depends(get_database)) -> ItemInResponse:
    """Update a given item"""
    # TODO add update route
    return {"success": True}


@router.post("/{category_id}/rate/{item_id}", response_model=ResponseBase, tags=["user", "rate"])
async def rate_item_route(category_id: str, item_id: ObjectID, rating: float,
                          token: dict = Depends(verify_token),
                          db: AsyncIOMotorClient = Depends(get_database)) -> ResponseBase:
    """"Rate a given item"""
    # TODO add rating functionality here
    return {"success": True}
