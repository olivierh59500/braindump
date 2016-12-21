import hashlib
from datetime import datetime

from braindump import db, login_manager, login_manager
from braindump.models.note import Note
from braindump.models.notebook import Notebook
from braindump.models.base import Base
from braindump.models.shared import SharedNote
from flask import current_app, jsonify, url_for
from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, Base):
    __tablename__ = 'users'
    email = db.Column(db.String(254), unique=True, index=True)
    password_hash = db.Column(db.String(256))
    confirmed = db.Column(db.Boolean, default=False)
    avatar_hash = db.Column(db.String(32))
    last_login_date = db.Column(db.DateTime(), default=datetime.utcnow)
    default_notebook = db.Column(db.Integer)

    notes = db.relationship(
        'Note', backref='author',
        lazy='dynamic', cascade="all, delete-orphan")
    notebooks = db.relationship(
        'Notebook', backref='author',
        lazy='dynamic', cascade="all, delete-orphan")
    shared_notes = db.relationship(
        'SharedNote', backref="author",
        lazy="dynamic", cascade="all, delete-orphan")

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.email is not None and self.avatar_hash is None:
            self.avatar_hash = hashlib.md5(
                self.email.encode('utf-8')).hexdigest()

    def get_deleted_notes(self):
        """ Return all notes owned by this user that are in the trash."""
        return list(filter(lambda note: note.is_deleted, self.notes))

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(
            password,
            method='pbkdf2:sha512')

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def generate_reset_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id})

    def reset_password(self, token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('reset') != self.id:
            return False
        self.password = new_password
        db.session.add(self)
        db.session.commit()
        return True

    def generate_email_change_token(self, new_email, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'change_email': self.id, 'new_email': new_email})

    def change_email(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('change_email') != self.id:
            return False
        new_email = data.get('new_email')
        if new_email is None:
            return False
        if self.query.filter_by(email=new_email).first() is not None:
            return False
        self.email = new_email
        self.avatar_hash = hashlib.md5(
            self.email.encode('utf-8')).hexdigest()
        db.session.add(self)
        db.session.commit()
        return True

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        db.session.commit()
        return True

    def generate_auth_token(self):
        s = Serializer(
            current_app.config['SECRET_KEY'],
            expires_in=3600)
        return s.dumps({'id': self.id})

    def log_login(self):
        self.last_login_date = datetime.utcnow()
        db.session.add(self)
        db.session.commit()
        return None


class AnonymousUser(AnonymousUserMixin):

    def can(self):
        return False

    def is_administrator(self):
        return False
