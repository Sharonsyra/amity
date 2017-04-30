import random
from termcolor import cprint

from office import Office
from living_space import LivingSpace
from fellow import Fellow
from staff import Staff


class Amity(object):
    """Amity class has functions that create rooms, add people, allocate people to rooms, 
    reallocate people to different rooms, load people and print allocated and unallocated people"""
    def __init__(self):

        self.space = ""

        self.room = {
            "rooms": [],
            "office": [],
            "living_space": [],
            "office_waiting_list": [],
            "living_space_waiting_list": []
            }

        self.person = {
            "people": [],
            "staff": [],
            "fellow": []
            }

        self.available_offices = []
        self.available_living_spaces = []
        self.full_offices = []
        self.full_living_spaces = []
        self.office_waiting_list = []
        self.living_space_waiting_list = []

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
                    print("Living Space {} of id - {} successfully created".format(living_space.room_name,
                                                                                   living_space.room_id))

    def add_person(self, first_name, last_name, person_type, wants_accommodation):
        # Get the list of available offices
        for room in self.room["office"]:
            if len(room.room_members) < room.room_capacity:
                if room not in self.available_offices:
                    self.available_offices.append(room)
            elif len(room.room_members) >= room.room_capacity:
                if room in self.available_offices:
                    self.available_offices.remove(room)
                    self.full_offices.append(room)

        # Get the list of available living spaces
        for room in self.room["living_space"]:
            if len(room.room_members) < room.room_capacity:
                if room not in self.available_living_spaces:
                    self.available_living_spaces.append(room)
            elif len(room.room_members) == room.room_capacity:
                if room in self.available_offices:
                    self.available_offices.remove(room)
                    self.full_living_spaces.append(room)

        if person_type == "staff":
            staff = Staff(first_name, last_name)
            # add staff to people
            self.person["people"].append(staff)
            self.person["staff"].append(staff)
            print("{} {} has been added to the system".format(staff.first_name, staff.last_name))
            # Allocate staff to a random empty office
            if len(self.available_offices) > 0:
                office_allocated = random.choice(self.available_offices)
                office_allocated.room_members.append(staff)
                print("{} {} has been allocated {}".format(staff.first_name, staff.last_name, office_allocated))
            elif len(self.available_offices) == 0:
                self.office_waiting_list.append(staff)
                print("{} {} has been added to the office waiting list".format(staff.first_name, staff.last_name))

        elif person_type == "fellow":
            fellow = Fellow(first_name, last_name)
            # add fellow to people
            self.person["people"].append(fellow)
            self.person["fellow"].append(fellow)
            print("{} {} has been added to the system".format(first_name, last_name))
            # Give them an office first
            if len(self.available_offices) > 0:
                office_allocated = random.choice(self.available_offices)
                office_allocated.room_members.append(fellow)
                print("{} {} has been allocated {}".format(fellow.first_name, fellow.last_name, office_allocated))
            elif len(self.available_offices) == 0:
                self.office_waiting_list.append(fellow)
                print("{} {} has been added to the office waiting list".format(fellow.first_name, fellow.last_name))

            if wants_accommodation == "Y":
                if len(self.available_living_spaces) > 0:
                    living_space_allocated = random.choice(self.available_living_spaces)
                    living_space_allocated.room_members.append(fellow)
                    print("{} {} has been allocated {}".format(fellow.first_name, fellow.last_name,
                                                               living_space_allocated))

                elif len(self.available_living_spaces) == 0:
                    self.living_space_waiting_list.append(fellow)
                    print("{} {} has been added to the living space waiting list".format(fellow.first_name,
                                                                                         fellow.last_name))

    def reallocate_person(self, person_id, room_name):
        pass

    def load_people(self, args):
        """Add people to rooms from a txt file"""
        filename = args["<filename>"]
        with open(filename, 'r') as my_file:
            people = my_file.readlines()
            for p in people:
                p = p.split()
                if p:
                    first_name = p[0]
                    last_name = p[1]
                    if p[2] == "FELLOW":
                        is_staff = False
                        is_fellow = True
                    else:
                        is_staff = True
                        is_fellow = False
                    if len(p) == 4:
                        wants_accommodation = p[3]
                    else:
                        wants_accommodation = None

                    self.add_person({
                        "<first_name>": first_name,
                        "<last_name>": last_name,
                        "<wants_accommodation>": wants_accommodation,
                        "Fellow": is_fellow,
                        "Staff": is_staff
                    })

    def print_allocations(self, args):
        """Print list of occupants per room to the  \
        screen and optionally to a text file"""
        print self.space
        output = ""
        for r in self.room["rooms"]:
            output += r.room_name + "\n"
            output += "-" * 50 + "\n"
            if r.room_members:
                output += ", ".join(p.room_name for p in r.room_members) + "\n"
                output += self.space + "\n"
            else:
                output += "This room has no occupants.\n"
                output += self.space + "\n"
        if not self.room["rooms"]:
            output += "There are no rooms in the system.\n"
            output += "Add a room using the create_room command" \
                      " and try again.\n"
        print output
        # if args["--o"]:
        #     with open(args["--o"], 'wt') as f:
        #         f.write(output)
        #         print "The list of allocations has been saved " \
        #               "to the following file: "
        #         print args["--o"]
        #         print self.space

    def print_unallocated(self, args):
        """Print list of unallocated people to the \
        screen and optionally to a text file"""
        print self.space
        output = ""
        output += "Unallocated People\n"
        output += "-" * 50 + "\n"
        for p in self.person["people"]:
            if p not in self.living_space_waiting_list and self.office_waiting_list:
                output += p.name + "\n"
                if p not in self.unallocated_people:
                    self.unallocated_people.append(p)
        if not self.person["people"]:
            output += "There are no people in the system.\n"
            output += "Add a person using the add_person command" \
                      " and try again.\n"
        elif not self.office_waiting_list and self.living_space_waiting_list:
            output += "There are no unallocated people in the system.\n"
        print output
        # if args["--o"]:
        #     with open(args["--o"], 'wt') as f:
        #         f.write(output)
        #         print "The list of unallocated people has been saved " \
        #               "to the following file: "
        #         print args["--o"]
        #         print spacer

    def print_room(self, args):
        """Print the names of all the people in room_name on the screen"""
        print self.space
        room_name = args["<room_name>"]
        if room_name not in [r.room_name for r in self.room["rooms"]]:
            print "The room you have entered does not exist."
            print "Please try again."
            print self.space
        for r in self.room["rooms"]:
            if r.room_name == room_name:
                room = r
                print room.room_name
                print "-" * 50
                if room.occupants:
                    for p in room.occupants:
                        print p.name
                else:
                    print "This room has no occupants."
                print self.space

        pass

    def save_state(self, *args):
        pass

    def load_state(self, *args):
        pass
