from db.run_sql import run_sql
from models.song import Song
from repositories import band_repository, song_repository, setlist_repository


def save(song, setlist=None):
    sql = """INSERT INTO songs 
    (title, artist, duration, song_key, structure, harmony, learned, notes, band_id) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"""
    values = [song.title,
            song.artist,
            song.duration,
            song.song_key,
            song.structure,
            song.harmony,
            song.learned,
            song.notes,
            song.band.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    song.id = id
    song.add_song_to_band(song.band)
    band_repository.update(song.band)
    if setlist:
        song.add_song_to_setlist(setlist)
        setlist_repository.update(setlist)


def select_all():
    songs = []
    sql = "SELECT * FROM songs"
    results = run_sql(sql)
    for result in results:
        band = band_repository.select(result['band_id'])
        song = Song(result['title'], result['duration'], result['song_key'], 
        result['structure'], result['harmony'], result['learned'], result['notes'], band, result['id'])
        songs.append(song)
    return songs

def select(id):
    sql = "SELECT FROM songs WHERE id= %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        band = band_repository.select(result['band_id'])
        song = Song(result['title'], result['duration'], result['song_key'], 
        result['structure'], result['harmony'], result['learned'], result['notes'], band, result['id'])
    return song

def delete_all():
    sql = "DELETE FROM songs"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM songs WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(song):
    sql = """UPDATE songs SET 
    (title, artist, duration, song_key, structure, harmony, learned, notes, band_id) 
    = (%s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"""
    values = [song.title, song.artist, song.duration, song.song_key, 
    song.structure, song.harmony, song.learned, song.notes, song.band.id, song.id]
    run_sql(sql, values)
