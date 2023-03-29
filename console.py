from models.note import Note
from models.track import Track

import repositories.note_repository as note_repository
import repositories.track_repository as track_repository

note_repository.delete_all()
track_repository.delete_all()

track1 = Track("Sweet Child O' Mine", 128)
track_repository.save(track1)
track2 = Track("FFVII Victory Fanfare", 120)
track_repository.save(track2)

notes = []

notes.append(Note(73, track1, 0.5, 0.0, 0.9))
notes.append(Note(85, track1, 0.5, 0.5, 0.9))
notes.append(Note(80, track1, 0.5, 1.0, 0.9))
notes.append(Note(78, track1, 0.5, 1.5, 0.9))
notes.append(Note(90, track1, 0.5, 2.0, 0.9))
notes.append(Note(80, track1, 0.5, 2.5, 0.9))
notes.append(Note(89, track1, 0.5, 3.0, 0.9))
notes.append(Note(80, track1, 0.5, 3.5, 0.9))
notes.append(Note(73, track1, 0.5, 4.0, 0.9))
notes.append(Note(85, track1, 0.5, 4.5, 0.9))
notes.append(Note(80, track1, 0.5, 5.0, 0.9))
notes.append(Note(78, track1, 0.5, 5.5, 0.9))
notes.append(Note(90, track1, 0.5, 6.0, 0.9))
notes.append(Note(80, track1, 0.5, 6.5, 0.9))
notes.append(Note(89, track1, 0.5, 7.0, 0.9))
notes.append(Note(80, track1, 0.5, 7.5, 0.9))

notes.append(Note(75, track1, 0.5, 8.0, 0.9))
notes.append(Note(85, track1, 0.5, 8.5, 0.9))
notes.append(Note(80, track1, 0.5, 9.0, 0.9))
notes.append(Note(78, track1, 0.5, 9.5, 0.9))
notes.append(Note(90, track1, 0.5, 10.0, 0.9))
notes.append(Note(80, track1, 0.5, 10.5, 0.9))
notes.append(Note(89, track1, 0.5, 11.0, 0.9))
notes.append(Note(80, track1, 0.5, 11.5, 0.9))
notes.append(Note(75, track1, 0.5, 12.0, 0.9))
notes.append(Note(85, track1, 0.5, 12.5, 0.9))
notes.append(Note(80, track1, 0.5, 13.0, 0.9))
notes.append(Note(78, track1, 0.5, 13.5, 0.9))
notes.append(Note(90, track1, 0.5, 14.0, 0.9))
notes.append(Note(80, track1, 0.5, 14.5, 0.9))
notes.append(Note(89, track1, 0.5, 15.0, 0.9))
notes.append(Note(80, track1, 0.5, 15.5, 0.9))

notes.append(Note(78, track1, 0.5, 16.0, 0.9))
notes.append(Note(85, track1, 0.5, 16.5, 0.9))
notes.append(Note(80, track1, 0.5, 17.0, 0.9))
notes.append(Note(78, track1, 0.5, 17.5, 0.9))
notes.append(Note(90, track1, 0.5, 18.0, 0.9))
notes.append(Note(80, track1, 0.5, 18.5, 0.9))
notes.append(Note(89, track1, 0.5, 19.0, 0.9))
notes.append(Note(80, track1, 0.5, 19.5, 0.9))
notes.append(Note(78, track1, 0.5, 20.0, 0.9))
notes.append(Note(85, track1, 0.5, 20.5, 0.9))
notes.append(Note(80, track1, 0.5, 21.0, 0.9))
notes.append(Note(78, track1, 0.5, 21.5, 0.9))
notes.append(Note(90, track1, 0.5, 22.0, 0.9))
notes.append(Note(80, track1, 0.5, 22.5, 0.9))
notes.append(Note(89, track1, 0.5, 23.0, 0.9))
notes.append(Note(80, track1, 0.5, 23.5, 0.9))

notes.append(Note(73, track1, 0.5, 24.0, 0.9))
notes.append(Note(85, track1, 0.5, 24.5, 0.9))
notes.append(Note(80, track1, 0.5, 25.0, 0.9))
notes.append(Note(78, track1, 0.5, 25.5, 0.9))
notes.append(Note(90, track1, 0.5, 26.0, 0.9))
notes.append(Note(80, track1, 0.5, 26.5, 0.9))
notes.append(Note(89, track1, 0.5, 27.0, 0.9))
notes.append(Note(80, track1, 0.5, 27.5, 0.9))
notes.append(Note(73, track1, 0.5, 28.0, 0.9))
notes.append(Note(85, track1, 0.5, 28.5, 0.9))
notes.append(Note(80, track1, 0.5, 29.0, 0.9))
notes.append(Note(78, track1, 0.5, 29.5, 0.9))
notes.append(Note(90, track1, 0.5, 30.0, 0.9))
notes.append(Note(80, track1, 0.5, 30.5, 0.9))
notes.append(Note(89, track1, 0.5, 31.0, 0.9))
notes.append(Note(80, track1, 0.5, 31.5, 0.9))

########

notes.append(Note(72, track2, 0.333, 0, 0.75))
notes.append(Note(67, track2, 0.333, 0, 0.75))
notes.append(Note(64, track2, 0.333, 0, 0.75))

notes.append(Note(72, track2, 0.333, 0.333, 0.75))
notes.append(Note(67, track2, 0.333, 0.333, 0.75))
notes.append(Note(64, track2, 0.333, 0.333, 0.75))

notes.append(Note(72, track2, 0.334, 0.666, 0.75))
notes.append(Note(67, track2, 0.334, 0.666, 0.75))
notes.append(Note(64, track2, 0.334, 0.666, 0.75))

notes.append(Note(72, track2, 1, 1, 0.75))
notes.append(Note(67, track2, 1, 1, 0.75))
notes.append(Note(64, track2, 1, 1, 0.75))

notes.append(Note(68, track2, 1, 2, 0.75))
notes.append(Note(63, track2, 1, 2, 0.75))
notes.append(Note(61, track2, 1, 2, 0.75))

notes.append(Note(70, track2, 1, 3, 0.75))
notes.append(Note(65, track2, 1, 3, 0.75))
notes.append(Note(62, track2, 1, 3, 0.75))

notes.append(Note(72, track2, 0.333, 4, 0.75))
notes.append(Note(64, track2, 0.333, 4, 0.75))
notes.append(Note(60, track2, 0.333, 4, 0.75))

notes.append(Note(70, track2, 0.333, 4.666, 0.75))
notes.append(Note(65, track2, 0.333, 4.666, 0.75))
notes.append(Note(61, track2, 0.333, 4.666, 0.75))

notes.append(Note(72, track2, 3, 5, 0.75))
notes.append(Note(65, track2, 3, 5, 0.75))
notes.append(Note(63, track2, 3, 5, 0.75))



notes.append(Note(48, track2, 0.333, 0, 0.6))
notes.append(Note(52, track2, 0.333, 0.333, 0.6))
notes.append(Note(55, track2, 0.333, 0.666, 0.6))

notes.append(Note(60, track2, 0.333, 1, 0.6))
notes.append(Note(55, track2, 0.333, 1.333, 0.6))
notes.append(Note(52, track2, 0.333, 1.666, 0.6))

notes.append(Note(49, track2, 0.333, 2, 0.6))
notes.append(Note(51, track2, 0.333, 2.333, 0.6))
notes.append(Note(56, track2, 0.333, 2.666, 0.6))

notes.append(Note(58, track2, 0.333, 3, 0.6))
notes.append(Note(61, track2, 0.333, 3.333, 0.6))
notes.append(Note(65, track2, 0.333, 3.666, 0.6))

notes.append(Note(53, track2, 0.333, 4, 0.6))
notes.append(Note(56, track2, 0.333, 4.333, 0.6))
notes.append(Note(58, track2, 0.333, 4.666, 0.6))

notes.append(Note(61, track2, 0.333, 5, 0.6))
notes.append(Note(65, track2, 0.333, 5.333, 0.6))
notes.append(Note(68, track2, 0.333, 5.666, 0.6))

notes.append(Note(72, track2, 0.25, 6, 0.6))
notes.append(Note(68, track2, 0.25, 6.25, 0.6))
notes.append(Note(65, track2, 0.25, 6.5, 0.6))
notes.append(Note(61, track2, 0.25, 6.75, 0.6))

notes.append(Note(60, track2, 0.25, 7, 0.6))
notes.append(Note(56, track2, 0.25, 7.25, 0.6))
notes.append(Note(53, track2, 0.25, 7.5, 0.6))
notes.append(Note(49, track2, 0.25, 7.75, 0.6))

for note in notes:
    note_repository.save(note)