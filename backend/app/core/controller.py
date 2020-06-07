import hashlib
import logging
import random
import urllib

import jwt

import ujson
from cas import CASClient
from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.responses import RedirectResponse

from config import SECRET_KEY
from ..models.category import Category
from ..models.responses import (CategorysInResponse, ResponseBase,
                                UsersInResponse)
from ..models.user import User
from ..utils.cas import get_cas
from ..utils.mongodb import get_database
from ..utils.token import verify_token

router = APIRouter()


@router.get("/login", tags=["auth"], include_in_schema=False)
async def login_route(next: str = "/", ticket: str = None, cas_client: CASClient = Depends(get_cas),
                      db: AsyncIOMotorClient = Depends(get_database)):
    """login using CAS login

    """
    if not ticket:
        # No ticket, the request come from end user, send to CAS login
        cas_login_url = cas_client.get_login_url()
        return RedirectResponse(url=cas_login_url)

    _user, attributes, _ = cas_client.verify_ticket(ticket)
    if not _user:
        return {
            "success": 0,
            "message": "Invalid user! Retry logging in!"
        }
    else:
        logging.debug(f"CAS verify ticket response: user: {_user}")
        if await db["core"]["users"].find_one({"username": _user}):
            _res = await db["core"]["users"].update_one({
                "last_login": attributes["authenticationDate"]
            })
        else:
            _res = await db["core"]["users"].insert_one({
                "username": _user,
                "last_login": attributes["authenticationDate"],
                "first_login": attributes["authenticationDate"],
            })

        jwt_token = jwt.encode({'username': _user}, str(
            SECRET_KEY), algorithm="HS256").decode()
        return ResponseBase(data={
            "token": jwt_token
        })


@router.get("/categories", response_model=CategorysInResponse, dependencies=[Depends(verify_token)], tags=["fetch", "categories"])
async def get_category_list(db: AsyncIOMotorClient = Depends(get_database)) -> CategorysInResponse:
    """Returns list of categories available"""
    categories = [Category(**category) async for
                  category in db["core"]["categories"].find()]
    return CategorysInResponse(data=categories)


@router.get("/users", response_model=UsersInResponse, dependencies=[Depends(verify_token)], tags=["fetch", "users", "testing"])
async def get_users_route(db: AsyncIOMotorClient = Depends(get_database)) -> UsersInResponse:
    """Get user information for logged in user"""
    users = [User(**user) async for user in db["core"]["users"].find()]
    return UsersInResponse(data=users)
