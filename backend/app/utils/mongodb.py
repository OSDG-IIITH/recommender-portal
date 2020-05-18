from motor.motor_asyncio import AsyncIOMotorClient


class Database:
    # TODO replace with relevant db connector
    client: AsyncIOMotorClient = None


db = Database()


async def get_database() -> AsyncIOMotorClient:
    return db.client
