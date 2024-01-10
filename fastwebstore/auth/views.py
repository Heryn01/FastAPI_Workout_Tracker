from typing import Union, List
from uuid import uuid4
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer
import json

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

@router.get("/")
def get_auth_page():
    return 'This is the authentication page. Prepare to be signed in!'