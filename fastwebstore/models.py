from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class Twilight(str, Enum):
    edward = "Edward"
    jacob = "Jacob"

class Role(str, Enum):
    admin = 'admin'
    user = 'user'
    
class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    twilight_team: Optional[Twilight] = None
    role: List[Role]
    
class HTTPException(BaseModel):
    detail: str
    error_code: Optional[str]