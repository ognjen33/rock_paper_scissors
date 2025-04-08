import logging
from fastapi import FastAPI
from app.api.v1.api_base import api_router
from app.db.session import engine
from app.models.choices import Base
from app.config import run_migrations
# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="RockPaperScissorsLizardSpock Game")

# Run migrations at startup
@app.on_event("startup")
async def startup_event():
    logging.info("Root endpoint called")
    run_migrations()

app.include_router(api_router)

