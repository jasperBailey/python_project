from flask import render_template, request, redirect, Blueprint
from repositories import note_repository
from repositories import track_repository

notes_blueprint = Blueprint("notes", __name__)

@notes_blueprint.route("/tracks/<track_id>/notes")
def notes(track_id):
    track = track_repository.select(track_id)
    notes = note_repository.notes_in_track(track)
    return render_template("notes/index.html", all_notes=notes, track=track)

# @notes_blueprint.route('/tracks/<track_id>/notes/new')
# def new_note():
#     tracks = track_repository.select_all()
#     return render_template("notes/new.html", all_tracks = tracks)

# @notes_blueprint.route('/tracks/<track_id>/notes', methods=['POST'])
# def create_note():
#     pitch = request.form['pitch']
#     track_id = request.form['track_id']
#     duration = request.form['duration']
#     location = request.form['location']
#     track = track_repository.select(track_id)
#     note = Note(pitch, track, duration, location)
#     note_repository.save(note)
#     return redirect('/notes')

# @notes_blueprint.route('/tracks/<track_id>/notes/<note_id>/edit')
# def edit_note(note_id):
#     note = note_repository.select(note_id)
#     tracks = track_repository.select_all()
#     return render_template('notes/edit.html', note=note, all_tracks=tracks)

# @notes_blueprint.route('/tracks/<track_id>/notes/<note_id>', methods=['POST'])
# def update_note(note_id):
#     pitch = request.form['pitch']
#     track_id = request.form['track_id']
#     duration = request.form['duration']
#     location = request.form['location']
#     track = track_repository.select(track_id)
#     note = Note(pitch, track, duration, location, note_id)
#     note_repository.update(note)
#     return redirect('/notes')

# @notes_blueprint.route('/tracks/<track_id>/notes/<note_id>/delete', methods=['POST'])
# def delete_note(note_id):
#     note_repository.delete(note_id)
#     return redirect('/notes')