from fastapi import FastAPI, Path


app = FastAPI()

users = {"1": "Имя:Example, возраст: 18"}


@app.get("/users")
async def get_users():
    return users

@app.post("/user/{username}/{age}")
async def post_users(username: str, age: int):
    current_id = str(int(max(users, key=str)))
    user_id = str(int(current_id) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def put_users(user_id: str, username: str, age: int):
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"The user {user_id} has been updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    users.pop(user_id)
    return f"The user {user_id} is deleted!"
