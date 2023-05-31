from flask import Blueprint, render_template

views = Blueprint('views', __name__)

#Decorator -> whenever accessing this url, home function is ran
@views.route('/')
def home():
    return render_template('home.html')