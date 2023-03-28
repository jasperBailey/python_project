from db.run_sql import run_sql

from models.note import Note
import repositories.track_repository as track_repository

def save(note):
    sql = "INSERT INTO notes (pitch, track_id, duration, location) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [note.pitch, note.track.id, note.duration, note.location]
    results = run_sql(sql, values)
    id = results[0]['id']
    note.id = id
    return note

def select_all():
    notes = []
    sql = "SELECT * FROM notes"
    results = run_sql(sql)

    for row in results:
        track = track_repository.select(row['track_id'])
        note = Note(row['pitch'], track, row['duration'], row['location'], row['id'] )
        notes.append(note)
    return notes

def select(id):
    note = None
    sql = "SELECT * FROM notes WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        track = track_repository.select(result['track_id'])
        note = Note(result['pitch'], track, result['duration'], result['location'], result['id'] )
    return note

def delete_all():
    sql = "DELETE FROM notes"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM notes WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(note):
    sql = "UPDATE notes SET (pitch, track_id, duration, location) = (%s, %s, %s, %s) WHERE id = %s"
    values = [note.pitch, note.track.id, note.duration, note.location, note.id]
    run_sql(sql, values)

def notes_in_track(track):
    notes = []
    sql = "SELECT * FROM notes WHERE track_id = %s"
    values = [track.id]
    results = run_sql(sql, values)

    for row in results:
        note = Note(row['pitch'], row['track_id'], row['duration'], row['location'], row['id'] )
        notes.append(note)
    return notes