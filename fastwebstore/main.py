from fastapi import FastAPI

from fastwebstore.route_handler import router
from fastwebstore.database import Base, engine
import users.models

Base.metadata.create_all(bind=engine)

app = FastAPI(title='projectnamehere', root_path="/api/v1")

#add all subdomain routes from the route handler
app.include_router(router)

app.mount("/api/v1", app=app)