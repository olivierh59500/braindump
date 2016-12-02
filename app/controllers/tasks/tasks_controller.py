from flask import render_template, \
    redirect, request, url_for, flash, jsonify
from flask_login import login_user, \
    logout_user, login_required, current_user

from app import db
from app.models import User
from app.model.tasks import Task
from app.controllers.tasks import tasks

@tasks.route('/')
@login_required
def show_tasks():
    tasks = current_user.tasks.all()
    return str(tasks)

@tasks.route('/add')
@login_required
def add_task():
    