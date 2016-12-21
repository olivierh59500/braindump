from braindump import db
from braindump.models.base import Base


class SharedNote(Base):
    """Model that keeps a record of shared notes"""
    __tablename__ = 'shared_notes'
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    note_id = db.Column(db.Integer, db.ForeignKey('notes.id'))
    recipient_email = db.Column(db.String(254))
