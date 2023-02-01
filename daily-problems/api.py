from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

daily_problem = {}

@app.get("/")
def read_root():
    return RedirectResponse(url = daily_problem["url"])

if __name__ == "__main__":
    with open("daily-problems.json", "r") as f:
        daily_problem = json.load(f)
    uvicorn.run(app, host='0.0.0.0', port=8000)