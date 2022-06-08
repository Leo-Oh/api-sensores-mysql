from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime, time

class StatusSensor(BaseModel):
    topic: str
    status: int
