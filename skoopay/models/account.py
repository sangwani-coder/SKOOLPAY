from functools import wraps

from werkzeug.utils import send_file
from wtforms import Form,  validators
from wtforms import SelectField, BooleanField, StringField, PasswordField

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('account', __name__, url_prefix='/admin')


class RegistrationForm(Form):
    TITLES = [(' '),('Mr.'),('Mrs.'),('Ms.'),('Dr.'),('Other.') ]
    GRADES = [(' '),('Day care'),('Pre'), ('G1'),('G2'),('G3'),]
    title = SelectField(u'Title', choices=TITLES)
    firstname = StringField('First name:', [validators.Length(min=6, max=35), validators.DataRequired()])
    surname = StringField('Surname:', [validators.Length(min=6, max=35), validators.DataRequired()])
    email = StringField('Email:', [validators.Length(min=4, max=25), validators.DataRequired()])
    mobile = StringField('Tel:', [validators.Length(min=4, max=25), validators.DataRequired()])
    grade = SelectField(u'Class:', choices=GRADES)
    beneficially_1 = StringField('BENEFICIALLY 1:', [validators.Length(min=6, max=35), validators.DataRequired()])
    beneficially_2 = StringField('BENEFICIALLY 2:', [validators.Length(min=6, max=35), validators.DataRequired()])
    beneficially_3 = StringField('BENEFICIALLY 3:', [validators.Length(min=6, max=35), validators.DataRequired()])
    beneficially_4 = StringField('BENEFICIALLY 4:', [validators.Length(min=6, max=35), validators.DataRequired()])

@bp.route('/account', methods=['GET', 'POST'])
def update():
    form = RegistrationForm(request.form)
    return render_template('school/account.html', session='admin', form=form)