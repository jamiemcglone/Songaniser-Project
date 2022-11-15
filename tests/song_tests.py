from models.song import Song
from models.band import Band
import unittest

class TestSong(unittest.TestCase):

    def test_update_learned_status(self):
        band1 = Band("Juno", "Function")
        song1 = Song("Dreams",
            "Fleetwood Mac",
            200,
            "A minor",
            "Intro, verse, chorus, solo, verse, chorus, outro",
            "F, G",
            True,
            "Lots of guitar melody bits",
            band1)
        song1.update_learned_status()
        self.assertEqual(False, song1.learned)