from models.note import Note
from models.track import Track

import repositories.note_repository as note_repository
import repositories.track_repository as track_repository

note_repository.delete_all()
track_repository.delete_all()

track1 = Track("the trackmeister", 80)
track_repository.save(track1)
track2 = Track("tracky mctrackface", 120)
track_repository.save(track2)

track_repository.select_all()

note1 = Note(69, track1, 4, 0, 0.9)
note_repository.save(note1)

note2 = Note(74, track1, 2, 4, 0.6)
note_repository.save(note2)

note3 = Note(67, track1, 2, 4, 0.4)
note_repository.save(note3)

note_sequence = []
for i in range(12):
    note_sequence.append(Note(69+2*i, track2, 0.25, i/4, 0.6))
    print(note_sequence[i])
    note_repository.save(note_sequence[i])
note_sequence = []
for i in range(13):
    note = Note(93-2*i, track2, 0.25, 3+i/4, 0.6)
    note_sequence.append(note)
    note_repository.save(note)
note_sequence = []
for i in range(12):
    note_sequence.append(Note(69+2*i, track2, 0.25, 1+i/4, 0.5))
    print(note_sequence[i])
    note_repository.save(note_sequence[i])
note_sequence = []
for i in range(13):
    note = Note(93-2*i, track2, 0.25, 4+i/4, 0.5)
    note_sequence.append(note)
    note_repository.save(note)



                         
