from fastapi import Depends
from database import engine, SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
import users.schemas
import users.models


def create_user(db: Annotated[Session, Depends()], user: users.schemas.UserBase):
    db_user = users.models.UserBase(username = user.username, name = user.name, email = user.email, hashed_password = user.password.get_secret_value())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(users.models.UserBase).filter(users.models.UserBase.id == user_id).first()

def get_user_by_username(db: Session, user_name: str):
    return db.query(users.models.UserBase).filter(users.models.UserBase.username == user_name).first()