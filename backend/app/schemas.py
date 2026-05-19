# Schema Section for task creation
# This section defines the Pydantic model for task creation, which will be used to validate incoming data when creating a new task. It ensures that the required fields are present and of the correct type.
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str



    