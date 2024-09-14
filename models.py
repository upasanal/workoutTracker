from sqlalchemy import Column, Integer, String, Float, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column

Base = declarative_base()


class Workout(Base):
    __tablename__ = "workouts"

    id = mapped_column(Integer, primary_key=True, index=True)
    date_time = mapped_column(DateTime, server_default=func.now())  
    duration = mapped_column(Float, nullable=False)  # Duration in minutes
    distance = mapped_column(Float, nullable=False)  # Distance in kilometers
    route= mapped_column(String, nullable=True)  # Optional
    heart_rate = mapped_column(Integer, nullable=True)
    photo_url = Column(String, nullable=True)   # Optional
    # Default to current time


