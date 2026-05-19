# Related code for task creation logic which interacts with the database.
from app.models import Task

def create_task(db, task_data):
    # Creates SQLAlchemy model object
    task = Task(
        title=task_data.title,
        description=task_data.description
    )

    # Tells SQLAlchemy to add the new task to db session, then commit it. Finally refresh after commit.
    db.add(task)
    db.commit()
    db.refresh(task)

    return task