# JWT token auth handlers
import logging

from fastapi import Header, HTTPException
import jwt

from config import SECRET_KEY


async def verify_token(authorization: str = Header(None)):
    """Verify JWT token for protected routes"""
    # NOTE: remove if extra jwt auth not required
    try:
        decoded_token = jwt.decode(
            authorization, str(SECRET_KEY), algorithms=["HS256"])
        return decoded_token
    except Exception as e:
        raise HTTPException(
            status_code=401, detail=f"[Authorization] {e}")
