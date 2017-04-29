import random

from office import Office
from living_space import LivingSpace
from fellow import Fellow
from staff import Staff

class Amity():
    "Amity class has functions that create rooms, add people, allocate people to rooms, reallocate people to different rooms, load people and print allocated and unallocated people"

    room = {
        "rooms": [],
        "office": [],
        "living_space": [],
        "office_waiting_list": [],
        "living_space_waiting_list": []
    }

    person = {
        "people": [],
        "staff": [],
        "fellow": []
    }

    available_offices = []
    available_living_spaces = []
    full_offices = []
    full_living_spaces = []
    office_waiting_list = []
    living_space_waiting_list = []

    def create_room(self, room_list, room_type):
        for room in room_list:
            if room in [i.room_name for i in self.room["rooms"]]:
                print("cannot create room {} . The room already exists.".format(room))
            else:
                if room_type == "office":
                    office = Office(room)
                    self.room['rooms'].append(office)
                    self.room["office"].append(office)
                    print("Office {} of id - {} successfully created".format(office.room_name, office.room_id))

                elif room_type == "living_space":
                    living_space = LivingSpace(room)
                    self.room['rooms'].append(living_space)
                    self.room["living_space"].append(living_space)
                    print("Living Space {} of id - {} successfully created".format(living_space.room_name, living_space.room_id))

    def add_person(self, first_name, last_name, person_type, wants_accomodation):
        # p_name = f_name + " " + s_name
        if person_type == "staff":
            staff = Staff(first_name, last_name)
            # add staff to office
            self.person["people"].append(staff)
            self.person["staff"].append(staff)
            if wants_accomodation == "Y":
                print "Accomodation is offered to Fellows only!"
            if self.available_offices != 0:
                office_allocated = self.allocate_office()
                return office_allocated
            else:
                self.office_waiting_list.append(staff)

        elif person_type == "fellow":
            fellow = Fellow(first_name, last_name)
            # add staff to office
            self.person["people"].append(fellow)
            self.person["fellow"].append(fellow)
            if wants_accomodation == "Y":
                pass

            elif wants_accomodation == "N":
                pass
            if self.available_offices != 0:
                office_allocated = self.allocate_office()
                return office_allocated
            else:
                self.office_waiting_list.append(fellow)

    def allocate_office(self):
        office_allocated = random.choice(self.available_offices)
        return office_allocated

    def allocate_living_space(self):
        living_space_allocated = random.choice(self.available_living_spaces)
        return living_space_allocated

    def available_office(self):
        [room for room in self.room["office"]]
        if len(room) < 6:
            room_capacity = 6 - len(room)
            self.available_offices.append(room)
            return self.available_offices, room_capacity
        elif len(room) == 6:
            self.full_offices.append(room)
        return self.full_offices

    def available_living_space(self):
        [room for room in self.room["living_space"]]
        if len(room) < 4:
            room_capacity = 4 - len(room)
            self.available_living_spaces.append(room)
            return self.available_living_spaces, room_capacity
        elif len(room) == 4:
            self.full_living_spaces.append(room)
            return self.full_living_spaces

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


# amity = Amity()
# amity.create_room(["Hogwarts", "Narnia"], "office")
#amity.create_room(["ddd"], "living_space")