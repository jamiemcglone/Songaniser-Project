import json

class Song:

    def __init__(self, title, artist, duration, 
    song_key, structure, harmony, learned, 
    notes, band, id=None):
    
        self.title = title
        self.artist = artist
        self.duration = duration
        self.song_key = song_key
        self.structure = structure
        self.harmony = harmony
        self.learned = learned
        self.notes = notes
        self.band = band
        self.id = id

    def update_learned_status(self):
        self.learned = json.loads(self.learned.lower())
        self.learned = not self.learned
