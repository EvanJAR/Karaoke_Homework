import unittest 
from src_code.guest import Guest
from src_code.room import Room
from src_code.room_2 import Room2
from src_code.room_3 import Room3
from src_code.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Party Room", 7)
        self.room_2 = Room2("Small Room", 5)
        self.room_3 = Room3("Celebration Room", 15) 
        

    def test_room_has_name(self):
        self.assertEqual("Party Room", self.room.name)
        self.assertEqual("Small Room", self.room_2.name)
        self.assertEqual("Celebration Room", self.room_3.name)

    def test_room_has_guests__empty_room(self):
        self.assertEqual(0, self.room.guest_count())
        self.assertEqual(0, self.room_2.guest_count())
        self.assertEqual(0, self.room_3.guest_count())

    def test_room_has_songs__empty_list(self):
        self.assertEqual(0, self.room.song_count())
        self.assertEqual(0, self.room_2.song_count())
        self.assertEqual(0, self.room_3.song_count())

    def test_room_has_capacity(self):
        self.assertEqual(7, self.room.capacity)
        self.assertEqual(5, self.room_2.capacity)
        self.assertEqual(15, self.room_3.capacity)
    
    def test_room_check_in__room1(self):
        guest = Guest("Nat King Cole")
        self.room.check_in(guest)
        self.assertEqual(1, self.room.guest_count())

    def test_room_check_out__room2(self):
        guest = Guest("Nat King Cole")
        self.room.check_in(guest)
        self.room.check_out(guest)
        self.assertEqual(0, self.room.guest_count())

    def test_room_check_in__room2(self):
        guest = Guest("Sammy Davis Jr.")
        self.room.check_in(guest)
        self.assertEqual(1, self.room.guest_count())

    def test_room_check_out__room2(self):
        guest = Guest("Sammy Davis Jr.")
        self.room.check_in(guest)
        self.room.check_out(guest)
        self.assertEqual(0, self.room.guest_count())

    def test_room_check_in__room3(self):
        guest = Guest("Lena Horne")
        self.room.check_in(guest)
        self.assertEqual(1, self.room.guest_count())

    def test_room_check_out__room3(self):
        guest = Guest("Lena Horne")
        self.room.check_in(guest)
        self.room.check_out(guest)
        self.assertEqual(0, self.room.guest_count())


    def test_room_can_add_songs_to_list(self):
        new_song = Song("Hit Me Baby One More Time", "Britney Spears")
        new_song2 = Song("Firework", "Katy Perry")
        new_song3 = Song("Sweet Caroline", "Neil Diamond")
        self.room.add_song(new_song)
        self.room_2.add_song(new_song2)
        self.room_3.add_song(new_song3)
        self.assertEqual(1, self.room.song_count())
        self.assertEqual(1, self.room_2.song_count())
        self.assertEqual(1, self.room_3.song_count())

 

    

    
