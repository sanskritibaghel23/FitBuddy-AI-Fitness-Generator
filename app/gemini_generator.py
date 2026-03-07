import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_fitness_plan(goal, intensity):

    prompt = f"""
    You are a professional fitness trainer and nutrition expert.

    Goal: {goal}
    Intensity: {intensity}

    Create a 7-day workout plan.

    Each day must include:
    Warm-up
    Exercises with sets and reps
    Cooldown

    Also provide one helpful nutrition tip.

    Format:

    WORKOUT PLAN
    Day 1:
    ...

    Day 7:
    ...

    NUTRITION TIP:
    ...
    """

    response = model.generate_content(prompt)

    text = response.text

    parts = text.split("NUTRITION TIP:")

    workout_plan = parts[0]
    nutrition_tip = parts[1] if len(parts) > 1 else ""

    return workout_plan, nutrition_tip
