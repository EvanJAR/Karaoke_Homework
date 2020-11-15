import unittest 
from src_code.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Party Room")

    def test_room_has_name(self):
        self.assertEqual("Party Room", self.room.name)
    
    def test_room_has_guests__empty_room(self):
        self.assertEqual(0, self.room.guest_count())

    def test_room_has_songs__empty_list(self):
        self.assertEqual(0, self.room.song_count())
