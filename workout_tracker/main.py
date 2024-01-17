import uvicorn
from fastapi import FastAPI

from workout_tracker.route_handler import router

app = FastAPI(title="projectnamehere", root_path="/api/v1")

# add all subdomain routes from the route handler
app.include_router(router)

app.mount("/api/v1", app=app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
