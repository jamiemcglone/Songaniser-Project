import pdb

from models.band import Band
from models.song import Song
from models.setlist import Setlist
from repositories import band_repository, song_repository, setlist_repository


band_repository.delete_all()
song_repository.delete_all()
setlist_repository.delete_all()

band1 = Band("Juno", "Function")
band_repository.save(band1)

setlist1 = Setlist("Finnegans Wake 01/10/22", band1)
setlist_repository.save(setlist1)


song1 = Song("Dreams",
            "Fleetwood Mac",
            200,
            "A minor",
            "Intro, verse, chorus, solo, verse, chorus, outro",
            "F, G",
            False,
            "Lots of guitar melody bits",
            band1)
song_repository.save(song1, setlist1)

song2 = Song("Zombie",
"The Cranberries",
250,
"E minor",
"Intro, verse, chorus, verse, chorus, outro",
"Em, Cmaj7, Gadd6, D/F#",
False,
"Just chords really", 
band1)
song_repository.save(song2, setlist1)



pdb.set_trace()