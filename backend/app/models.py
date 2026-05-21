# SQLAlchemy model for Task Table
# This section defines the SQLAlchemy model for the Task table in the database.

from sqlalchemy import Column, Integer, String
from app.connection import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
