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

    def add_song_to_band(self, band):
        band.song_catalogue.append(self.id)

    def add_song_to_setlist(self, setlist):
        setlist.songs.append(self.id)