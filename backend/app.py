from fastapi import FastAPI
from routes import router   # IMPORTANT LINE
from database import engine
from models import Base

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(router)  # IMPORTANT LINE

@app.get("/")
def home():
    return {"message": "FitBuddy Backend Running"}