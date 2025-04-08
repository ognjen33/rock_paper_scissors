from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.game import GamePlay, GameResult, GameStats
from app.services.random_mapper import fetch_and_map_random_value
from app.services.game import play_game_vs_computer, get_last_10_games, get_game_statistics
from app.config import get_db, RANDOM_API_URL

router = APIRouter()

@router.get("/games", response_model=list[GameResult])
def get_games(db: Session = Depends(get_db)):
    return get_last_10_games(db)

@router.get("/games/statistics", response_model=GameStats)
def get_games_stats(db: Session = Depends(get_db)):
    return get_game_statistics(db)

@router.post("/play", response_model=GameResult, status_code=201)
async def play_game(game_play: GamePlay, db: Session = Depends(get_db)):
    try:
        computer_choice_id = await fetch_and_map_random_value(RANDOM_API_URL)
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return play_game_vs_computer(db, game_play, computer_choice_id)

