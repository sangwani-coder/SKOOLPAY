import os
import re
import sys
# adding models/subfolder to the system path
sys.path.insert(0, '/mnt/e/FLASK-PROJECTS/SKOOLPAY/skoopay/')
from . helpers import apology


from flask import Blueprint, Flask, flash, g, redirect, render_template, request, session, url_for

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    # Register blueprints
    from models import auth, account, sponsor, admin, user, pay, history, histry
    app.register_blueprint(auth.bp)
    app.register_blueprint(account.bp)
    app.register_blueprint(sponsor.bp)
    app.register_blueprint(admin.bp)
    app.register_blueprint(user.bp)
    app.register_blueprint(pay.bp)
    app.register_blueprint(history.bp)
    app.register_blueprint(histry.bp)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/', methods=['GET', 'POST'])
    def homepage():
        try:
            if request.method == 'GET':
                return render_template('school/index.html', session='user_ot')
            if not request.form['schoolcode'] and not request.form["studentcode"]:
                return apology("Must provide both School and student code")

            elif not request.form.get('schoolcode'):
                return apology("Must provide School code")

            elif not request.form.get('studentcode'):
                return apology("Must provide Student code")
                
            else:
                return redirect('user/payment')
        except Exception as e:
            print(e)
 

    return app