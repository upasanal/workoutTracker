from sqlalchemy.orm import Session
import models
import pydan_models

def create_workout(db: Session, workout: pydan_models.WorkoutCreate):
    """Creates a workout instance in sql table by converting passed in pydantic model instance"""
    # https://docs.pydantic.dev/latest/concepts/models/#model-signature
    # Pydantic documentation used to turn pydantic model into sql alchemy workout entity
    # format by argument unpacking the dictionary created
    db_workout = models.Workout(**workout.model_dump())
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout

def get_workouts(db: Session):
    """Returns all workouts"""
    return db.query(models.Workout).all()

def get_workout(db: Session, workout_id: int):
    """Gets specific workout at given id"""
    return db.query(models.Workout).filter(models.Workout.id == workout_id).first()

def delete_workout_by_id(db: Session, workout_id: int):
    """Deletes workout by id"""
    db_workout = get_workout(db, workout_id)
    if db_workout:
        db.delete(db_workout)
        db.commit()
    return db_workout



