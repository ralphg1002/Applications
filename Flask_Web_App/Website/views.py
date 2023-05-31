from flask import Blueprint

views = Blueprint('views', __name__)

#Decorator -> whenever accessing this url, home function is ran
@views.route('/')
def home():
    return '<h1>Test<h1>'