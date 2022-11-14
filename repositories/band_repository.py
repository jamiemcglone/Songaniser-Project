from db.run_sql import run_sql
from models.band import Band
from repositories import band_repository, song_repository, setlist_repository

def save(band):
    sql = "INSERT INTO bands (band_name, band_type) VALUES (%s, %s) RETURNING id"
    values = [band.band_name, band.band_type]
    results = run_sql(sql, values)
    id = results[0]['id']
    band.id = id

def select_all():
    bands = []
    sql = "SELECT * FROM bands"
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
    sql = "UPDATE bands SET (band_name, band_type, song_catalogue, setlists) = (%s, %s, %s, %s) WHERE id = %s"
    values = [band.band_name, band.band_type, band.song_catalogue, band.setlists, band.id]
    run_sql(sql, values)

# def update_songs_catalogue(song, band):
#     sql = "UPDATE bands SET (song_catalogue) = (%s) WHERE id = %s"
#     values = [song, band.id]
#     run_sql(sql, values)

