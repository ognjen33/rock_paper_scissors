from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.choice import ChoiceOut
from app.services.choice import list_choices, get_choice
from app.services.random_mapper import fetch_and_map_random_value
from app.config import get_db, RANDOM_API_URL

router = APIRouter()


@router.get("/choices", response_model=list[ChoiceOut])
def get_choices(db: Session = Depends(get_db)):
    return list_choices(db)

@router.get("/choice", response_model=ChoiceOut)
async def get_random_choice(db: Session = Depends(get_db)):
    try:
        choice_id = await fetch_and_map_random_value(RANDOM_API_URL)
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return get_choice(db, choice_id)

