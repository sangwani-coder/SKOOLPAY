import os

from flask import (
    Blueprint, Flask, flash, g, redirect, render_template, request, session, url_for
)

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    # Register blueprints
    from . import auth, account, sponsor, admin, user
    app.register_blueprint(auth.bp)
    app.register_blueprint(account.bp)
    app.register_blueprint(sponsor.bp)
    app.register_blueprint(admin.bp)
    app.register_blueprint(user.bp)

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

    @app.route('/')
    def homepage():
        return render_template('school/index.html')
 

    return app