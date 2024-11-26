from fastapi import FastAPI
from app.routers import task as task_router
from app.routers import user as user_router
import uvicorn
import asyncio


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task_router)
app.include_router(user_router)


if __name__ == "main":
    asyncio.run(uvicorn.run(app, host="127.0.0.1", port=8000, loop="asyncio"))