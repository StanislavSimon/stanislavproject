from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def start_page() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin_page() -> dict:
    return {"message":f"Вы вошли как администратор!"}

@app.get("/user/{user_id}")
async def user_id_page(user_id = int) -> dict:
    return {"message":f"Вы вошли как пользователь №, {user_id}"}

@app.get("/user")
async def user_info(username:str, age:int) -> dict:
    return {"message":f"Информация о пользователе. Имя:{username}, Возраст:{age}"}