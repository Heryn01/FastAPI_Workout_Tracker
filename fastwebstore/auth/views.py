from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from database import get_db
from users.schemas import UserBase

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/")
def get_auth_page():
    return "This is the authentication page. Prepare to be signed in!"


@router.post("/login")
def login_user(db: Annotated[Session, Depends(get_db)], user: UserBase):
    return "This is the authentication page. Prepare to be signed in!"
