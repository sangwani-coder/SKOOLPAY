from functools import wraps
from wtforms import Form,  validators
from wtforms import SelectField, BooleanField, StringField, PasswordField

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('account', __name__, url_prefix='/account')


class RegistrationForm(Form):
    mobile = StringField('MOMO ACCOUNT NUMBER', [validators.Length(min=4, max=25), validators.DataRequired()])
    name = StringField('ACCOUNT NAME', [validators.Length(min=6, max=35), validators.DataRequired()])
    # language = SelectField(u'Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])

@bp.route('/update', methods=['GET', 'POST'])
def update():
    form = RegistrationForm(request.form)
    return render_template('school/account.html', form=form)