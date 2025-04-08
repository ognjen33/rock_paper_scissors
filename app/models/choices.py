from sqlalchemy import Column, Integer, Date, Enum as SqlEnum, Text
from enum import Enum
from sqlalchemy.types import TypeDecorator
import json
from app.models.base import Base



# SQLite does not support native array tipe, this is workaround
class JSONEncodedList(TypeDecorator):
    impl = Text

    def process_bind_param(self, value, dialect):
        if value is not None:
            return json.dumps(value)
        return "[]"

    def process_result_value(self, value, dialect):
        if value:
            return json.loads(value)
        return []

class ChoiceEnum(str, Enum):
    rock = "rock"
    paper = "paper"
    scissors = "scissors"
    lizzard = "lizzard"
    spock = "spock"


class Choice(Base):
    __tablename__ = "choices"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(SqlEnum(ChoiceEnum), nullable=False)
    wins = Column(JSONEncodedList, nullable=False, default=[])
