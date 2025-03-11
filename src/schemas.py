from datetime import datetime

from pydantic import BaseModel


class TaskSchema(BaseModel):
    name: str
    date_limit: datetime


class TaskTimeSchema(BaseModel):
    name: str
    time_remaining: float
