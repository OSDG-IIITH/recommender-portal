from typing import Dict, List, Union

from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient

from ..models.base import ObjectID, CategoryEnum
from ..models.category import Anime, Category, Movie, Music, Show, Book
from ..models.responses import (CategorysInResponse, ItemInResponse,
                                ItemsInResponse, ResponseBase)
from ..utils.mongodb import get_database
from ..utils.token import verify_token
from ..models.base import CategoryEnum

router = APIRouter()


@router.get("/{category_id}", response_model=ItemsInResponse, tags=["fetch"])
async def get_category_route(category_id: CategoryEnum,
                             db: AsyncIOMotorClient = Depends(get_database)) -> ItemsInResponse:
    """Get the items under a given category"""

    loader = None
    if category_id == CategoryEnum.movies:
        loader = Movie
    elif category_id == CategoryEnum.anime:
        loader = Anime
    elif category_id == CategoryEnum.music:
        loader = Music
    elif category_id == CategoryEnum.shows:
        loader = Show
    elif category_id == CategoryEnum.books:
        loader = Book
    items = [loader(**item) async for item in db[category_id]["data"].find()]
    return ItemsInResponse(data=items)


@router.get("/{category_id}/{item_id}", response_model=ItemInResponse, tags=["fetch", "item"])
async def get_category_item_route(category_id: CategoryEnum, item_id: ObjectID,
                                  db: AsyncIOMotorClient = Depends(get_database)) -> ItemInResponse:
    """Get the details about a particular item"""
    # TODO: add particular item fetching
    return {"success": True}


@router.post("/{category_id}", response_model=ItemInResponse, dependencies=[Depends(verify_token)], tags=["add"])
async def add_item_route(category_id: CategoryEnum, item: Union[Movie, Anime, Show, Music, Book],
                         db: AsyncIOMotorClient = Depends(get_database)) -> ItemInResponse:
    """Add item to a given category"""

    # creating dict for checking response body
    classof = {
        CategoryEnum.movies: Movie,
        CategoryEnum.shows: Show,
        CategoryEnum.anime: Anime,
        CategoryEnum.books: Book,
        CategoryEnum.music: Music
    }

    # checking if request body is of correct type
    if not isinstance(item, classof[category_id]):
        raise HTTPException(
            status_code=400, detail=f'item does not match {category_id} schema')

    # Adding into db
    _res = await db[category_id]["data"].insert_one(item.dict())

    return ItemInResponse(data=item)


@router.patch("/{category_id}/{item_id}", response_model=ItemInResponse, dependencies=[Depends(verify_token)], tags=["update"])
async def update_item_route(category_id: CategoryEnum,item_id: ObjectID, 
                            item: Union[Movie, Anime, Show, Music, Book],db: AsyncIOMotorClient = Depends(get_database)) -> ItemInResponse:
    """Update a given item"""
    classof = {
        CategoryEnum.movies: Movie,
        CategoryEnum.shows: Show,
        CategoryEnum.anime: Anime,
        CategoryEnum.books: Book,
        CategoryEnum.music: Music
    }

    # checking if request body is of correct type
    if not isinstance(item, classof[category_id]):
        raise HTTPException(
            status_code=400, detail=f'Item does not match {category_id} schema')
    _res = await db[category_id]["data"].update_one({"_id": item_id},{"$set":item.dict()})
    if (_res.matched_count==0):
        raise HTTPException(
            status_code=400, detail=f'ObjectID {item_id} not found in {category_id}')
    return ItemInResponse(data=item.dict())    


@router.post("/{category_id}/rate/{item_id}", response_model=ResponseBase, tags=["user", "rate"])
async def rate_item_route(category_id: CategoryEnum, item_id: ObjectID, rating: float,
                          token: dict = Depends(verify_token),
                          db: AsyncIOMotorClient = Depends(get_database)) -> ResponseBase:
    """"Rate a given item"""
    # TODO add rating functionality here
    return {"success": True}
