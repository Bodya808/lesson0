import asyncio
import uvicorn
from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users():
    return users


@app.post("/user/{username}/{age}")
async def post_user(
        username: Annotated[str, Path(min_length=5, max_length=20,
                                      description='Enter username', example="UrbanUser")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]):
    user_id = str(len(users) + 1)
    users.update({user_id: f"Имя: {username}, возраст: {age}"})
    return f"User {len(users)} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[int, Path(title="ID пользователя")],
        username: str,
        age: int
) -> dict[str, str]:
    if user_id not in users:
        return {"error": f"User with ID {user_id} does not exist"}

    users[user_id] = f'Имя: {username}, возраст: {age}'
    return {"message": f"The user {user_id} has been updated"}


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[int, Path(description="ID удаляемого пользователя")]
) -> dict[str, str]:
    try:
        del users[user_id]
        return {"message": f"User {user_id} has been deleted"}
    except KeyError:
        return {"error": f"User with ID {user_id} does not exist"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
