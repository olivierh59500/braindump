from flask import Blueprint, render_template, current_app
from flask_login import current_user, login_required
from braindump.models.user import User
from braindump.models.note import Note

dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('dashboard/index.html')
    else:
        stats = {
            'users': User.query.count(),
            'notes': Note.query.count()
        }
        return render_template('home.html', stats=stats)


@dashboard.route('/settings')
@login_required
def settings():
    version = current_app.config['BRAINDUMP_VERSION']
    return render_template('dashboard/settings.html', version=version)
