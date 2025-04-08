from sqlalchemy.orm import Session
from app.models.choices import Choice

def get_all_choices(db: Session):
    return db.query(Choice).all()

def get_choice(db: Session, choice_id: int):
    return db.query(Choice).filter(Choice.id == choice_id).one_or_none()
