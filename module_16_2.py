from fastapi import FastAPI, Path
from typing import Annotated

# Создаём объект приложения
app = FastAPI()


# Маршрут к главной странице
@app.get("/")
def home():
    return {"message": "Главная страница"}


# Маршрут для страницы администратора
@app.get("/user/admin")
def admin_page():
    return {"message": "Вы вошли как администратор"}


# Динамический маршрут для пользователей по user_id
@app.get("/user/{user_id}")
def user_by_id(user_id: Annotated[int, Path(..., ge=1, le=100, description="Enter User ID", example=1)]):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


# Маршрут с передачей данных через path параметры
@app.get("/user/{username}/{age}")
def user_info(
    username: Annotated[str, Path(..., min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
    age: Annotated[int, Path(..., ge=18, le=120, description="Enter age", example=24)],
):
    return {
        "message": f'Информация о пользователе. Имя: "{username}", Возраст: {age}'
    }
