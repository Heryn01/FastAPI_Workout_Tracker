from typing import Annotated

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

import users.models
import users.schemas


def create_user(
    db: Annotated[Session, Depends()],
    user: users.schemas.UserCreate,
):
    db_user = users.models.UserBase(
        username=user.username,
        name=user.name,
        email=user.email,
        hashed_password=user.password.get_secret_value().encode("utf-8"),
    )
    if db_user:
        if get_user_by_username(db, user.email):
            raise HTTPException(status_code=400, detail="Email already taken")
        if get_user_by_mail(db, user.email):
            raise HTTPException(status_code=400, detail="Username already taken")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return (
        db.query(users.models.UserBase)
        .filter(users.models.UserBase.id == user_id)
        .first()
    )


def get_all_users(db: Session):
    return db.query(users.models.UserBase).all()


def get_user_by_username(db: Session, user_name: str):
    return (
        db.query(users.models.UserBase)
        .filter(users.models.UserBase.username == user_name)
        .first()
    )


def get_user_by_mail(db: Session, user_mail: str):
    return (
        db.query(users.models.UserBase)
        .filter(users.models.UserBase.email == user_mail)
        .first()
    )
