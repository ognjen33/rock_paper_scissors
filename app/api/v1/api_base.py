from fastapi import APIRouter
from app.api.v1 import choice, game

api_router = APIRouter()
api_router.include_router(choice.router, prefix="", tags=["Choices"])
api_router.include_router(game.router, prefix="", tags=["Game"])
