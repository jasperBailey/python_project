from flask import render_template, request, redirect, Blueprint
from repositories import note_repository
from repositories import track_repository
from models.note import Note

notes_blueprint = Blueprint("notes", __name__)

@notes_blueprint.route("/tracks/<track_id>/notes")
def notes(track_id):
    track = track_repository.select(track_id)
    notes = note_repository.notes_in_track(track)
    notes.sort(key=lambda x: x.position)
    return render_template("notes/index.html", all_notes=notes, track=track, title=f"Edit {track.title}")

@notes_blueprint.route('/tracks/<track_id>/notes', methods=['POST'])
def create_note(track_id):
    pitch = request.form['pitch']
    duration = request.form['duration']
    position = request.form['position']
    velocity = request.form['velocity']
    track = track_repository.select(track_id)
    note = Note(pitch, track, duration, position, velocity)
    note_repository.save(note)
    return redirect(f'/tracks/{track_id}/notes')

@notes_blueprint.route('/tracks/<track_id>/notes/<note_id>', methods=['POST'])
def update_note(track_id, note_id):
    pitch = request.form['pitch']
    duration = request.form['duration']
    position = request.form['position']
    velocity = request.form['velocity']
    track = track_repository.select(track_id)
    note = Note(pitch, track, duration, position, velocity, note_id)
    note_repository.update(note)
    return redirect(f'/tracks/{track_id}/notes')

@notes_blueprint.route('/tracks/<track_id>/notes/<note_id>/delete', methods=['POST'])
def delete_note(track_id, note_id):
    note_repository.delete(note_id)
    return redirect(f'/tracks/{track_id}/notes')