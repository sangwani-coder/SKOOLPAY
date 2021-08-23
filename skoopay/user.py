from functools import wraps

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard/dash_1.html', session="user")

