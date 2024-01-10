from pydantic import BaseModel, SecretStr, EmailStr

class UserBase(BaseModel):
    username: str
    name: str | None
    email: EmailStr
    password: SecretStr
