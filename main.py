from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from typing import List

import service
import models
import pydan_models
from database import SessionLocal, engine

# Create the database tables
models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST: Create a new workout
@app.post("/workouts/", response_model=pydan_models.WorkoutDetails)
def create_workout(workout: pydan_models.WorkoutCreate, db: Session = Depends(get_db)):
    return service.create_workout(db=db, workout=workout)

# GET: Retrieve workouts with optional filtering
@app.get("/workouts/", response_model=List[pydan_models.WorkoutDetails])
def get_workouts(db: Session = Depends(get_db)):
    workouts = service.get_workouts(db)
    return workouts

# GET: Retrieve a specific workout by ID
@app.get("/workouts/{workout_id}", response_model=pydan_models.WorkoutDetails)
def get_workout_by_id(workout_id: int, db: Session = Depends(get_db)):
    db_workout = service.get_workout(db, workout_id=workout_id)
    if db_workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return db_workout

# DELETE: Remove a workout by ID
@app.delete("/workouts/{workout_id}", response_model=pydan_models.WorkoutDetails)
def delete_workout(workout_id: int, db: Session = Depends(get_db)):
    db_workout = service.get_workout(db, workout_id=workout_id)
    if db_workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    
    return service.delete_workout_by_id(db, workout_id=workout_id)