from flask import Blueprint, Flask, redirect, render_template, request
from repositories import band_repository, song_repository, setlist_repository

bands_blueprint = Blueprint("bands", __name__)

@bands_blueprint.route("/bands")
def bands():
    bands = band_repository.select_all()
    songs = song_repository.select_all()
    return render_template("bands/index.html", bands=bands, songs=songs)