"""Test all the classes in app folder"""

from unittest import TestCase

from app.amity import Amity
from app.fellow import fellow
from app.living_space import LivingSpace
from app.office import office
from app.person import person
from app.room import room
from app.staff import staff

class AmityTestCase(unittest.TestCase):

    """ Tests for amity """

    def setUp(self):
        self.amity = Amity()

    #... Tests for create_person ...#

    def test_create_living(self):
        """ Test that living space was created successfully """
        self.assertEqual(self.amity.create_room("Maathai", "Tutu", " Lorup", "LivingSpace"), "Living space has been created")

    def test_create_office(self):
        """ Test that office was created successfully """
        self.assertEqual(self.amity.create_room("PinkRoom", "ConferenceCentre", "BlueRoom", "Office"), "Office has been created")

    def test_room_can_only_be_added_once(self):
        """ Test that room can only be added once """
        self.assertEqual(self.amity.create_room("Maathai", "LivingSpace"), "Room already exists. Create a different room!")

    def test_room_name_cannot_be_used_in_office_and_living(self):
        """ Test that room name is used for one room type only """
        self.assertEqual(self.amity.create_room("PinkRoom", "LivingSpace"), "The room name is already in use!")

    def test_handling_wrong_room_type(self):
        """ Test that room type can only be office or living space """
        self.assertEqual(self.amity.create_room("Conference", "Business"), "Business is not a room type! Please try Living Space or Office")

    #... Tests for add_person ...#

    def test_add_fellow(self):
        """ Test that fellow was added successfully """
        self.assertEqual(self.amity.add_person("Robley Gori", "Fellow"), "Fellow added successfully!")

    def test_add_staff(self):
        """ Test that staff was added successfully """
        self.assertEqual(self.amity.add_person("Christina Sass", "Staff"), "Staff added successfully!")

    def test_person_can_be_added_to_office(self):
        """ Test that person is successfully added to office """
        self.assertEqual(self.amity.add_person("Robley Gori", "Fellow", "N"), "Person was allocated an office successfully")

    def test_fellow_can_be_added_to_living_space(self):
        """ Test that fellow is successfully added to living space """
        self.assertEqual(self.amity.add_person("Robley Gori", "Fellow", "Y"), "Fellow was assigned to living space successfully")

    def test_staff_cannot_be_added_to_living_space(self):
        """ Test that staff cannot be added to living space """
        self.assertEqual(self.amity.add_person("Christina Sass", "Staff", "Y"), "Only fellows can be assigned living space")

    def test_person_added_to_waiting_list_if_office_is_full(self):
        """ Test that person is added to waiting list if offices are full """
        self.assertEqual(self.amity.add_person("Wekesa Maina", "Fellow", "Y"), "All the offices are fully occupied at the moment. You have been added to the waiting list")

    def test_fellow_added_to_waiting_list_if_living_space_is_full(self):
        """ Test that fellow is added to waiting list if living spaces are full """
        self.assertEqual(self.amity.add_person("Wekesa Maina", "Fellow", "Y"), "Sorry all the living spaces are fully occupied at the moment. You have been added to the waiting list")

    def test_fellow_can_be_added_to_living_space_if_office_is_full(self):
        """ Test that fellow can is added to living space even when offices are full """
        self.assertEqual(self.amity.add_person("Wekesa Maina", "Fellow", "Y"), "Fellow was assigned a living space successfully. Offices are fully occupied!")

    #... Tests for realocate person ...#

    def test_person_was_reallocated_successfully(self):
        self.assertEqual(self.amity.reallocate_person("F1", "Maathai"), "Person was reallocated successfully!")

    def test_person_cannot_be_reassigned_to_the_same_room(self):
        self.amity.reallocate_person("F1", "Maathai")
        self.assertEqual(self.amity.reallocate_person("F1", "Maathai"), "Person cannot be reallocated to the same room")

    def test_person_can_only_reallocate_to_specific_room_type(self):
        pass

    def test_reject_move_to_room_with_wrong_person_id(self):
        self.assertEqual(self.amity.reallocate_person("F9", "Tutu"), "Person cannot be reallocated with wrong person id")

    #... Tests for load people ...#



    #... Tests for print allocations ...#

    def test_print_allocations_prints_successfully_to_screen(self):
        """To test if method prints allocations to screen."""
        self.amity.create_room("office", ["Narnia"])
         self.amity.create_room("living_space", ["Python"])
        # create people
        self.amity.add_person("Fellow", "Daniel", "Maina1", "Y")
        self.amity.add_person("Fellow", "Daniel", "Maina2", "Y")
        self.amity.add_person("Fellow", "Daniel", "Maina3", "Y")

        self.assertEqual(self.amity.print_allocations(),
                         "Allocations successfully printed to screen.")

    def test_print_allocations_prints_successfully_dumps_to_file(self):
        """To test if method prints allocations to screen."""
        self.amity.create_room("office", ["Narnia"])
        self.amity.create_room("living_space", ["Python"])
        # create people
        self.assertEqual(self.amity.print_allocations("test_file.txt"),
                         "Successfully dumped to file.")

    #... Tests for unallocated rooms ...#

    def test_print_unallocated_prints_successfully_to_screen(self):
        """To test if method prints unallocated people to screen."""
        # create people without existing rooms
        self.amity.add_person("Fellow", "Daniel", "Maina1", "Y")

        self.assertEqual(self.amity.print_unallocated(),
                         "Successfully printed unallocated people to screen.")

    def test_print_unallocated_dumps_empty_file_if_no_unallocations(self):
        """To test if method dumps empty file when no unallocations."""
        # create people without existing rooms
        self.amity.add_person("Fellow", "Daniel", "Maina1", "Y")

        self.assertEqual(self.amity.print_unallocated("test_file.txt"),
                         "Successfully dumped unallocated people to file.")

    def test_print_unallocated_dumps_to_file_if_unallocations(self):
        """To test if method dumps empty file when no unallocations."""

        self.amity.add_person("Fellow", "Daniel", "Maina", "Y")

        self.assertEqual(self.amity.print_unallocated("test_file.txt"),
                         "Successfully dumped unallocated people to file.")

    #... Tests for print room ...#

    #... Tests for save state ...#

    #... Tests for load state ...#

    def test_load_state_prints_error_if_empty_db(self):
        """To test if method prints error message if empty db."""
        self.assertEqual(self.amity.load_state("no_db.db"),
                         "No data in {}".format("no_db.db"))

    def test_load_state_prints_when_db_not_empty(self):
        """To test if method retreives data from db."""
        self.assertEqual(self.amity.load_state("amity.db"),
                         "Data load from {} success".format("amity.db"))

    def test_load_people_rejects_load_if_file_not_found(self):
        """To test load_people rejects loading people if file not found."""
        self.assertEqual(self.amity.load_people("i_am_not_here.txt"),
                             "File does not exist.")

    def test_load_people_loads_successfully_from_file(self):
        """To test that load_people loads successfully."""
        self.assertEqual(self.amity.load_people("text.txt"),
                         "File found")


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
