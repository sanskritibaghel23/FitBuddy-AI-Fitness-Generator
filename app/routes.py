from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.gemini_generator import generate_fitness_plan
from app.updated_plan import update_workout_plan

from app.database import (
    save_user,
    save_plan,
    get_original_plan,
    update_plan,
    SessionLocal,
    User,
    WorkoutPlan
)

router = APIRouter()

templates = Jinja2Templates(directory="templates")


# -------------------------
# Delete plan
# -------------------------
@router.get("/delete-plan/{plan_id}")
def delete_plan(plan_id: int):

    db = SessionLocal()

    plan = db.query(WorkoutPlan).filter(
        WorkoutPlan.id == plan_id
    ).first()

    if plan:
        db.delete(plan)
        db.commit()

    db.close()

    return {"message": "Plan deleted"}


# -------------------------
# User plan history
# -------------------------
@router.get("/user-plans/{user_id}", response_class=HTMLResponse)
def user_plan_history(request: Request, user_id: str):

    db = SessionLocal()

    plans = db.query(WorkoutPlan).filter(
        WorkoutPlan.user_id == user_id
    ).all()

    db.close()

    return templates.TemplateResponse(
        "plan_history.html",
        {
            "request": request,
            "plans": plans,
            "user_id": user_id
        }
    )


# -------------------------
# Home page
# -------------------------
@router.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


# -------------------------
# Generate workout + nutrition
# SINGLE GEMINI CALL
# -------------------------
@router.post("/generate-workout", response_class=HTMLResponse)
def generate_plan(
    request: Request,
    username: str = Form(...),
    user_id: str = Form(...),
    age: int = Form(...),
    weight: float = Form(...),
    goal: str = Form(...),
    intensity: str = Form(...)
):

    # Save user
    save_user(user_id, username, age, weight, goal, intensity)

    # ONE AI CALL
    workout_plan, nutrition_tip = generate_fitness_plan(goal, intensity)

    # Save plan
    save_plan(user_id, workout_plan)

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "username": username,
            "user_id": user_id,
            "age": age,
            "weight": weight,
            "goal": goal,
            "intensity": intensity,
            "workout_plan": workout_plan,
            "nutrition_tip": nutrition_tip
        }
    )


# -------------------------
# Update plan with feedback
# -------------------------
@router.post("/submit-feedback")
def submit_feedback(
    request: Request,
    user_id: str = Form(...),
    feedback: str = Form(...)
):

    original = get_original_plan(user_id)

    updated = update_workout_plan(original, feedback)

    update_plan(user_id, updated)

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "workout_plan": updated
        }
    )


# -------------------------
# Admin dashboard
# -------------------------
@router.get("/view-all-users", response_class=HTMLResponse)
def view_all_users(request: Request):

    db = SessionLocal()

    users = db.query(User).all()

    user_data = []

    for user in users:

        plans = db.query(WorkoutPlan).filter(
            WorkoutPlan.user_id == user.id
        ).all()

        for plan in plans:

            user_data.append({
                "id": user.id,
                "name": user.name,
                "age": user.age,
                "weight": user.weight,
                "goal": user.goal,
                "intensity": user.intensity,
                "original_plan": plan.original_plan,
                "updated_plan": plan.updated_plan
            })

    db.close()

    return templates.TemplateResponse(
        "all_users.html",
        {
            "request": request,
            "users": user_data
        }
    )