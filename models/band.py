class Band:

    def __init__(self, band_name, band_type, id=None):

        self.band_name = band_name
        self.band_type = band_type
        self.song_catalogue = []
        self.setlists = []
        self.id = id
        