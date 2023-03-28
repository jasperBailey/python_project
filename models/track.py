class Track:
    def __init__(self, title, tempo, id=None):
        self.title = title
        self.tempo = tempo
        self.id = id
        
    def __repr__(self):
        return f"Track({self.title}, {self.tempo})"