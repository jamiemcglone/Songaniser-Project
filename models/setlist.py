class Setlist:

    def __init__(self, setlist_name, band, id=None):
        
        self.setlist_name = setlist_name
        self.songs = []
        self.band = band
        self.id = id

    def add_setlist_to_band(self, band):
        band.setlists.append(self.id)
        