from sqlalchemy.orm import Session
from app.models.choices import Choice
from app.schemas.choice import ChoiceCreate

def get_all_choices(db: Session):
    return db.query(Choice).all()

# TODO nece biti create choice, ovo je samo helper za kreiranje
# recorda u bazi, prebaciti na migraciju
def create_choice(db: Session, choice: ChoiceCreate):
    db_choice = Choice(name=choice.name, wins=choice.wins)
    db.add(db_choice)
    db.commit()
    db.refresh(db_choice)
    return db_choice

def get_choice(db: Session, choice_id: int):
    return db.query(Choice).filter(Choice.id == choice_id).one_or_none()
