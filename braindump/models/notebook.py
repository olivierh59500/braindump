from braindump.models.shared import Base
from braindump import db


class Notebook(Base):
    __tablename__ = 'notebooks'
    title = db.Column(db.String(200))
    is_deleted = db.Column(db.Boolean, default=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    notes = db.relationship(
        'Note', backref='notebook',
        lazy='dynamic')

    def active_notes(self):
        return list(filter(lambda note: (
            not note.is_deleted and not note.is_archived), self.notes))

    def to_json(self):
        json = {
            'id': self.id,
            'title': self.title,
            'is_deleted': self.is_deleted,
            'author': self.author_id,
            'notes': list(map(lambda note: note.to_json(), self.notes.all())),
            'uri': url_for('api.notebook', notebook_id=self.id)
        }
        return json
