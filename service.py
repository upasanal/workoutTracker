from sqlalchemy.orm import Session
import models
import pydan_models

def create_workout(db: Session, workout: pydan_models.WorkoutCreate):
    # Using model_dump() to avoid deprecated dict() method
    db_workout = models.Workout(**workout.model_dump())
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout

def get_workouts(db: Session):
    return db.query(models.Workout).all()

def get_workout(db: Session, workout_id: int):
    return db.query(models.Workout).filter(models.Workout.id == workout_id).first()

def delete_workout_by_id(db: Session, workout_id: int):
    db_workout = get_workout(db, workout_id)
    if db_workout:
        db.delete(db_workout)
        db.commit()
    return db_workout



