from flask import Blueprint, redirect, render_template, request
from repositories import band_repository, song_repository
from models.song import Song

songs_blueprint = Blueprint("songs", __name__)

@songs_blueprint.route("/songs")
def songs():
    songs = song_repository.select_all()
    return render_template("songs/index.html", songs=songs)

@songs_blueprint.route("/songs/<id>")
def song_view(id):
    song_to_view = song_repository.select(id)
    return render_template("songs/view.html", song=song_to_view)


@songs_blueprint.route("/songs/new")
def new_song():
    bands = band_repository.select_all()
    return render_template("songs/new.html", bands=bands)


@songs_blueprint.route("/songs", methods=["POST"])
def create_song():
    title = request.form['title']
    artist = request.form['artist']
    duration = request.form['duration']
    song_key = request.form['key']
    structure = request.form['structure']
    harmony = request.form['harmony']
    notes = request.form['notes']
    band = band_repository.select(request.form['band'])
    new_song = Song(title, artist, duration, song_key, 
    structure, harmony, False, notes, band)
    song_repository.save(new_song)
    return redirect("/songs")

@songs_blueprint.route("/songs/<id>/delete", methods=['POST'])
def delete_song(id):
    song_repository.delete(id)
    return redirect("/songs")

@songs_blueprint.route("/songs/<id>/edit")
def edit_song(id):
    song_to_edit = song_repository.select(id)
    bands = band_repository.select_all()
    return render_template("/songs/edit.html", song=song_to_edit, bands=bands)

@songs_blueprint.route("/songs/<id>", methods=["POST"])
def update_song(id):
    title = request.form['title']
    artist = request.form['artist']
    duration = request.form['duration']
    song_key = request.form['key']
    structure = request.form['structure']
    harmony = request.form['harmony']
    notes = request.form['notes']
    band = band_repository.select(request.form['band'])
    song = Song(title, artist, duration, song_key, 
    structure, harmony, False, notes, band, id)
    song_repository.update(song)
    return redirect("/songs")

@songs_blueprint.route("/songs/<id>/learned", methods=['POST'])
def update_learned_status(id):
    song_to_update = song_repository.select(id)
    song_to_update.update_learned_status()
    song_repository.update(song_to_update)
    return redirect("/songs")