from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class WorkoutCreate(BaseModel):
    """Created class that handles front end passed in info to create a workout"""
    date_time: datetime
    duration: int
    distance: float
    route: Optional[str] = None
    heart_rate: Optional[int] = None
    photo_url: Optional[str] = None
    weather: Optional[str] = None


class WorkoutDetails(BaseModel):
    """Created a class that represents what the API responses are, which are basically the same but with ids!"""
    id: int
    date_time: datetime
    duration: int
    distance: float
    route: Optional[str]
    heart_rate: Optional[int]
    photo_url: Optional[str]
    weather: Optional[str] 

    class Config:
        orm_mode = True
    # Without orm_mode, would have to manually convert ORM object to something the pydantic model would understand
    # like a dictionary or a list, now you don't need to. 


