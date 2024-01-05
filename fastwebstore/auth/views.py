from typing import Union, List
from uuid import uuid4
from fastapi import APIRouter
import json
from fastwebstore.models import User, Role

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

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

@router.get("/")
def read_root():
    return 'This is the authentication page. Prepare to be signed in!'

@router.post("/login")
def read_users():
    return user_db

@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}