from sqlalchemy.orm import Session
from app.repositories import choice as choice_repo


def list_choices(db: Session):
    return choice_repo.get_all_choices(db)

def get_choice(db: Session, choice_id: int):
    return choice_repo.get_choice(db, choice_id)

