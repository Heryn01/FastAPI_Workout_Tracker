from database import Base, engine
from pydantic import BaseModel

BaseModel
Base.metadata.create_all(engine)
