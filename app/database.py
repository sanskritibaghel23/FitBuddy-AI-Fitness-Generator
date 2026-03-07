from sqlalchemy import create_engine, Column, String, Integer, Float, Text
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///fitbuddy.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    weight = Column(Float)
    goal = Column(String)
    intensity = Column(String)


class WorkoutPlan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String)
    original_plan = Column(Text)
    updated_plan = Column(Text)


Base.metadata.create_all(bind=engine)


def save_user(user_id, name, age, weight, goal, intensity):

    db = SessionLocal()

    existing_user = db.query(User).filter(User.id == user_id).first()

    if not existing_user:

        user = User(
            id=user_id,
            name=name,
            age=age,
            weight=weight,
            goal=goal,
            intensity=intensity
        )

        db.add(user)
        db.commit()

    db.close()


def save_plan(user_id, plan):
    db = SessionLocal()

    workout = WorkoutPlan(
        user_id=user_id,
        original_plan=plan
    )

    db.add(workout)
    db.commit()
    db.close()


def get_original_plan(user_id):

    db = SessionLocal()

    plan = db.query(WorkoutPlan)\
        .filter(WorkoutPlan.user_id == user_id)\
        .order_by(WorkoutPlan.id.desc())\
        .first()

    db.close()

    return plan.original_plan if plan else None


def update_plan(user_id, updated_plan):

    db = SessionLocal()

    plan = db.query(WorkoutPlan)\
        .filter(WorkoutPlan.user_id == user_id)\
        .order_by(WorkoutPlan.id.desc())\
        .first()

    if plan:
        plan.updated_plan = updated_plan
        db.commit()

    db.close()