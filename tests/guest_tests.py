import unittest
from src_code.guest import Guest


class TestGuest(unittest.TestCase): 

    def setUp(self):
        self.guest = Guest("Nat King Cole")

    def test_guest_has_name(self):
        self.assertEqual("Nat King Cole", self.guest.name)

    def test_group_size(self):
        self.assertEqual(0, self.guest.group_size())

    def test_guest_can_add_new_member_to_group(self):
        new_guest = Guest("Dean Martin")
        self.guest.add_to_group(new_guest)
        self.assertEqual(1, self.guest.group_size())

    def test_guest_can_remove_member_from_group(self):
        guest_to_remove = Guest("Dean Martin")
        self.guest.add_to_group(guest_to_remove)
        self.guest.remove_from_group(guest_to_remove)
        self.assertEqual(0, self.guest.group_size())
        
    

