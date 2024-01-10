from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class UserBase(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), index=True)
    name = Column(String(50), index = True, nullable=False)
    email = Column(String(320), index = True, unique=True)
    hashed_password = Column(String)
