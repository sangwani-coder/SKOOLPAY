from functools import wraps

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('histry', __name__, url_prefix='/user')

@bp.route('/history', methods=['GET', 'POST'])
def history():
    return render_template('parent/history.html', session="user")

