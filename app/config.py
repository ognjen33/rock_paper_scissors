from app.db.session import SessionLocal
from alembic.config import Config
from alembic import command


RANDOM_API_URL = 'https://codechallenge.boohma.com/random'

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def run_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

