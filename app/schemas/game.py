from pydantic import BaseModel, Field
from app.models.choices import ChoiceEnum

class GamePlay(BaseModel):
    player: int = Field(ge=0, le=5)

class GameResult(BaseModel):
    result: str
    player: int = Field(ge=0, le=5)
    computer: int = Field(ge=0, le=5)

    class Config:
        orm_mode = True

