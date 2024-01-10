from typing import Annotated
from uuid import uuid4
from fastapi import APIRouter, Depends, HTTPException
from fastwebstore.database import get_db
from sqlalchemy.orm import Session
from users.services import create_user, get_user_by_username
import users


router = APIRouter()

@router.get("/")
def get_user_page():
    return 'This is the user page.'

@router.get("/me")
def get_self_user():
    return 'This is your current profile information.'

@router.get("/{username}", response_model=users.schemas.UserBase)
def get_user_by_username(
    db: Annotated[Session, Depends(get_db)],
    username:str,
    ):
    db_user = get_user_by_username(db, username)
    if db_user:
        return db_user
    raise HTTPException(status_code=404, detail={'User not found'} )

@router.post('/register', response_model=users.schemas.UserBase)
def register_user(db: Annotated[Session, Depends(get_db)], 
                  user: users.schemas.UserBase
                  ):
    new_user = create_user(db, user)
    
    return new_user