import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.base import Base
from app.models.game import Game
from app.models.choices import Choice

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

@pytest.fixture(scope="function")
def db_session():
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    Base.metadata.create_all(bind=engine)
    
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture
def sample_choices(db_session):
    choices = [
        Choice(id=1, name="rock", wins=["scissors", "lizzard"]),
        Choice(id=2, name="paper",wins=["scissors", "lizzard"]),
        Choice(id=3, name="scissors",wins=["scissors", "lizzard"]),
        Choice(id=4, name="lizzard",wins=["scissors", "lizzard"]),
        Choice(id=5, name="spock",wins=["scissors", "lizzard"]),


    ]
    db_choices = db_session.query(Choice).all()
    if len(db_choices) == 5:
        return choices
    for choice in choices:
        db_session.add(choice)
    db_session.commit()
    return choices
