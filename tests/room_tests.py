import unittest 
from src_code.guest import Guest
from src_code.room import Room
from src_code.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Party Room", 10)

    def test_room_has_name(self):
        self.assertEqual("Party Room", self.room.name)
    
    def test_room_has_guests__empty_room(self):
        self.assertEqual(0, self.room.guest_count())

    def test_room_has_songs__empty_list(self):
        self.assertEqual(0, self.room.song_count())

    def test_room_has_capacity(self):
        self.assertEqual(10, self.room.capacity)

    def test_room_check_in(self):
        guest = Guest("Nat King Cole")
        self.room.check_in(guest)
        self.assertEqual(1, self.room.guest_count())

    def test_room_check_out(self):
        guest = Guest("Nat King Cole")
        self.room.check_in(guest)
        self.room.check_out(guest)
        self.assertEqual(0, self.room.guest_count())

    def test_room_can_add_songs_to_list(self):
        new_song = Song("Hit Me Baby One More Time", "Britney Spears")
        self.room.add_song(new_song)
        self.assertEqual(1, self.room.song_count())

    
