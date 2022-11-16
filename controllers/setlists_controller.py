from flask import Blueprint, Flask, redirect, render_template, request
from repositories import setlist_repository, song_repository, band_repository, setlist_song_repository
from models.setlist import Setlist
from models.setlist_song import Setlist_song

setlists_blueprint = Blueprint("setlists", __name__)

@setlists_blueprint.route("/setlists")
def setlists():
    setlists = setlist_repository.select_all()
    return render_template("setlists/index.html", setlists=setlists)

@setlists_blueprint.route("/setlists/<id>")
def setlist_view(id):
    setlist_to_view = setlist_repository.select(id)
    setlist_songs = setlist_repository.get_songs_in_set(setlist_to_view)
    return render_template("setlists/view.html", setlist=setlist_to_view, setlist_songs=setlist_songs)


@setlists_blueprint.route("/setlists/new")
def new_setlist():
    songs = song_repository.select_all()
    bands = band_repository.select_all()
    return render_template("setlists/new.html", bands=bands, songs=songs)


@setlists_blueprint.route("/setlists", methods=["POST"])
def create_setlist():
    name = request.form['setlist_name']
    band = band_repository.select(request.form['band'])
    new_setlist = Setlist(name, band)
    setlist_repository.save(new_setlist)
    return redirect("/setlists")

@setlists_blueprint.route("/setlists/<id>/delete", methods=['POST'])
def delete_setlist(id):
    setlist_repository.delete(id)
    return redirect("/setlists")

@setlists_blueprint.route("/setlists/songs/<id>")
def song_view(id):
    song_to_view = song_repository.select(id)
    return render_template("songs/view.html", song=song_to_view)

@setlists_blueprint.route("/setlists/<id>/edit")
def edit_setlist(id):
    bands = band_repository.select_all()
    all_songs = song_repository.select_all()
    setlist_to_edit = setlist_repository.select(id)
    songs_in_set = setlist_repository.get_songs_in_set(setlist_to_edit)

    song_ids = []
    for song in songs_in_set:
        song_ids.append(song.id)
    
    songs_to_display = []
    for song in all_songs:
        if song.id not in song_ids:
            songs_to_display.append(song)
    return render_template("setlists/edit.html", setlist=setlist_to_edit, bands=bands, songs=songs_to_display)

@setlists_blueprint.route("/setlists/<id>", methods=["POST"])
def update_setlist(id):
    name = request.form["setlist_name"]
    band = band_repository.select(request.form["band"])
    songs_to_add = request.form.getlist("songs")
    setlist = Setlist(name, band, id)
    setlist_repository.update(setlist)

    songs_in_set = setlist_repository.get_songs_in_set(setlist)
    for song_id in songs_to_add:
        song_object = song_repository.select(song_id)
        setlist_song = Setlist_song(setlist, song_object)
        if song_object in songs_in_set:
            continue
        else:
            setlist_song_repository.save(setlist_song)
            
    setlist_to_view = setlist_repository.select(id)
    setlist_songs = setlist_repository.get_songs_in_set(setlist_to_view)
    return render_template("setlists/view.html", setlist=setlist_to_view, setlist_songs=setlist_songs)

@setlists_blueprint.route("/setlists/<set_id>/songs/<song_id>/delete", methods=["POST"])
def remove_song_from_set(set_id, song_id):
    setlist_songs = setlist_song_repository.select_all()
    for song in setlist_songs:
        if song.song.id == int(song_id) and song.setlist.id == int(set_id):
            setlist_song_repository.delete(song.id)
    setlist_to_view = setlist_repository.select(set_id)
    setlist_songs = setlist_repository.get_songs_in_set(setlist_to_view)
    return render_template("setlists/view.html", setlist=setlist_to_view, setlist_songs=setlist_songs)