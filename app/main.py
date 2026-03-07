from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import router
import app.database
from fastapi.templating import Jinja2Templates

app = FastAPI(title="FitBuddy AI")
templates = Jinja2Templates(directory="templates")

# enable static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router)