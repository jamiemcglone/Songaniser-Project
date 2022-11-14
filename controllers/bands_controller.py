from flask import Blueprint, Flask, redirect, render_template, request
from repositories import band_repository, setlist_repository, setlist_song_repository, song_repository
import pdb

bands_blueprint = Blueprint("bands", __name__)

@bands_blueprint.route("/bands")
def bands():
    bands = band_repository.select_all()
    setlists = setlist_repository.select_all()
    songs = setlist_song_repository.select_all()
    return render_template("bands/index.html", bands=bands, setlists=setlists, setlist_songs=songs)

@bands_blueprint.route("/bands/<id>")
def band_view():
    band_to_view = band_repository.select(id)
    return render_template("")