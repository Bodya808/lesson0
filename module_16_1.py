from fastapi import FastAPI

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
def user_by_id(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


# Маршруты с передачей данных через query параметры
@app.get("/user")
def user_info(username: str, age: int = None):
    if not age:
        return {"error": "Возраст является обязательным параметром."}

    return {
        "message": f'Информация о пользователе. Имя: "{username}", Возраст: {age}'
    }
