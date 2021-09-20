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
        schools = {'Shalom School':'2021', 'Elim':'2022', 'Jack':'2023'}


        shalom = ['2030', 'Taonga Hara', 'Shalom Christian School', '2300', 'Grade 6']
        elim = ['2030', 'Taonga Banda', 'Elim School', '2300', 'Grade 7']
        jack = ['2030', 'Tembo Banda', 'Jack School', '2300', 'Grade 2']
         
        try:
            if request.method == 'GET':
                return render_template('school/index.html', session='user_ot')
            if not request.form['schoolcode'] and not request.form["studentcode"]:
                return apology("Must provide both School and student code")

            elif not request.form.get('schoolcode'):
                return apology("Must provide School code")

            elif not request.form.get('studentcode'):
                return apology("Must provide Student code")

            elif request.form.get('schoolcode') == schools['Shalom School'] and request.form.get('studentcode') == '2030':
                
                return render_template('parent/pay.html', std = shalom)

            elif request.form.get('schoolcode') == schools['Elim'] and request.form.get('studentcode') == '2030':
                return render_template('parent/pay.html', std = elim)

            elif request.form.get('schoolcode') == schools['Jack'] and request.form.get('studentcode') == '2030':
                return render_template('parent/pay.html', std = jack)
            else:
                return apology("No records found")
        except Exception as e:
            print(e)
 

    return app