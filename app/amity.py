# from app.office import Office
from office import Office
from living_space import LivingSpace
from fellow import Fellow
from staff import Staff

class Amity():
    "Amity class has functions that create rooms, add people, allocate people to rooms, reallocate people to different rooms, load people and print allocated and unallocated people"

    room = {
        "rooms": [],
        "office": [],
        "livingspace": [],
        "office_waiting_list": [],
        "living_space_waiting_list": []
    }

    person = {
        "people": [],
        "staff": [],
        "fellow": []
    }
    def create_room(self, room_list, room_type):
        for room in room_list:
            if room in [i.room_name for i in self.room["rooms"]]:
                print("cannot create room {} . The room already exists.".format(room))
            else:
                if room_type == "office":
                    office = Office(room)
                    self.room['rooms'].append(office)
                    # self.room['office'][office] = []
                    print("Office {} of id - {} successfully created".format(office.room_name, office.room_id))

                elif room_type == "living_space":
                    livingspace = LivingSpace(room)
                    self.room['rooms'].append(livingspace)
                    # self.room['livingspace'][livingspace] = []
                    print("Living Space {} of id - {} successfully created".format(livingspace.room_name, livingspace.room_id))
                else:
                    print("Invalid room type. Use office or livingspace only")

    def add_person(self, first_name, second_name, type, wants_accomodation):
        pass

    def reallocate_person(self, person_id, room_name):
        pass

    def load_people(self, *args):
        pass

    def print_allocations(self, *args):
        pass

    def print_unallocated(self, *args):
        pass

    def print_room(self, room):
        pass

    def get_available_rooms(self):
        pass

    def get_room_allocated(self):
        pass

    def get_full_rooms(self):
        pass

    def print_people(self):
        pass

    def print_people_and_their_allocations(self):
        pass

    def save_state(self, *args):
        pass

    def load_state(self, *args):
        pass
amity = Amity()
amity.create_room(["Hogwarts", "Narnia"], "office")
amity.create_room(["ddd"], "living_space")
