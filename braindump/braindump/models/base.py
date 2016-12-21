from datetime import datetime
from braindump import db


class Base(db.Model):
    """
    Base model that includes primary key, created_date, and updated_date
    """
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
