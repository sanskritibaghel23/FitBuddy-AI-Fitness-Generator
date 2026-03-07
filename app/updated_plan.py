import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("AIzaSyBiLvaBf4qzn66UBYoEDlBkfWIJCEKEeYk"))

model = genai.GenerativeModel("gemini-2.5-flash")


def update_workout_plan(original_plan, feedback):

    prompt = f"""
    Here is the workout plan:

    {original_plan}

    User feedback:
    {feedback}

    Update the plan accordingly.
    """

    response = model.generate_content(prompt)

    return response.text