from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    #Encrypt/secure cookies and session data related to website
    app.config['SECRET_KEY'] = 'hjlio6sdwapo0'
    #Define where db is located
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #Connect app with db
    db.__init__(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(blueprint= views, url_prefix= '/')
    app.register_blueprint(blueprint= auth, url_prefix= '/')
    
    from .models import User, Note
    
    create_database(app)

    return app

def create_database(app):
    with app.app_context():
        db.create_all()
        print('Created Database!')
