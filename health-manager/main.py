"""Rest server starts from this file.
All routes are bridged here.
"""
from fastapi import FastAPI

app = FastAPI(title="Rest API for health manager", version="0.1")


@app.get("/")
def root():
    return {"message": "Welcome to health manager API"}
