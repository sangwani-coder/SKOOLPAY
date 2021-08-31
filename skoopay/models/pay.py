from functools import wraps

from werkzeug.utils import send_file

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('payment', __name__, url_prefix='/user')

@bp.route('/payment', methods=['GET', 'POST'])
def payment():
    return render_template('parent/pay.html', session='user')