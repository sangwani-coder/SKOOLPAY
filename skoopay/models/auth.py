from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods =['GET','POST'])
def login():
    return render_template('auth/login.html')

@bp.route('/sign', methods=('GET', 'POST'))
def sign():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # # db = get_db()
        # error = None

        # if not username:
        #     error = 'Username is required.'
        # elif not password:
        #     error = 'Password is required.'

        # if error is None:
        #     try:
        #         db.execute(
        #             "INSERT INTO user (username, password) VALUES (?, ?)",
        #             (username, generate_password_hash(password)),
        #         )
        #         db.commit()
        #     except db.IntegrityError:
        #         error = f"User {username} is already registered."
        #     else:
        #         return redirect(url_for("auth.login"))

        # flash(error)

    return render_template('auth/register.html')

""" Authentication routes For both schools and parent """

@bp.route('/logout') # Logout route
def logout():
    try:
        return redirect('/')
    except Exception as e:
        print(e)
    
@bp.route('/register', methods = ['GET', 'POST']) # signup parent
def register():
    try:
        if request.method =='GET':
            return render_template('auth/register.html')
        return render_template('auth/login.html')
    except Exception as e:
        print(e)

@bp.route('/signup', methods = ['GET', 'POST']) # Signup school
def signup():
    try:
        if request.method =='GET':
            return render_template('auth/signup.html')
        return render_template('auth/login.html')

    except Exception as e:
        print(e)