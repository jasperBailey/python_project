from models.note import Note
from models.track import Track

import repositories.note_repository as note_repository
import repositories.track_repository as track_repository

note_repository.delete_all()
track_repository.delete_all()

track1 = Track("the trackmeister", 69)
track_repository.save(track1)
track2 = Track("tracky mctrackface", 120)
track_repository.save(track2)

track_repository.select_all()

note1 = Note(69, track1, 4, 0)
note_repository.save(note1)

note2 = Note(76, track1, 2, 4)
note_repository.save(note2)
