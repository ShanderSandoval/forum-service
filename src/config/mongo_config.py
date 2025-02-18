import os
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from model.forum_model import Forum

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DATABASE_NAME = os.getenv("MONGO_DATABASE_NAME", "projectManagement")

async def init_db():
    client = AsyncIOMotorClient(MONGO_URI)
    database = client[MONGO_DATABASE_NAME]

    await init_beanie(database, document_models=[Forum])
