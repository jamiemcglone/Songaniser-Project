from flask import Blueprint, Flask, redirect, render_template, request
from repositories import band_repository, setlist_repository, setlist_song_repository, song_repository
import pdb
from models.band import Band

bands_blueprint = Blueprint("bands", __name__)

@bands_blueprint.route("/bands")
def bands():
    bands = band_repository.select_all()
    setlists = setlist_repository.select_all()
    songs = song_repository.select_all()
    return render_template("bands/index.html", bands=bands, setlists=setlists, songs=songs)

@bands_blueprint.route("/bands/<id>")
def band_view(id):
    band_to_view = band_repository.select(id)
    setlists = band_repository.get_all_setlists(band_to_view)
    songs = band_repository.get_all_songs(band_to_view)
    return render_template("bands/view.html", band=band_to_view, setlists=setlists, songs=songs)


@bands_blueprint.route("/bands/new")
def new_band():
    return render_template("bands/new.html")




@bands_blueprint.route("/bands", methods=["POST"])
def create_band():
    name = request.form["band_name"]
    band_type = request.form["band_type"]
    new_band = Band(name, band_type)
    band_repository.save(new_band)
    return redirect("/bands")
