import logging

from motor.motor_asyncio import AsyncIOMotorClient
from config import DATABASE_URL, MIN_CONNECTIONS_COUNT, MAX_CONNECTIONS_COUNT
from .mongodb import db


async def connect_db():
    """Connect to the database on startup"""
    logging.debug("Connecting to database client")
    db.client = AsyncIOMotorClient(DATABASE_URL,
                                   maxPoolSize=MAX_CONNECTIONS_COUNT,
                                   minPoolSize=MIN_CONNECTIONS_COUNT)


async def disconnect_db():
    """Disconnect from the database"""
    logging.debug("Disconnecting from database")
    db.client.close()
