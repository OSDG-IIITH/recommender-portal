from typing import Dict

from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from typing_extensions import Literal

from app.utils.token import verify_token
from app.utils.mongodb import get_database
from app.models.base import ObjectID
from app.models.user import User, LikeEnum
from app.models.responses import UserInResponse, UsersInResponse, LikeInResponse

router = APIRouter()


@router.post("/signup", tags=["signup", "auth", "testing"])
async def signup_route(user: User, db: AsyncIOMotorClient = Depends(get_database)):
    """Signup route (for testing)"""
    # TODO signup functionality
    return {"success": True}


@router.get("/", response_model=UsersInResponse, dependencies=[Depends(verify_token)], tags=["fetch", "bulk"])
async def get_users_route(db: AsyncIOMotorClient = Depends(get_database)) -> UsersInResponse:
    """Get user information for logged in user"""
    # TODO fetch users functionality
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
