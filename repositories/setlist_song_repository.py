from db.run_sql import run_sql
from models.setlist_song import Setlist_song
from repositories import song_repository, setlist_repository


def save(setlist_song):
    sql = """INSERT INTO setlist_songs 
    (setlist_id, song_id) 
    VALUES (%s, %s) RETURNING id"""
    values = [setlist_song.setlist.id, setlist_song.song.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    setlist_song.id = id


def select_all():
    setlist_songs = []
    sql = "SELECT * FROM setlist_songs"
    results = run_sql(sql)
    for result in results:
        print('this is result of setlist_song')
        print(result)
        setlist = setlist_repository.select(result['setlist_id'])
        song = song_repository.select(result['song_id'])
        setlist_song = Setlist_song(setlist, song, result['id'])
        setlist_songs.append(setlist_song)
    return setlist_songs

def select(id):
    sql = "SELECT FROM setlist_songs WHERE id= %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        setlist = setlist_repository.select(result['setlist_id'])
        song = song_repository.select(result['song_id'])
        setlist_song = Setlist_song(setlist, song, result['song_id'])
    return setlist_song

def delete_all():
    sql = "DELETE FROM setlist_songs"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM setlist_songs WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(setlist_song):
    sql = """UPDATE setlist_songs SET 
    (setlist_id, song_id) 
    = (%s, %s) WHERE id = %s"""
    values = [setlist_song.setlist.id, setlist_song.song.id]
    run_sql(sql, values)
