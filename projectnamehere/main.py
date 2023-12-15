from typing import Union, List
from uuid import uuid4
from fastapi import FastAPI
import json
from models import User, Role

app = FastAPI(title='projectnamehere', root_path="/api/v1")

user_db: List[User] = [
    User(
        id=uuid4(),
        first_name = 'Emert',
        middle_name = 'Emert',
        last_name  = 'Dington',
        twilight_team = 'Edward',
        role = [Role.user]
    ),
    User(
        id=uuid4(),
        first_name = 'Tim',
        middle_name = 'Tom',
        last_name  = 'Tomington',
        role = [Role.user]
    ),
]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/users")
def read_users():
    return user_db

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}




app.mount("/api/v1", app=app)