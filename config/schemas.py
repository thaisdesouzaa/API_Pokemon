from typing import List
from pydantic import BaseModel


class Time(BaseModel):
    user:str
    team:List[str]
