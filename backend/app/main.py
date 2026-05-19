from fastapi import FastAPI
from app.routes import router as task_router

from app.connection import engine
from app.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(task_router)

