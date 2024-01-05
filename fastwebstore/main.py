from typing import Union, List
from uuid import uuid4
from fastapi import FastAPI
import json
from fastwebstore.models import User, Role
from fastwebstore.route_handler import router 

app = FastAPI(title='projectnamehere', root_path="/api/v1")
app.include_router(router)






app.mount("/api/v1", app=app)