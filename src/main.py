from fastapi import FastAPI
from dotenv import load_dotenv
import os
import uvicorn
import asyncio

from config import mongo_config
from controller.forum_controller import ForumController

load_dotenv()

app = FastAPI()

asyncio.run(mongo_config.init_db())

app.include_router(ForumController.router)

if __name__ == "__main__":
    try:
        host = os.getenv("UVICORN_HOST", "0.0.0.0")
        port = int(os.getenv("UVICORN_PORT", "10103"))

        print(f"Starting server on {host}:{port}...")
        uvicorn.run(app, host=host, port=port)
    except ValueError:
        print("Invalid port number. Please check the UVICORN_PORT environment variable.")
