from fastapi import APIRouter
from app.api.v1 import choices

api_router = APIRouter()
api_router.include_router(choices.router, prefix="", tags=["Choices"])

