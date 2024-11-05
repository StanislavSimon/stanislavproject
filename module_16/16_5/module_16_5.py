from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from starlette import status

templates = Jinja2Templates(directory="homework")

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/", status_code=status.HTTP_201_CREATED)
def get_all_message(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


def get_user_by_id(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return None


@app.get("/users/{user_id}")
def get_users(request: Request, user_id: int) -> HTMLResponse:
    user = get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User  not found")
    return templates.TemplateResponse("users.html", {"request": request, "user": user})


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
