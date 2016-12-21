from datetime import datetime

from braindump import db
from braindump.models.shared import Base
from braindump.models.tag import Tag
from braindump.models import note_tag
from flask_sqlalchemy import BaseQuery
from sqlalchemy_searchable import SearchQueryMixin
from sqlalchemy_utils.types import TSVectorType


class NoteQuery(BaseQuery, SearchQueryMixin):
    pass


class Note(Base):
    query_class = NoteQuery
    __tablename__ = 'notes'
    title = db.Column(db.String(200))
    body = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    notebook_id = db.Column(db.Integer, db.ForeignKey('notebooks.id'))
    is_deleted = db.Column(db.Boolean, default=False)
    is_favorite = db.Column(db.Boolean, default=False)
    is_archived = db.Column(db.Boolean, default=False)

    tags = db.relationship(
        "Tag", secondary=note_tag,
        backref="Note", passive_deletes=True)

    # Full Text Search
    search_vector = db.Column(TSVectorType('title', 'body'))

    def to_json(self):
        json_note = {
            'id': self.id,
            #'url': url_for('api.get_note', id=self.id, _external=True),
            'body': self.body,
            #'created_date': self.created_date,
            'author': self.author_id,
        }
        return json_note

    def get_notebook(self, id):
        notebook = Notebook.query.filter_by(
            id=id).first()
        return notebook

    @staticmethod
    def from_json(json_post):
        body = json_post.get('body')
        if body is None or body == '':
            raise ValidationError('note does not have a body')
        return Note(body=body)

    def _find_or_create_tag(self, tag):
        q = Tag.query.filter_by(tag=tag)
        t = q.first()
        if not (t):
            t = Tag(tag=tag.strip())
        return t

    def _get_tags(self):
        return [x.tag for x in self.tags]

    def _set_tags(self, value):
        while self.tags:
            del self.tags[0]
        for tag in value:
            self.tags.append(self._find_or_create_tag(tag))

    # simple wrapper for tags relationship
    str_tags = property(_get_tags,
                        _set_tags)
