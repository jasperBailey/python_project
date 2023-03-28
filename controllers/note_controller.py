from flask import render_template, request, redirect, Blueprint
from repositories import note_repository
from repositories import track_repository
from models.note import Note

notes_blueprint = Blueprint("notes", __name__)

@notes_blueprint.route("/notes")
def notes():
    notes = note_repository.select_all()
    return render_template("notes/index.html", all_notes = notes)

@notes_blueprint.route('/notes/new')
def new_note():
    tracks = track_repository.select_all()
    return render_template("notes/new.html", all_tracks = tracks)

@notes_blueprint.route('/notes', methods=['POST'])
def create_note():
    pitch = request.form['pitch']
    track_id = request.form['track_id']
    duration = request.form['duration']
    location = request.form['location']
    track = track_repository.select(track_id)
    note = Note(pitch, track, duration, location)
    note_repository.save(note)
    return redirect('/notes')

@notes_blueprint.route('/notes/<index>')
def show_note(index):
    note = note_repository.select(index)
    return render_template('notes/show.html', note=note)

@notes_blueprint.route('/notes/<index>/edit')
def edit_note(index):
    note = note_repository.select(index)
    tracks = track_repository.select_all()
    return render_template('notes/edit.html', note=note, all_tracks=tracks)

@notes_blueprint.route('/notes/<index>', methods=['POST'])
def update_note(index):
    pitch = request.form['pitch']
    track_id = request.form['track_id']
    duration = request.form['duration']
    location = request.form['location']
    track = track_repository.select(track_id)
    note = Note(pitch, track, duration, location, index)
    note_repository.update(note)
    return redirect('/notes')

@notes_blueprint.route('/notes/<index>/delete', methods=['POST'])
def delete_note(index):
    note_repository.delete(index)
    return redirect('/notes')