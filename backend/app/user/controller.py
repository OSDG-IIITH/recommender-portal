from typing import Dict

from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient

from ..models.base import ObjectID
from ..models.responses import LikeInResponse, UserInResponse, UsersInResponse
from ..models.user import LikeEnum, User
from ..utils.mongodb import get_database
from ..utils.token import verify_token

router = APIRouter()


@router.post("/signup", tags=["signup", "auth", "testing"])
async def signup_route(user: User, db: AsyncIOMotorClient = Depends(get_database)):
    """Signup route (for testing)"""
    return {"success": True}



@router.get("/{user_id}", response_model=UserInResponse, tags=["fetch"])
async def get_user_route(user_id: ObjectID,
                         db: AsyncIOMotorClient = Depends(get_database)) -> UserInResponse:
    """Get user information for logged in user"""
    # TODO fetch user functionality
    return {"success": True}


@router.patch("/", response_model=UserInResponse, tags=["update"])
async def update_user_route(token: dict = Depends(verify_token),
                            db: AsyncIOMotorClient = Depends(get_database)) -> UserInResponse:
    """Update user information for logged in user"""
    # TODO update user functionality
    return {"success": True}


@router.post("/like/{category_id}/{item_id}", response_model=LikeInResponse, tags=["like"])
async def like_item_route(category_id: str, item_id: str, value: LikeEnum,
                          token: dict = Depends(verify_token),
                          db: AsyncIOMotorClient = Depends(get_database)) -> LikeInResponse:
    """Like a given shared item"""
    # TODO like item route
    return {"success": True}
