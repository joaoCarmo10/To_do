from fastapi import FastAPI
from core.config import settings
from beanie import init_beanie
from motor.motor_asybcio import AsyncIOMotorClient

app = FastAPI()

app = FastAPI(
    title = settings.PROJECT_NAME,
    openapi_url = f'{settings.API_V1_STR}/openapi.json'
)

