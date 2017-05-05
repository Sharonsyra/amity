import random

from office import Office
from living_space import LivingSpace
from fellow import Fellow
from staff import Staff


class Amity(object):
    """Amity class has functions that create rooms, add people, allocate people to rooms, 
    reallocate people to different rooms, load people and print allocated and unallocated people"""
    def __init__(self):

        self.rooms = []
        self.offices = []
        self.living_spaces = []
        self.people = []
        self.allocated_people = []
        self.waiting_list = []
        self.office_waiting_list = []
        self.living_space_waiting_list = []
        self.fellows = []
        self.allocated_fellows = []
        self.staff = []
        self.allocated_staff = []

    def create_room(self, room_list, room_type):
        for room in room_list:
            if room in [i.room_name for i in self.rooms]:
                print("cannot create room {} . The room already exists.".format(room))
            else:
                if room_type == "office":
                    office = Office(room)
                    self.rooms.append(office)
                    self.offices.append(office)
                    print("Office {} of id - {} successfully created".format(office.room_name, office.room_id))

                elif room_type == "living_space":
                    living_space = LivingSpace(room)
                    self.rooms.append(living_space)
                    self.living_spaces.append(living_space)
                    print("Living Space {} of id - {} successfully created".format(living_space.room_name,
                                                                                   living_space.room_id))

    def add_person(self, first_name, last_name, person_type, wants_accommodation=None):
        if person_type == "staff":
            staff = Staff(first_name, last_name)
            # add staff to people
            self.people.append(staff)
            self.staff.append(staff)
            print("{} {} of id {} has been added to the system".format(staff.first_name, staff.last_name, staff.person_id))
            # Allocate staff to a random empty office
            if len([i for i in self.offices if len(i.room_members) < i.room_capacity]) > 0:
                office_allocated = random.choice([i for i in self.offices if len(i.room_members) < i.room_capacity])
                office_allocated.room_members.append(staff)
                print("{} {} has been allocated {}".format(staff.first_name, staff.last_name, office_allocated))
            else:
                self.waiting_list.append(staff)
                self.office_waiting_list.append(staff)
                print("{} {} has been added to the office waiting list".format(staff.first_name, staff.last_name))

        elif person_type == "fellow":
            fellow = Fellow(first_name, last_name)
            # add fellow to people
            self.people.append(fellow)
            self.fellows.append(fellow)
            print("{} {} of id {} has been added to the system".format(first_name, last_name, fellow.person_id))
            # Give them an office first
            if len([i for i in self.offices if len(i.room_members) < i.room_capacity]) > 0:
                office_allocated = random.choice([i for i in self.offices if len(i.room_members) < i.room_capacity])
                office_allocated.room_members.append(fellow)
                print("{} {} has been allocated {}".format(fellow.first_name, fellow.last_name, office_allocated))
            else:
                self.waiting_list.append(fellow)
                self.office_waiting_list.append(fellow)
                print("{} {} has been added to the office waiting list".format(fellow.first_name, fellow.last_name))

            if wants_accommodation == "Y":
                # Get the list of available living spaces
                if len([i for i in self.living_spaces if len(i.room_members) < i.room_capacity]) > 0:
                    living_space_allocated = random.choice([i for i in self.living_spaces if len(i.room_members) < i.room_capacity])
                    living_space_allocated.room_members.append(fellow)
                    print("{} {} has been allocated {}".format(fellow.first_name, fellow.last_name,
                                                               living_space_allocated))

                else:
                    self.waiting_list.append(fellow)
                    self.living_space_waiting_list.append(fellow)
                    print("{} {} has been added to the living space waiting list".format(fellow.first_name,
                                                                                         fellow.last_name))
        return self

    def print_id(self):
        for person in [i for i in self.people]:
            print("{} {} {}".format(person.person_id, person.first_name, person.last_name))

    def reallocate_person(self, identifier, new_room):
        fellow = Staff(identifier)
        staff = Staff(identifier)
        if identifier in [i.person_id for i in self.people]:
            if new_room in [i.room_name for i in self.rooms]:
                if new_room in [i for i in self.rooms if len(i.room_members) < i.room_capacity]:
                    if identifier in [i.person_id for i in self.fellows]:
                        if new_room in [i.room_name for i in self.offices]:
                            if identifier in [i.person_id for i in [i.room_members for i in self.offices]]:
                                print("You cannot reallocate to the same office!")
                            else:
                                office_allocated = new_room
                                office_allocated.room_members(fellow)
                                print("The ")
                        elif new_room in [i.room_name for i in self.living_spaces]:
                            if identifier in [i.person_id for i in [i.room_members for i in self.offices]]:
                                print("You cannot reallocate to the same living space!")
                            else:
                                living_space_allocated = new_room
                                living_space_allocated.room_members(fellow)
                    elif identifier in [i.person_id for i in self.staff]:
                        if identifier in [i.person_id for i in [i.room_members for i in self.offices]]:
                            print("You cannot reallocate to the same office!")
                        else:
                            office_allocated = new_room
                            office_allocated.room_members.append(staff)
                else:
                    print("The room you entered is fully occupied")
            else:
                print("The room is not in the system!")
        else:
            "The person id is not available"
        return

    def load_people(self, txt_file=None):
        with open(txt_file, 'r') as person_file:
            for line in person_file:
                first_name = line.split()[0]
                last_name = line.split()[1]
                person_type = line.split()[2].lower()
                if len(line.split()) == 4:
                    wants_accommodation = line.split()[3].upper()
                else:
                    wants_accommodation = "N"
                self.add_person(first_name, last_name, person_type, wants_accommodation)
                print("\n")
        person_file.close
        return self

    def print_allocations(self, args=None):
        for room in self.rooms:
            print("\n")
            print(room.room_name)
            print("---------------------------------------")
            if len(room.room_members) == 0:
                print("This room is empty")
            else:
                for person in room.room_members:
                    print(person, person.person_id)
        if not new_amity.rooms:
            print("There are no rooms in the system. Create rooms and add people to display the allocations")
            print("\n")

        # if args:
        #     with open(args, "w") as allocations_file:
        #         for room in [i.room_name for i in self.rooms]:
        #             allocations_file.write(room + "\n")
        #             for person in [i.room_members for i in self.rooms]:
        #                 allocations_file.write("".join(person))
                          # allocations_file.write(person.first_name + " " + person.last_name + " " + person.person_type + " " + person.wants_accommodation + "\n")
        # else:
            # print("File does not exist")
        # if args:
        #     with open(args, 'w') as allocations_file:
        #         allocations_file.write(room.room_name)
        #         for r in [i.room_members for i in self.rooms]:
        #             allocations_file.write(r.room_members)
        #         # print("Allocations have been saved to {}".format(args))

    def print_unallocated(self, args=None):
        if len(self.waiting_list) == 0:
            print("There are no unallocated people")
        else:
            print("Office waiting list")
            print("---------------------------------------")
            for person in self.office_waiting_list:
                print(person, person.person_id)
            print("\n")
            print("Living Space waiting list")
            print("---------------------------------------")
            for person in self.living_space_waiting_list:
                print(person, person.person_id)

        if args:
            if args is True:
                with open(args, "w") as unallocated_file:
                    for person in self.office_waiting_list:
                        unallocated_file.write("Office Waiting List")
                        unallocated_file.write(person.first_name + " " + person.last_name + " " + person.person_type + " " +person.wants_accommodation +" " + "\n")

                    for person in self.living_space_waiting_list:
                        unallocated_file.write("Living Space Waiting List")
                        unallocated_file.write(person.first_name + " " + person.last_name + " " + person.person_type + " " + person.wants_accommodation + " " + "\n")
            else:
                print("File does not exist")
            return self

    def print_room(self, room):
        if room in [i.room_name for i in self.rooms]:
            print(room)
            print("---------------------------------------")
            for r in self.rooms:
                if room in r.room_name:
                    for person in r.room_members:
                        print(person, person.person_id)
        else:
            print("The room does not exist in the system")
        return self

new_amity = Amity()

new_amity.create_room(["Blue", "Red"], "office")
new_amity.create_room(["Mara"], "living_space")
# new_amity.add_person("Robley", "Gori", "fellow", "Y")
# new_amity.add_person("Ry", "Gi", "fellow", "N")
# new_amity.add_person("R", "G", "fellow", "Y")
# new_amity.add_person("Robley", "Gori", "fellow", "Y")
# new_amity.add_person("Robley", "Gori", "fellow", "Y")
# new_amity.add_person("Robley", "Gori", "staff", "Y")
# new_amity.add_person("Robley", "Gori", "fellow", "Y")
# new_amity.add_person("Robley", "Gori", "staff", "Y")
# new_amity.add_person("Robley", "Gori", "fellow", "Y")
# new_amity.add_person("Robley", "Gori", "fellow", "Y")
# new_amity.add_person("Rob", "Gori", "staff", "N")
new_amity.print_allocations()
print("\n")
new_amity.print_unallocated()
print("\n")
new_amity.print_room("Mara")
print("\n")
new_amity.load_people('people.txt')
new_amity.print_allocations('allocations.txt')
print("\n")
new_amity.print_unallocated('unallocated.txt')
print("\n")
new_amity.print_room("Mara")
print("\n")
# new_amity.reallocate_person(4469159248, "Red")
