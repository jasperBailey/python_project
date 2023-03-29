from db.run_sql import run_sql
from models.track import Track

def save(track):
    sql = "INSERT INTO tracks (title, tempo) VALUES (%s, %s) RETURNING *"
    values = [track.title, track.tempo]
    results = run_sql(sql, values)
    id = results[0]['id']
    track.id = id
    return track

def select_all():
    tracks = []

    sql = "SELECT * FROM tracks"
    results = run_sql(sql)

    for row in results:
        track = Track(row['title'], row['tempo'], row['id'] )
        tracks.append(track)
    return tracks

def select(id):
    track = None
    sql = "SELECT * FROM tracks WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        track = Track(result['title'], result['tempo'], result['id'] )
    return track

def delete_all():
    sql = "DELETE FROM tracks"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM tracks WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(track):
    sql = "UPDATE tracks SET (title, tempo) = (%s, %s) WHERE id = %s"
    values = [track.title, track.tempo, track.id]
    run_sql(sql, values)