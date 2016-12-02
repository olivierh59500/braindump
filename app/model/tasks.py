import enum 
from datetime import datetime

from app import db
from app.model.base import Base


class TaskPriority(enum.Enum):
    p0 = 0
    p1 = 1
    p2 = 2


class TaskStatus(enum.Enum):
    s0 = "Pending"
    s1 = "In Progress"
    s2 = "Doing"
    s3 = "Blocked"
    s4 = "Done"
    

class Task(Base):
    """ Tasks that are related to a note """
    __tablename__ = 'tasks'
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    note_id = db.Column(db.Integer, db.ForeignKey('notes.id'))
    title = db.Column(db.String)
    priority = db.Column(db.Enum(TaskPriority))
    status = db.Column(db.Enum(TaskStatus))
    due_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)