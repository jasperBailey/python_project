class Note:
    def __init__(self, pitch, track, duration, position, velocity=1.0, id=None):
        self.pitch = pitch
        self.duration = duration
        self.position = position
        self.track = track
        self.velocity = velocity
        self.id = id

    def __repr__(self):
        return f"Note({self.pitch}, {self.track}, {self.duration}, {self.position}, {self.velocity}, {self.id})"
    
    def get_pitch_as_string(self):
        pitches = ["C", "C#/D♭", "D", "D#/E♭", "E", "F", "F#/G♭", "G",
                   "G#/A♭", "A", "A#/B♭", "B"]
        return pitches[self.pitch % 12]