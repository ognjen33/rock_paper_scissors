from sqlalchemy import Column, Integer, Enum, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from app.models.base import Base
import enum
from sqlalchemy.sql import func


class GameResult(enum.Enum):
    win = "win"
    lose = "lose"
    tie = "tie"


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    
    player_id = Column(Integer, ForeignKey("choices.id"), nullable=False)
    computer_id = Column(Integer, ForeignKey("choices.id"), nullable=False)

    result = Column(Enum(GameResult), nullable=False)

    created_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # Relationships
    player = relationship("Choice", foreign_keys=[player_id])
    computer = relationship("Choice", foreign_keys=[computer_id])
