from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.connection import get_db 
from app.schemas import TaskCreate
from app.services import create_task, delete_task, get_tasks, get_task, update_task

router = APIRouter()

# On POST request, JSON body is parsed into TaskCreate Pydantic model, then passed to controller. 
@router.post("/tasks")
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)

@router.get("/tasks")
def get_all_tasks(db: Session = Depends(get_db)):
    return get_tasks(db)

@router.get("/tasks/{task_id}")
def get_single_task(task_id: int, db: Session = Depends(get_db)):
    task = get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}")
def update_single_task(task_id: int, task_data: TaskCreate, db: Session = Depends(get_db)):
    task = update_task(db, task_id, task_data)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/tasks/{task_id}")
def delete_single_task(task_id: int, db: Session = Depends(get_db)):
    result = delete_task(db, task_id)
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    else:
        return {"message": "Task deleted"}