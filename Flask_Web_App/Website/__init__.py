from flask import Flask

def create_app():
    app = Flask(__name__)
    #Encrypt/secure cookies and session data related to website
    app.config['SECRET_KEY'] = 'hjlio6sdwapo0'

    from .views import views
    from .auth import auth

    app.register_blueprint(blueprint= views, url_prefix= '/')
    app.register_blueprint(blueprint= auth, url_prefix= '/')

    return app


