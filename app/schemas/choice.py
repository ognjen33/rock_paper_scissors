from pydantic import BaseModel
from app.models.choices import ChoiceEnum
from typing import List

class ChoiceOut(BaseModel):
    id: int
    name: ChoiceEnum
    wins: List[ChoiceEnum]

    class Config:
        orm_mode = True

