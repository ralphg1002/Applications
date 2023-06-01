from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default = func.now()) #Get current time
    #Child object referencing user parent object using primary key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #ForeignKey method defines a one to many relationship

#Store user objects
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique= True) #Each user has unique email address
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #All Notes will be assigned to a user