import logging

from fastapi import APIRouter, Depends, HTTPException, Depends
from motor.motor_asyncio import AsyncIOMotorClient

from ..models.base import ObjectID, CategoryEnum
from ..models.responses import LikeInResponse, UserInResponse
from ..models.user import Like
from ..utils.mongodb import get_database
from ..utils.token import verify_token

router = APIRouter()


@router.get("/me", response_model=UserInResponse, tags=["fetch"])
async def get_user_route(token: dict = Depends(verify_token),
                         db: AsyncIOMotorClient = Depends(get_database)) -> UserInResponse:
    """Get user information for logged in user"""
    _user = await db.core.users.find_one(token)
    if _user:
        return UserInResponse(data=_user)
    raise HTTPException(
        status_code=400, detail="User doesn't exist in DB")


# NOTE: not required as of now
# @router.patch("/", response_model=UserInResponse, tags=["update"])
# async def update_user_route(token: dict = Depends(verify_token),
#                             db: AsyncIOMotorClient = Depends(get_database)) -> UserInResponse:
#     """Update user information for logged in user"""
#     return {"success": True}


@router.post("/like/{category_id}/{item_id}",
             response_model=LikeInResponse, tags=["like"])
async def like_item_route(category_id: CategoryEnum, item_id: ObjectID, like: Like,
                          token: dict = Depends(verify_token),
                          db: AsyncIOMotorClient = Depends(get_database)) -> LikeInResponse:
    """Like a given shared item"""
    _res = await db[category_id]["data"].find_one({"_id": item_id})
    if _res:
        _update = await db.core.users.update_one(token, {
            "$set": {f"likes.{category_id}.{item_id}": like.value}
        })
        return LikeInResponse(data=like, category_id=category_id, item_id=item_id)

    raise HTTPException(
        status_code=400, detail=f'Item id {item_id} not found in {category_id}')
