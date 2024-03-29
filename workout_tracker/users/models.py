from database import Base, engine
from sqlalchemy import Column, Integer, String


class UserBase(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), index=True)
    name = Column(String(50), index=True, nullable=False)
    email = Column(String(320), index=True, unique=True)
    hashed_password = Column(String)


Base.metadata.create_all(engine)
