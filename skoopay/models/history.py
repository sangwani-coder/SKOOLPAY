from functools import wraps

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('history', __name__, url_prefix='/admin')

@bp.route('/history', methods=['GET', 'POST'])
def history():
    return render_template('school/history.html', session="admin")

