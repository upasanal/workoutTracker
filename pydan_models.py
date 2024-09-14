from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Pydantic model for creating a new workout
class WorkoutCreate(BaseModel):
    date_time: datetime
    duration: int
    distance: float
    route: Optional[str] = None
    heart_rate: Optional[int] = None
    photo_url: Optional[str] = None

# Pydantic model for returning workout details
class WorkoutDetails(BaseModel):
    id: int
    date_time: datetime
    duration: int
    distance: float
    route: Optional[str]
    heart_rate: Optional[int]
    photo_url: Optional[str]

    class Config:
        orm_mode = True


