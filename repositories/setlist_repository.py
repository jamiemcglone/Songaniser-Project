from db.run_sql import run_sql
from models.setlist import Setlist
from repositories import band_repository

def save(setlist):
    sql = "INSERT INTO setlists (setlist_name, band_id) VALUES (%s, %s) RETURNING id"
    values = [setlist.setlist_name, setlist.band.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    setlist.id = id
    
def select_all():
    setlists = []
    sql = "SELECT * FROM setlists"
    results = run_sql(sql)
    for result in results:
        band = band_repository.select(result['band_id'])
        setlist = Setlist(result['setlist_name'], band, result['id'])
        setlists.append(setlist)
    return setlists
    

def select(id):
    sql = "SELECT * FROM setlists WHERE id = %s"
    values = [id]
  
    results = run_sql(sql, values)
    if results:
        result = results[0]
        print('This is the result:')
        print(result)
        band = band_repository.select(result['band_id'])
        setlist = Setlist(result['setlist_name'], band, result['id'])
    return setlist

def delete_all():
    sql = "DELETE FROM setlists"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM setlists WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(setlist):
    sql = "UPDATE setlists SET (setlist_name, band_id) = (%s, %s) WHERE id = %s"
    values = [setlist.setlist_name, setlist.band.id, setlist.id]
    run_sql(sql, values)
