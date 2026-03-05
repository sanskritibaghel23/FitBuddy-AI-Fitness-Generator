from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE USER (POST)
@router.post("/users")
def create_user(name: str, age: int, weight: float, goal: str, intensity: str, db: Session = Depends(get_db)):
    new_user = User(
        name=name,
        age=age,
        weight=weight,
        goal=goal,
        intensity=intensity
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# GET ALL USERS
@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users