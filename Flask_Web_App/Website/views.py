from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

#Decorator -> whenever accessing this url, home function is ran
@views.route('/')
@login_required #Can't access home page unless logged in
def home():
    return render_template('home.html', user= current_user) #Passing current user allows ability to reference current user