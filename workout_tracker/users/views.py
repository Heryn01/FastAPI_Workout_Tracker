from typing import Annotated

import users
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from users.services import (create_user, get_all_users, get_user_by_mail,
                            get_user_by_username)

from workout_tracker.database import get_db

router = APIRouter()


@router.get("/")
def get_user_page():
    return "This is the user page."


@router.get("/me")
def get_self_user():
    return "This is your current profile information."


@router.get("/username/{username}", response_model=users.schemas.UserBase)
def get_user_by_name(
    db: Annotated[Session, Depends(get_db)],
    username: str,
):
    db_user = get_user_by_username(db, username)
    if db_user:
        return db_user
    raise HTTPException(status_code=404, detail={"msg": "No user found."})


@router.get("/email/{email}", response_model=users.schemas.UserBase)
def get_user_by_email(
    db: Annotated[Session, Depends(get_db)],
    email: str,
):
    db_user = get_user_by_mail(db, email)
    if db_user:
        return db_user
    else:
        raise HTTPException(status_code=404, detail={"msg": "No user found."})


@router.get("/all")
def get_users(
    db: Annotated[Session, Depends(get_db)],
):
    db_user = get_all_users(db)
    if db_user:
        return db_user
    raise HTTPException(status_code=404, detail={"msg": "No users found."})


@router.post("/register")
def register_user(
    db: Annotated[Session, Depends(get_db)], user: users.schemas.UserCreate
):
    new_user = create_user(db, user)

    return new_user
