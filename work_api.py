from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from typing import List

import service
import models
import pydan_models
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/workouts/", response_model=pydan_models.WorkoutDetails)
def create_workout(workout: pydan_models.WorkoutCreate, db: Session = Depends(get_db)):
    """
    Create a new workout

    Parameters:
        Takes in a WorkoutCreate instance 

    Returns:
        list[Organization]: All `Organization`s in the `Organization` database table
    """
    return service.create_workout(db=db, workout=workout)


@app.get("/workouts/", response_model=List[pydan_models.WorkoutDetails])
def get_workouts(db: Session = Depends(get_db)):
    """
    Get workouts

    Parameters:
        n/a

    Returns:
        All workouts in the database using get_workouts service method.
    """
    workouts = service.get_workouts(db)
    return workouts


@app.get("/workouts/{workout_id}", response_model=pydan_models.WorkoutDetails)
def get_workout_by_id(workout_id: int, db: Session = Depends(get_db)):
    """
    Get workout given a specific id

    Parameters:
        workout_id: A valid integer id 

    Returns:
        The workout at an ID if existing, else 404 error
    """
    db_workout = service.get_workout(db, workout_id=workout_id)
    if db_workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return db_workout


@app.delete("/workouts/{workout_id}", response_model=pydan_models.WorkoutDetails)
def delete_workout(workout_id: int, db: Session = Depends(get_db)):
    """
    Delete a workout given an id

    Parameters:
        workout_id: A valid_ID

    Returns:
       Workout that was deleted 
    """
    db_workout = service.get_workout(db, workout_id=workout_id)
    if db_workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    
    return service.delete_workout_by_id(db, workout_id=workout_id)