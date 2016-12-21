from datetime import datetime

import html
from braindump import db
from braindump.forms.notes import NoteForm
from braindump.models.note import Note
from braindump.models.notebook import Notebook
from flask import (Blueprint, current_app, redirect, render_template, request,
                   url_for)
from flask_login import current_user, login_required

notes = Blueprint('notes', __name__)


@notes.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.args.get('notebook'):
        notebook = Notebook.query.filter_by(
            id=int(request.args.get('notebook'))).first()
        form = NoteForm(notebook=notebook.id)
    else:
        form = NoteForm()
    form.notebook.choices = [
        (n.id, n.title) for n in
        Notebook.query.filter_by(
            author_id=current_user.id, is_deleted=False).all()]
    if form.validate_on_submit():

        # Parse title from note
        # The title is the first line of the note
        # If the first line is blank we use the current date instead
        title = html.escape(form.body.data.split('\r\n')[0])
        if len(title.strip()) == 0:
            title = datetime.utcnow()

        note = Note(
            title=title,
            body=form.body.data,
            notebook_id=form.notebook.data,
            author_id=current_user.id)
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('dashboard.index', id=note.notebook_id))
    return render_template('notes/add.html', form=form)
