from flask import render_template, request, redirect, Blueprint, send_from_directory
from repositories import track_repository
from models.track import Track
from helpers.track_generator import *
from os import remove
from os.path import exists

tracks_blueprint = Blueprint("tracks", __name__)

@tracks_blueprint.route("/tracks")
def tracks():
    tracks = track_repository.select_all()
    return render_template("tracks/index.html", all_tracks = tracks, title="All tracks")

@tracks_blueprint.route('/tracks/new')
def new_track():
    return render_template("tracks/new.html", title="New track")

@tracks_blueprint.route('/tracks', methods=['POST'])
def create_track():
    title = request.form['title']
    tempo = request.form['tempo']
    track = Track(title, tempo)
    track_repository.save(track)
    return redirect('/tracks')

@tracks_blueprint.route('/tracks/<id>')
def show_track(id):
    track = track_repository.select(id)
    return render_template('tracks/show.html', track=track, title=track.title)

@tracks_blueprint.route('/tracks/<id>/edit')
def edit_track(id):
    track = track_repository.select(id)
    return render_template('tracks/edit.html', track=track, title=f"Edit {track.title} details")

@tracks_blueprint.route('/tracks/<id>', methods=['POST'])
def update_track(id):
    remove_mp3(id)
    title = request.form['title']
    tempo = request.form['tempo']
    track = Track(title, tempo, id)
    track_repository.update(track)
    return redirect('/tracks/'+str(id))

@tracks_blueprint.route('/tracks/<id>/delete', methods=['POST'])
def delete_track(id):
    remove_mp3(id)
    track_repository.delete(id)
    return redirect('/tracks')

@tracks_blueprint.route('/tracks/<id>/generate')
def gen_track(id):
    track = track_repository.select(id)
    generate_track_mp3(track)
    return render_template('tracks/download.html', track=track, title=f"Play {track.title}")

@tracks_blueprint.route('/tracks/<id>/download')
def download_track(id):
    track = track_repository.select(id)
    filename = track.title + ".mp3"
    return send_from_directory('out/', filename)

def remove_mp3(track_id):
    track = track_repository.select(track_id)
    if exists(f"out/{track.title}.mp3"):
        remove(f"out/{track.title}.mp3")