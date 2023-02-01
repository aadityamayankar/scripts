from typing import Union
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import json

app = FastAPI()

daily_problem = {}
with open("daily-problems.json", "r") as f:
    daily_problem = json.load(f)

@app.get("/")
def read_root():
    return RedirectResponse(url = daily_problem["url"])