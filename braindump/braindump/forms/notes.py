# -*- coding: utf-8 -*-
"""
    braindump.forms.notes
    ~~~~~~~~~~~~~~~~~~~~

    Forms used for working with notes

"""
from braindump.models.user import Note
from flask_wtf import FlaskForm
from wtforms import (SubmitField, SelectField, TextAreaField)
from wtforms.validators import EqualTo, Length, Regexp, Required


class NoteForm(FlaskForm):
    body = TextAreaField()
    notebook = SelectField(coerce=int)
    submit = SubmitField('Add Note')
