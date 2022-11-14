import pdb

from models.band import Band
from models.song import Song
from models.setlist import Setlist
from models.setlist_song import Setlist_song
from repositories import band_repository, song_repository, setlist_repository, setlist_song_repository


band_repository.delete_all()
song_repository.delete_all()
setlist_repository.delete_all()
setlist_song_repository.delete_all()

band1 = Band("Juno", "Function")
band_repository.save(band1)

band2 = Band("Bob", "Cover")
band_repository.save(band2)

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
song_repository.save(song1)

setlist_song1 = Setlist_song(setlist1, song1)
setlist_song_repository.save(setlist_song1)

song2 = Song("Zombie",
    "The Cranberries",
    250,
    "E minor",
    "Intro, verse, chorus, verse, chorus, outro",
    "Em, Cmaj7, Gadd6, D/F#",
    False,
    "Just chords really", 
    band1)
song_repository.save(song2)

song3 = Song("Hotel Tropicana",
    "Wham",
    200,
    "C major",
    "Intro, verse, chorus, verse, chorus, bridge, chorus, outro",
    "C, D",
    False,
    "Lots of percussion",
    band2)
song_repository.save(song3)

setlist2 = Setlist("B Bar 20/08/22", band1)
setlist_repository.save(setlist2)


pdb.set_trace()