from db.run_sql import run_sql
from models.band import Band
from models.setlist import Setlist
from models.song import Song
from repositories import band_repository

def save(band):
    sql = "INSERT INTO bands (band_name, band_type) VALUES (%s, %s) RETURNING id"
    values = [band.band_name, band.band_type]
    results = run_sql(sql, values)
    id = results[0]['id']
    band.id = id

def select_all():
    bands = []
    sql = "SELECT * FROM bands ORDER BY band_name"
    results = run_sql(sql)
    for result in results:
        band = Band(result['band_name'], result['band_type'], result['id'])
        bands.append(band)
    return bands

def select(id):
    sql = "SELECT * FROM bands WHERE id=%s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        band = Band(result['band_name'], result['band_type'], id)
    return band

def delete_all():
    sql = "DELETE FROM bands"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM bands WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(band):
    sql = "UPDATE bands SET (band_name, band_type) = (%s, %s) WHERE id = %s"
    values = [band.band_name, band.band_type, band.id]
    run_sql(sql, values)

def get_all_setlists(band):
    setlists = []
    sql = 'SELECT * FROM setlists WHERE band_id = %s'
    values = [band.id]
    results = run_sql(sql, values)

    for row in results:
        setlist_name = row['setlist_name']
        band = band_repository.select(row['band_id'])
        setlist = Setlist(setlist_name, band, row['id'])
        setlists.append(setlist)
    return setlists

def get_all_songs(band):
    songs = []
    sql = 'SELECT * FROM songs WHERE band_id = %s'
    values = [band.id]
    results = run_sql(sql, values)

    for row in results:
        song_title = row['title']
        song_artist = row['artist']
        song_duration = row['duration']
        song_key = row['song_key']
        song_structure = row['structure']
        song_harmony = row['harmony']
        song_learned = row['learned']
        song_notes = row['notes']
        song_id = row['id']
        band = band_repository.select(row['band_id'])
        song = Song(song_title, song_artist, song_duration, song_key, song_structure, song_harmony, song_learned, song_notes, band, song_id)
        songs.append(song)
        
    return songs




