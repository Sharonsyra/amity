"""Test all the classes in app folder"""

import unittest
from app.amity import Amity


class AmityTestCase(unittest.TestCase):

    """ Tests for amity """

    def setUp(self):
        self.amity = Amity()
        self.amity.rooms = []
        self.amity.offices = []
        self.amity.living_spaces = []
        self.amity.people = []
        self.amity.fellows = []
        self.amity.staff = []
        self.amity.waiting_list = []
        self.amity.office_waiting_list = []
        self.amity.living_space_waiting_list = []

    # ... Tests for create_room ...#

    def test_create_room_add_room_successfully(self):
        """ Test that room was created successfully """
        self.amity.create_room(["Hogwarts"], "office")
        self.assertEqual("Hogwarts", self.amity.rooms[0].room_name)

    def test_create_room_duplicates(self):
        """ Test that room can only be added once """
        self.amity.create_room(["Hogwarts"], "office")
        self.assertIn("Hogwarts", [i.room_name for i in self.amity.rooms])
        length_of_rooms = len(self.amity.rooms)
        self.amity.create_room(["Hogwarts"], "office")
        self.assertEqual(len(self.amity.rooms), length_of_rooms)

    # ... Tests for add_person ...#

    def test_add_person_add_fellow(self):
        """ Test that fellow was added successfully """
        self.amity.create_room("BlueRoom", "Office")
        person = self.amity.add_person("Robley", "Gori", "fellow", "N")
        p_id = self.amity.people[0].person_id
        self.assertIn("Robley Gori of id " + str(p_id) + " has been added to \
                                the system", person)

    def test_add_person_add_staff(self):
        """ Test that staff was added successfully """

        self.amity.create_room("Maathai", "LivingSpace")
        person = self.amity.add_person("Robley", "Gori", "fellow", "Y")
        p_id = self.amity.people[0].person_id
        self.assertIn("Robley Gori of id " + str(p_id) + " has been added to \
                              the system", person)

    def test_add_person_add_person_to_office(self):
        """ Test that person is successfully added to office """

        self.amity.create_room("BlueRoom", "Office")
        person = self.amity.add_person("Robley", "Gori", "fellow", "N")
        self.assertIn(kkk, person)

    def test_add_person_add_fellow_to_living_space(self):
        """ Test that fellow is successfully added to living space """


    def test_add_person_add_staff_to_living_space(self):
        """ Test that staff cannot be added to living space """
        self.amity.create_room("Maathai", "LivingSpace")
        person = self.amity.add_person("Robley", "Gori", "staff", "Y")
        self.assertIn("Staff cannot be allocated a living space!", person)

    def test_add_person_add_person_full_office(self):
        """ Test that person is added to waiting list if offices are full """
        self.amity.create_room("PinkRoom", "Office")
        self.amity.load_people("people.txt")

        person = self.amity.add_person("Jackline", "Maina", "Fellow", "Y")
        self.assertIn("Jackline Maina has been added to the office waiting \
                       list", person)

    def test_add_person_add_fellow_full_living_space(self):
        """ Test that fellow is added to waiting list if living spaces are \
        full """
        self.amity.create_room("Maathai", "LivingSpace")
        self.amity.add_person("Flevian", "Kanaiza", "Fellow", "Y")
        self.amity.add_person("Robley", "Gori", "Fellow", "Y")
        self.amity.add_person("Jus", "Machungwa", "Fellow", "Y")
        self.amity.add_person("Angela", "Mutava", "Fellow", "Y")
        person = self.amity.add_person("Jackline", "Maina", "Fellow", "Y")
        self.assertIn("Jackline Maina has been added to the living space \
                      waiting list", person)

    # ... Tests for reallocate person ...#

    def test_reallocate_person_reallocates_person(self):
        """ Tests that person is reallocated """
        self.amity.create_room("PinkRoom", "Office")
        self.amity.create_room("ConferenceCentre", "Office")
        self.assertEqual(self.amity.reallocate_person("F1", "PinkRoom"),
    "Person was reallocated successfully!")

    def test_reallocate_person_cannot_reassign_person_to_the_same_room(self):
        """ Tests that person is not reallocated to the same room """
        self.amity.create_room(["PinkRoom"], "Office")
        self.amity.add_person("Robley", "Gori", "fellow", "N")
        p_id = self.amity.people[0].person_id
        self.amity.create_room(["ConferenceCentre"], "Office")
        person = self.amity.reallocate_person(p_id, "ConferenceCentre")
        self.assertIn("Robley Gori of id " + str(p_id) + " has been\
        reallocated from PinkRoom to ConferenceCentre", person)


    # ... Tests for load people ...#

    def test_load_people_loads_people_from_txt_file(self):
        """ Tests that people are successfully loaded from a txt file """
        self.amity.load_people("people.txt")
        self.assertTrue("Data successfully loaded to amity!")

    # ... Tests for print allocations ...#

    def test_print_allocations_prints_allocations_to_screen(self):
        """To test if method prints allocations to screen."""
        self.amity.create_room(["red"], "office")
        self.amity.load_people("people.txt")
        self.amity.print_allocations()
        self.assertTrue("These are the rooms and there allocations")

    def test_print_allocations_prints_allocations_to_txt_file(self):
        """To test if method prints allocations to txt file."""
        self.amity.create_room(["red"], "office")
        self.amity.load_people("people.txt")
        self.amity.print_allocations("files/allocations.txt")
        self.assertTrue("Data has been dumped to file")

    # ... Tests for unallocated rooms ...#

    def test_print_unallocated_prints_unallocated_people_to_screen(self):
        """To test if method prints unallocated people to screen."""
        self.amity.load_people("people.txt")
        self.amity.load_people("people.txt")
        self.amity.print_unallocated()
        self.assertTrue("These are the people in the waiting list")

    def test_print_unallocated_prints_unallocated_people_to_txt_file(self):
        """To test if method prints unallocated people to txt file."""
        self.amity.load_people("people.txt")
        self.amity.print_unallocated("files/unallocated.txt")
        self.assertTrue("Data has been dumped to file")

    # ... Tests for print room ...#

    def test_print_room_prints_all_people_in_room_name_to_screen(self):
        """ It tests that all people in a room name are printed to screen """
        self.amity.create_room(["red"], "office")
        self.amity.load_people("people.txt")
        self.amity.print_room("red")
        self.assertTrue("red")
    # ... Tests for save state ...#

    def test_save_state_adds_data_to_database(self):
        """ Test to affirm that data from the application is successfully \
        added to the database """
        self.amity.save_state()
        self.assertTrue("Data successfully saved to database!")
    # ... Tests for load state ...#

    def test_load_state_successfully_loads_data_from_database(self):
        """ Test that data is successfully loaded from database """
        self.amity.save_state("amity.db")
        self.assertTrue("Data successfully loaded to amity!")


if __name__ == '__main__':
    unittest.main()
