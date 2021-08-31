from functools import wraps
from wtforms import Form,  validators
from wtforms import SelectField, BooleanField, StringField, PasswordField

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('sponsor', __name__, url_prefix='/admin')

@bp.route('/sponsors', methods=['GET', 'POST'])
def sponsor():
    return render_template('school/sponsor.html', session='admin')