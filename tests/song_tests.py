import unittest
from src_code.song import Song 

class TestSong(unittest.TestCase): 

    def setUp(self):
        self.song = Song("Hit Me Baby One More Time", "Britney Spears")
    
    def test_song_has_name(self):
        self.assertEqual("Hit Me Baby One More Time", self.song.name)

    def test_song_has_artist(self):
        self.assertEqual("Britney Spears", self.song.artist)