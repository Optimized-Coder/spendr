import os
from flask import Flask, url_for
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# db init
db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # register bp's
    from core.main import bp as bp_main
    app.register_blueprint(bp_main)

    from core.auth import bp as bp_auth
    app.register_blueprint(bp_auth, url_prefix='/auth/')


    from .models import User

    create_database(app)


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)


    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Database created successfully')