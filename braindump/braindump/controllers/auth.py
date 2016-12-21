from braindump import db
from braindump.forms.auth import LoginForm, RegistrationForm
from braindump.models.notebook import Notebook
from braindump.models.user import User
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(
            email=form.email.data.lower().strip()).first()
        if user is not None and user.verify_password(form.password.data):
            user.log_login()
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('dashboard.index'))
        flash('Invalid username or password', 'error')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('dashboard.index'))


@auth.route('/regsiter', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data.lower().strip()
        password = form.password.data

        # Check if user is already registered and attempt to log them in
        user = User.query.filter_by(email=email).first()
        if user:
            if user.verify_password(password):
                login_user(user)
                return redirect(
                    request.args.get('next') or url_for('dashboard.index'))
            flash('Invalid username or password')
            return redirect(url_for('hodashboardme.index'))

        # Register user
        user = User(
            email=email,
            password=password,
            confirmed=True)
        db.session.add(user)
        db.session.commit()
        default_notebook = Notebook(
            title='default', author_id=user.id
        )
        db.session.add(default_notebook)
        db.session.commit()
        user.default_notebook = default_notebook.id
        db.session.commit()
        return redirect(url_for('dashboard.index'))
    return render_template('auth/register.html', form=form)
