from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

#Decorator -> whenever accessing this url, home function is ran
@views.route('/', methods= ['GET', 'POST'])
@login_required #Can't access home page unless logged in
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        
        if len(note) < 1:
            flash('Note is too short!', category= 'error')
        else:
            new_note = Note(data= note, user_id= current_user.id)
            #Add note to db
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category= 'success')
            
    return render_template('home.html', user= current_user) #Passing current user allows ability to reference current user

@views.route('/delete-note', methods= ['POST'])
def delete_note():
    #Take in data from POST request and load it in as a json object/python dictionary
    note = json.loads(request.data)
    #Access noteId attribute (from index file)
    noteId = note['noteId']
    #Look for noteId
    note = Note.query.get(noteId)
    #Check if note exists
    if note:
        #Then check if user that is signed in owns that note
        if note.user_id == current_user.id:
            #Now delete note
            db.session.delete(note)
            db.session.commit()
            
    #Return empty response as json object -> required for flask*
    return jsonify({})
            