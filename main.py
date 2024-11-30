from fastapi import FastAPI
from app.routers import task, user
import uvicorn
import asyncio

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router)
app.include_router(user.router)
