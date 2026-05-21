# Related code for task creation logic which interacts with the database.
from app.models import Task

def create_task(db, task_data):
    task = Task(
        title=task_data.title,
        description=task_data.description
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_tasks(db):
    return db.query(Task).all()

def get_task(db, task_id):
    return db.query(Task).filter(Task.id == task_id).first()

def update_task(db, task_id, task_data):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None

    for key, value in task_data.model_dump().items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    return task

def delete_task(db, task_id):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return False

    db.delete(task)
    db.commit()
    return True