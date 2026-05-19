from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.connection import get_db 
from app.schemas import TaskCreate
from app.controllers import create_task

router = APIRouter()

# On POST request, JSON body is parsed into TaskCreate Pydantic model, then passed to controller. 
@router.post("/tasks")
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)