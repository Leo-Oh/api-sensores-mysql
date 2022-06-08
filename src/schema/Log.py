from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime, time

class Log(BaseModel):
    id: Optional[int]
    topic: str
    value: float
    date: date
    time: time
