from braindump import db
from braindump.models import note_tag


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(200))

    notes = db.relationship("Note", secondary=note_tag, backref="Tag")

    def _get_notes(self):
        return list(filter(lambda x: (
            x.author == current_user and not x.is_deleted), self.notes))
