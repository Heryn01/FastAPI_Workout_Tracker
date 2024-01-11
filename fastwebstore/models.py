from pydantic import BaseModel

from database import Base, engine

BaseModel
Base.metadata.create_all(engine)
