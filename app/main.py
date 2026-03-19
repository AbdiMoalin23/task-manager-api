from fastapi import FastAPI

from app.database import engine
from app.models import Base
from app.routes import users, tasks

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message" : "Task Manager API is running"}