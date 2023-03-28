class Note:
    def __init__(self, pitch, track, duration, location, velocity=1.0, id=None):
        self.pitch = pitch
        self.duration = duration
        self.location = location
        self.track = track
        self.velocity = velocity
        self.id = id

    def __repr__(self):
        return f"Note({self.pitch}, {self.track}, {self.duration}, {self.location}, {self.velocity}, {self.id})"