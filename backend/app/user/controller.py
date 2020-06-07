import logging
from typing import Dict

from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient

from ..models.base import ObjectID, CategoryEnum
from ..models.responses import LikeInResponse, UserInResponse, UsersInResponse
from ..models.user import LikeEnum, User, Like
from ..utils.mongodb import get_database
from ..utils.token import verify_token

router = APIRouter()


@router.get("/{user_id}", response_model=UserInResponse, tags=["fetch"])
async def get_user_route(user_id: ObjectID,
                         db: AsyncIOMotorClient = Depends(get_database)) -> UserInResponse:
    """Get user information for logged in user"""
    # TODO fetch user functionality
    return {"success": True}


# NOTE: not required as of now
# @router.patch("/", response_model=UserInResponse, tags=["update"])
# async def update_user_route(token: dict = Depends(verify_token),
#                             db: AsyncIOMotorClient = Depends(get_database)) -> UserInResponse:
#     """Update user information for logged in user"""
#     return {"success": True}


@router.post("/like/{category_id}/{item_id}", response_model=LikeInResponse, tags=["like"])
async def like_item_route(category_id: CategoryEnum, item_id: str, like: Like,
                          token: dict = Depends(verify_token),
                          db: AsyncIOMotorClient = Depends(get_database)) -> LikeInResponse:
    """Like a given shared item"""

    _update = await db.core.users.update_one(token, {
        "$set": {f"likes.{category_id}.{item_id}": like.value}
    })
    return LikeInResponse(data=like, category_id=category_id, item_id=item_id)
