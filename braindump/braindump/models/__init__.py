from braindump import db
from sqlalchemy_searchable import make_searchable

make_searchable()

"""
Association Table to resolve M:M Relationship between
Note and Tag
"""
note_tag = db.Table(
    'note_tag',
    db.Column(
        'note_id',
        db.Integer,
        db.ForeignKey('notes.id', ondelete="CASCADE")),
    db.Column(
        'tag_id',
        db.Integer,
        db.ForeignKey('tags.id', ondelete="CASCADE")))
