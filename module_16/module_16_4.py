from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

def get_user_by_id(user_id):
    for user in users:
        if user.id == user_id:
            return user
    return None

@app.get("/users")
def get_users():
    return users

@app.post("/user/{username}/{age}")
def create_user(username: str, age: int):
    if users:
        user_id = users[-1].id + 1
    else:
        user_id = 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user

@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: int, username: str, age: int):
    user = get_user_by_id(user_id)
    if user:
        user.username = username
        user.age = age
        return user
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    user = get_user_by_id(user_id)
    if user:
        users.remove(user)
        return user
    raise HTTPException(status_code=404, detail="User was not found")
