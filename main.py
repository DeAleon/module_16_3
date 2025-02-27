from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/')
async def home() -> str:
    return 'Главная страница'


@app.get('/user')
async def get_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def user_id(username: str = Path(min_length=5, max_length=20,description='Enter username', example='UrbanUser'),
                  age: int = Path(ge=18, le=120, description='Enter age', example='24')) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    new_user = {current_index: f'Имя: {username}, возраст: {age}'}
    users.update(new_user)
    return f'User {current_index} is registered'

@app.put('/user/{user_id}/{username}/{age})')
async def update_users(user_id: int = Path(ge=1, le=100, description='Enter id', example='2'),
                       username: str = Path(min_length=5, max_length=20,description='Enter username', example='UrbanUser'),
                       age: int = Path(ge=18, le=120, description='Enter age', example='24')) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"The user {user_id} is updated"

@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f'User {user_id} has been deleted'
