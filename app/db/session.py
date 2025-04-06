from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.choices import Base

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Create tables
Base.metadata.create_all(bind=engine)

