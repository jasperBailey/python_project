from flask import render_template, request, redirect, Blueprint
from repositories import track_repository
from models.track import Track

tracks_blueprint = Blueprint("tracks", __name__)

@tracks_blueprint.route("/tracks")
def tracks():
    tracks = track_repository.select_all()
    return render_template("tracks/index.html", all_tracks = tracks)

@tracks_blueprint.route('/tracks/new')
def new_track():
    return render_template("tracks/new.html")

@tracks_blueprint.route('/tracks', methods=['POST'])
def create_track():
    title = request.form['title']
    tempo = request.form['tempo']
    track = Track(title, tempo)
    track_repository.save(track)
    return redirect('/tracks')

@tracks_blueprint.route('/tracks/<index>')
def show_track(index):
    track = track_repository.select(index)
    return render_template('tracks/show.html', track=track)

@tracks_blueprint.route('/tracks/<index>/edit')
def edit_track(index):
    track = track_repository.select(index)
    return render_template('tracks/edit.html', track=track)

@tracks_blueprint.route('/tracks/<index>', methods=['POST'])
def update_track(index):
    title = request.form['title']
    tempo = request.form['tempo']
    track = Track(title, tempo, index)
    track_repository.update(track)
    return redirect('/tracks')

@tracks_blueprint.route('/tracks/<index>/delete', methods=['POST'])
def delete_track(index):
    track_repository.delete(index)
    return redirect('/tracks')