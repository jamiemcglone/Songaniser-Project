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

band2 = Band("Band2", "Cover")
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

setlist_song2 = Setlist_song(setlist1, song2)
setlist_song_repository.save(setlist_song2)

song3 = Song("Wake Me Up Before You Go-Go",
    "Wham!",
    200,
    "C major",
    "Intro, verse, chorus, verse, chorus, bridge, chorus, outro",
    "C, Dm",
    True,
    "You play the horns solo bit",
    band1)
song_repository.save(song3)

setlist_song3 = Setlist_song(setlist1, song3)
setlist_song_repository.save(setlist_song3)

song4 = Song("Life is a Highway",
    "Rascal Flatts",
    220,
    "F major",
    "Intro, verse, chorus, verse, chorus, bridge, chorus, outro",
    "Dm C Bb Bb F C, Bb F C, Dm C Bb G7",
    False,
    "There's 2 solos",
    band1)
song_repository.save(song4)

setlist_song4 = Setlist_song(setlist1, song4)
setlist_song_repository.save(setlist_song4)

song5 = Song("She Moves in Her Own Way",
    "The Kooks",
    200,
    "G major",
    "Intro, verse, chorus, verse, chorus, bridge, solo, chorus",
    "G C G Bm Am Bm C",
    True,
    "You play the chords right after the solo",
    band2)

song_repository.save(song5)

song6 = Song("A song",
    "A band",
    100,
    "C major",
    "Chorus",
    "D",
    True,
    "This one is easy",
    band2)

song_repository.save(song6)

setlist2 = Setlist("B Bar 20/08/22", band2)
setlist_repository.save(setlist2)

setlist_song5 = Setlist_song(setlist2, song5)
setlist_song_repository.save(setlist_song5)

setlist_song6 = Setlist_song(setlist2, song6)
setlist_song_repository.save(setlist_song6)


pdb.set_trace()