import unittest
from src_code.guest import Guest


class TestGuest(unittest.TestCase): 

    def setUp(self):
        self.guest = Guest("Nat King Cole", 41)

    def test_guest_has_name(self):
        self.assertEqual("Nat King Cole", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(41, self.guest.age)

    
