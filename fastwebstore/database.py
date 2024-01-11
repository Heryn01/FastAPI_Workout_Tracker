import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASS = os.environ.get("POSTGRES_PASS")
POSTGRES_IP = os.environ.get("POSTGRES_IP")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")

URL_DATABASE = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_IP}: \
    {POSTGRES_PORT}/FastAPIWebstore"

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
