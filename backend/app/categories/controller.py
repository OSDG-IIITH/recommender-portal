from typing import Dict, List, Union

from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient

from ..models.base import ObjectID, CategoryEnum
from ..models.category import Anime, Movie, Music, Show, Book
from ..models.ratings import Rating
from ..models.responses import (ItemInResponse,
                                ItemsInResponse, ResponseBase)
from ..utils.mongodb import get_database
from ..utils.token import verify_token

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


@router.get("/{category_id}/{item_id}",
            response_model=ItemInResponse, tags=["fetch", "item"])
async def get_category_item_route(category_id: CategoryEnum, item_id: ObjectID,
                                  db: AsyncIOMotorClient = Depends(get_database)) -> ItemInResponse:
    """Get the details about a particular item"""

    _res = await db[category_id]["data"].find_one({"_id": item_id})
    if _res:
        return ItemInResponse(data=_res)
    raise HTTPException(
        status_code=404,
        detail=f'ObjectID {item_id} not found in {category_id}')


@router.post("/{category_id}", response_model=ItemInResponse,
             dependencies=[Depends(verify_token)], tags=["add"])
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
        raise HTTPException(status_code=400,
                            detail=f'item does not match {category_id} schema')

    # current item.id is set to None, should be removed
    item_dict = item.dict()
    item_dict.pop('id')

    # Adding into db
    _res = await db[category_id]["data"].insert_one(item_dict)

    # update id to the inserted id
    item.id = _res.inserted_id

    return ItemInResponse(data=item)


@router.patch("/{category_id}/{item_id}", response_model=ItemInResponse,
              dependencies=[Depends(verify_token)], tags=["update"])
async def update_item_route(category_id: CategoryEnum, item_id: ObjectID,
                            item: Union[Movie, Anime, Show, Music, Book],
                            db: AsyncIOMotorClient = Depends(get_database)) -> ItemInResponse:
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
        raise HTTPException(status_code=400,
                            detail=f'Item does not match {category_id} schema')
    # current item.id is set to None, should be removed
    item_dict = item.dict()
    item_dict.pop('id')
    _res = await db[category_id]["data"].update_one({"_id": item_id}, {"$set": item_dict})
    if _res.matched_count == 0:
        raise HTTPException(
            status_code=400,
            detail=f'ObjectID {item_id} not found in {category_id}')

    # add id to the item
    item.id = item_id
    return ItemInResponse(data=item.dict())


@router.post("/{category_id}/rate/{item_id}",
             response_model=ResponseBase, tags=["user", "rate"])
async def rate_item_route(category_id: CategoryEnum, item_id: ObjectID, _rating: Dict[str, float],
                          token: dict = Depends(verify_token),
                          db: AsyncIOMotorClient = Depends(get_database)) -> ResponseBase:
    """"Rate a given item"""
    rating = _rating.get("rating", None)
    item = await db[category_id]["data"].find_one({"_id": item_id})
    if item and rating:
        # update/insert a rating into the `ratings` collection
        token.update({"item_id": item_id})
        _res = await db[category_id]["ratings"].update_one(token, {
            "$set": {"rating": rating}
        }, upsert=True)

        if _res.upserted_id:
            # first time a document is inserted, add `rating_id` as well to
            # user collection
            update_key = f"ratings.{category_id}.{item_id}"
            _rating.update({"rating_id": _res.upserted_id})
        else:
            # subsequent times rating is updated, only update rating field
            update_key = f"ratings.{category_id}.{item_id}.rating"
            _rating = rating

        token.pop("item_id")  # to update user, `item_id` is not required
        _user_update = await db.core.users.update_one(token, {
            "$set": {
                update_key: _rating
            }
        })

        rate = Rating(item_id=item_id, username=token.get(
            'username'), rating=rating)
        return ResponseBase(data=[rate.dict()])

    return ResponseBase(success=False, error=[
                        f"Item not found in {category_id} schema!"])
