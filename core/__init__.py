import os
from flask import Flask, url_for
from os import path
from flask_sqlalchemy import SQLAlchemy

# db init
db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # register bp's
    from core.main import bp as bp_main
    app.register_blueprint(bp_main)

    create_database(app)


    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Database created successfully')