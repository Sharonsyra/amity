"""Test all the classes in app folder"""

from unittest import TestCase

from app.amity import Amity
from app.fellow import fellow
from app.livingspace import LivingSpace
from app.office import office
from app.person import person
from app.room import room
from app.staff import staff

class TestAMity(unittest.TestCase):
    def setUp(self):
        self.amity = Amity()

    def test_create_single_room(self):
        self.assertEqual(self.amity.Create_room("Maathai", "LivingSpace"), "Room has been created")

    def test_create_multiple_rooms(self):
        self.assertEqual(self.amity.Create_room("Maathai", "LivingSpace"), "Room has been created")
        self.assertEqual(self.amity.Create_room("Tutu", "LivingSpace"), "Room has been created")
        self.assertEqual(self.amity.Create_room("Lorup", "LivingSpace"), "Room has been created")

    def test_room_name_is_string(self):
        self.assertEqual(self.amity.Create_room())

    def test_existing_room_type(self):
        self.assertEqual(self.amity.Create_room("Conference", "Business"), "Business is not a room type")

    def test_correct_room_type(self):
        self.assertTrue(self.amity.Create_room("", ""), "")

