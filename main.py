from fastapi import FastAPI
from app.api.v1.api_base import api_router
from app.db.session import engine
from app.models.choices import Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Clean FastAPI App")

app.include_router(api_router)

