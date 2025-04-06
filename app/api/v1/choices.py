from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.choice import ChoiceOut, ChoiceCreate
from app.schemas.game import GamePlay, GameResult
from app.services.choice_service import list_choices, create_choice, get_choice
from app.services.random_mapper import fetch_and_map_random_value
from app.services.play_game import play_game_vs_computer

router = APIRouter()

# Todo move to separate file, think about were should it live. /db config?
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/choices", response_model=list[ChoiceOut])
def get_choices(db: Session = Depends(get_db)):
    return list_choices(db)

# Helper for creating choices in database, will be moved to migration
@router.post("/choices", response_model=ChoiceOut, status_code=201)
def create_new_choice(choice: ChoiceCreate, db: Session = Depends(get_db)):
    return create_choice(db, choice)

@router.get("/choice", response_model=ChoiceOut)
async def get_random_choice(db: Session = Depends(get_db)):
    # Todo Move this to constant in some kind of config file
    api_url = 'https://codechallenge.boohma.com/random'
    try:
        choice_id = await fetch_and_map_random_value(api_url)
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return get_choice(db, choice_id)

@router.post("/play", response_model=GameResult, status_code=201)
async def play_game(game_play: GamePlay, db: Session = Depends(get_db)):
    # Todo Move this to constant in some kind of config file
    api_url = 'https://codechallenge.boohma.com/random'

    try:
        computer_choice_id = await fetch_and_map_random_value(api_url)
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return play_game_vs_computer(db, game_play, computer_choice_id)


