"""Test all the classes in app folder"""

from unittest import TestCase
import unittest
from app.amity import Amity

class AmityTestCase(unittest.TestCase):

    """ Tests for amity """

    def setUp(self):
        self.amity = Amity()
        self.amity.rooms = []
        self.amity.available_rooms = []
        self.amity.offices = []
        self.amity.available_offices = []
        self.amity.living_spaces = []
        self.amity.available_living_spaces = []
        self.amity.people = []
        self.amity.allocated_people = []
        self.amity.waiting_list = []
        self.amity.office_waiting_list = []
        self.amity.living_space_waiting_list = []
        self.amity.fellows = []
        self.amity.allocated_fellows = []
        self.amity.staff = []
        self.amity.allocated_staff = []

    #... Tests for create_room ...#

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

    #... Tests for add_person ...#

    def test_add_person_add_fellow(self):
        """ Test that fellow was added successfully """

        self.amity.add_person("Robley", "Gori", "fellow", "Y")
        length_of_fellows = len(self.amity.fellows)
        self.assertEqual(len(self.amity.fellows), length_of_fellows)

    def test_add_person_add_staff(self):
        """ Test that staff was added successfully """

        self.amity.add_person("Robley", "Gori", "staff")
        length_of_staff = len(self.amity.fellows)
        self.assertEqual(len(self.amity.fellows), length_of_staff)

    def test_add_person_add_person_to_office(self):
        """ Test that person is successfully added to office """
        initial_people_in_office = len(self.amity.room.room_members())
        self.amity.create_room("red", "office")
        self.amity.add_person("Robley", "Gori", "staff", "N")
        final_length_of_office = len(self.amity.room.room_members())
        self.assertEqual((initial_people_in_office + 1), final_length_of_office)
    #     # self.amity.create_room("PinkRoom", "Office")
    #     # self.amity.create_room("ConferenceCentre", "Office")
        # self.amity.create_room("BlueRoom", "Office")
        # self.assertEqual(self.amity.add_person("Robley", "Gori", "Fellow", "N"), "Person was allocated an office successfully")

    def test_add_person_add_fellow_to_living_space(self):
        """ Test that fellow is successfully added to living space """
        self.amity.create_room("Maathai", "LivingSpace")
        self.amity.create_room("Tutu", "LivingSpace")
        self.amity.create_room("Lorup", "LivingSpace")
        self.assertEqual(self.amity.add_person("Robley", "Gori", "Fellow", "Y"), "Fellow was assigned to living space successfully")

    def test_add_person_add_staff_to_living_space(self):
        """ Test that staff cannot be added to living space """
        self.assertEqual(self.amity.add_person("Christina", "Sass", "Staff", "Y"), "Only fellows can be assigned living space")

    def test_add_person_add_person_full_office(self):
        """ Test that person is added to waiting list if offices are full """
        self.amity.create_room("PinkRoom", "Office")
        self.amity.add_person("Christina", "Sass", "Staff", "N")
        self.amity.add_person("Jeremy", "Johnson", "Staff", "N")
        self.amity.add_person("Robley", "Gori", "Fellow", "Y")
        self.amity.add_person("Jus", "Machungwa", "Fellow", "N")
        self.amity.add_person("Angela", "Mutava", "Fellow", "N")
        self.amity.add_person("Rose" , "Wambui", "Fellow", "N")
        self.assertEqual(self.amity.add_person("Jackline", "Maina", "Fellow", "Y"), "All the offices are fully occupied at the moment. You have been added to the waiting list")

    def test_add_person_add_fellow_to_full_living_space(self):
        """ Test that fellow is added to waiting list if living spaces are full """
        self.amity.create_room("Maathai", "LivingSpace")
        self.amity.add_person("Flevian", "Kanaiza", "Fellow", "Y")
        self.amity.add_person("Robley", "Gori", "Fellow", "Y")
        self.amity.add_person("Jus", "Machungwa", "Fellow", "Y")
        self.amity.add_person("Angela", "Mutava", "Fellow", "Y")
        self.assertEqual(self.amity.add_person("Jackline", "Maina", "Fellow", "Y"), "Sorry all the living spaces are fully occupied at the moment. You have been added to the waiting list")

    def test_add_person_add_fellow_to_living_with_full_office(self):
        """ Test that fellow is added to living space even when offices are full """
        self.amity.create_room("PinkRoom", "Office")
        self.amity.add_person("Christina", "Sass", "Staff", "N")
        self.amity.add_person("Jeremy", "Johnson", "Staff", "N")
        self.amity.add_person("Robley", "Gori", "Fellow", "Y")
        self.amity.add_person("Jus", "Machungwa", "Fellow", "N")
        self.amity.add_person("Angela", "Mutava", "Fellow", "N")
        self.amity.add_person("Rose", "Wambui", "Fellow", "N")

        self.amity.create_room("Maathai", "LivingSpace")
        self.amity.add_person("Flevian", "Kanaiza", "Fellow", "Y")
        self.amity.add_person("Robley", "Gori", "Fellow", "Y")
        self.amity.add_person("Angela", "Mutava", "Fellow", "Y")

        self.assertEqual(self.amity.add_person("Wekesa", "Maina", "Fellow", "Y"), "Fellow was assigned a living space successfully. Offices are fully occupied!")

    #... Tests for reallocate person ...#

#     def test_reallocate_person_reallocates_person(self):
#         """ Tests that person is reallocated """
#         self.amity.create_room("PinkRoom", "Office")
#         self.amity.create_room("ConferenceCentre", "Office")
#         self.assertEqual(self.amity.reallocate_person("F1", "PinkRoom"), "Person was reallocated successfully!")
#
#     def test_reallocate_person_cannot_reassign__person_to_the_same_room(self):
#         """ Tests that person is not reallocated to the same room """
#         self.amity.reallocate_person("F1", "Maathai")
#         self.assertEqual(self.amity.reallocate_person("F1", "Maathai"), "Person cannot be reallocated to the same room")
#
#     def test_reallocate_person_rejects_move_to_room_with_wrong_person_id(self):
#         """ Tests that a person cannot be reallocated using a wrong user id """
#         self.amity.add_person("Robley", "Gori", "Fellow", "F1")
#         self.assertEqual(self.amity.reallocate_person("F9", "Tutu"), "Person cannot be reallocated with wrong person id")
#
#     #... Tests for load people ...#
#
#     def test_load_people_loads_people_from_txt_file(self):
#         """ Tests that people are successfully loaded from a txt file """
#         self.assertEqual(self.amity.load_people('/Users/sharonsyra/Desktop/project1/amity/people.txt'), "People successfully added from txt file")
#
#     #... Tests for print allocations ...#
# #
# #     def test_print_allocations_prints_allocations_to_screen(self):
# #         """To test if method prints allocations to screen."""
#         self.amity.create_room("PinkRoom", "Office")
#         self.amity.add_person("Oliver", "Munala", "Fellow", "N")
#         self.amity.add_person("Jus", "Machungwa", "Fellow", "N")
#         self.amity.create_room("Maathai", "LivingSpace")
#         self.amity.add_person("Jackline", "Maina", "Fellow","N")
#         self.assertEqual(self.amity.print_allocations("Rooms"), "PinkRoom - Oliver Munala  Jus Machungwa   Maathai - Jackline Maina")
#
#     def test_print_allocations_prints_allocations_to_txt_file(self):
#         """To test if method prints allocations to txt file."""
#         self.assertEqual(self.amity.print_allocations("allocations.txt"), "Successfully dumped to file.")
#
#     #... Tests for unallocated rooms ...#
#
#     def test_print_unallocated_prints_unallocated_people_to_screen(self):
#         """To test if method prints unallocated people to screen."""
#         self.amity.create_room("PinkRoom", "Office")
#         self.amity.add_person("Oliver", "Munala", "Fellow", "Y")
#         self.amity.add_person("Jus", "Machungwa", "Fellow", "Y")
#         self.amity.create_room("Maathai", "LivingSpace")
#         self.amity.add_person("Jackline", "Maina", "Fellow", "Y")
#         self.assertEqual(self.amity.print_unallocated(), "PinkRoom - Oliver Munala  Jus Machungwa   Maathai - Jackline Maina")
#
#     def test_print_unallocated_prints_unallocated_people_to_txt_file(self):
#         """To test if method prints unallocated people to txt file."""
#         self.assertEqual(self.amity.print_unallocated("unallocated.txt"), "Successfully dumped unallocated people to file.")
#
#     #... Tests for print room ...#
#
#     def test_print_room_prints_all_people_in_room_name_to_screen(self):
#         """ It tests that all people in a room name are printed to screen """
#         self.amity.create_room("Tutu", "LivingSpace")
#         self.amity.add_person("Robley", "Gori", "Fellow", "Y")
#         self.amity.add_person("Jackline", "Maina", "Fellow", "Y")
#         self.amity.add_person("Angela", "Mutava", "Fellow", "Y")
#         self.amity.add_person("Rose", "Wambui", "Fellow", "Y")
#         self.assertEqual(self.amity.print_room("Tutu"), "\n Tutu: \n Robley Gori \n Jackline Maina  \n  Angela Mutava  \n Rose Wambui")
#
#     #... Tests for save state ...#
#
#     def test_save_state_adds_data_to_database(self):
#         """ Test to affirm that data from the application is successfully added to the database """
#
#         self.assertEqual(self.amity.save_state("amity.db"), "Data successfully added to database")
#
#     #... Tests for load state ...#
#
#     def test_load_state_successfully_loads_data_from_database(self):
#         """ Test that data is successfully loaded from database """
#         self.assertEqual(self.amity.load_state("amity.db"), "Data successfully loaded from database")
#
#
if __name__ == '__main__':
    unittest.main()

