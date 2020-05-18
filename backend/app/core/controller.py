import hashlib
import urllib
import logging
import random

from cas import CASClient
from fastapi import APIRouter, Depends, HTTPException
import jwt
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.responses import RedirectResponse
import ujson

from app.utils.cas import get_cas
from app.utils.token import verify_token
from app.utils.mongodb import get_database
from app.models.user import StateInResponse, Audit
from app.models.questionnaire import QuestionnaireInResponse
from config import SECRET_KEY

router = APIRouter()


@router.get("/login", tags=["auth"])
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
        # TODO add additional login functionality here
        redirect_url = f"{next}#/?user={_user}"
        return RedirectResponse(url=redirect_url)


# TODO add aditional routes here
