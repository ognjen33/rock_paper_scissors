from pydantic import BaseModel
from app.models.choices import ChoiceEnum
from typing import List

class ChoiceCreate(BaseModel):
    name: ChoiceEnum
    wins: List[ChoiceEnum]

class ChoiceOut(BaseModel):
    id: int
    name: ChoiceEnum
    wins: List[ChoiceEnum]

    class Config:
        orm_mode = True

