from pydantic import BaseModel, EmailStr, SecretStr


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    name: str | None
    password: SecretStr


class User(UserBase):
    id: int
