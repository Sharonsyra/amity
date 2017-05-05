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
        self.fellows = []
        self.staff = []
        self.waiting_list = []
        self.office_waiting_list = []
        self.living_space_waiting_list = []

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
        return self

    def add_person(self, first_name, last_name, person_type, wants_accommodation=None):
        if person_type == "staff":
            staff = Staff(first_name, last_name)
            # add staff to people
            self.people.append(staff)
            self.staff.append(staff)
            print(
            "{} {} of id {} has been added to the system".format(staff.first_name, staff.last_name, staff.person_id))
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
                    living_space_allocated = random.choice(
                        [i for i in self.living_spaces if len(i.room_members) < i.room_capacity])
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

    def reallocate_person(self, person_identifier, new_room):
        person = [p for p in self.people if person_identifier is p.person_id][0].__dict__
        print("\n")
        print(person)
        current_room = [i for i in self.rooms if person_identifier in [p.person_id for p in i.room_members]][0].__dict__
        print(current_room)
        new_room_object = [room for room in self.rooms if new_room is room.room_name][0].__dict__
        print(new_room_object)
        if person in self.staff:
            if new_room_object in self.living_spaces:
                print("Staff cannot be reallocated to a living space!")
            elif current_room is False:
                print("We cannot reallocate you as you had no room to begin with")
            elif new_room_object not in [i.room_name for i in self.rooms if len(i.room_members) < i.room_capacity]:
                print("Sorry. The room is not available!")
            elif new_room_object in [i.room_name for i in self.rooms if len(i.room_members) < i.room_capacity]:
                current_room.room_members.remove(person)
                new_room_object.room_members.append(person)
                print("{} {} has been allocated to {}".format(person.first_name, person.last_name, new_room_object.room_name))
        elif person in self.fellows:
            if new_room in self.offices:
                if current_room is False:
                    print("We cannot reallocate you as you had no room to begin with")
                elif new_room_object.room_type is not current_room.room_type:
                    print("You can only be reallocated to the same room type as your current room!")
                elif new_room_object not in [i.room_name for i in self.rooms if len(i.room_members) < i.room_capacity]:
                    print("Sorry. The room is not available!")
                elif new_room_object in [i.room_name for i in self.rooms if len(i.room_members) < i.room_capacity]:
                    current_room.room_members.remove(person)
                    new_room_object.room_members.append(person)
                    print("{} {} has been allocated to {}".format(person.first_name, person.last_name,
                                                                  new_room_object.room_name))
            elif new_room in self.living_spaces:
                if current_room is False:
                    print("We cannot reallocate you as you had no room to begin with")
                elif new_room_object.room_type is not current_room.room_type:
                    print("You can only be reallocated to the same room type as your current room!")
                elif new_room_object not in [i.room_name for i in self.rooms if len(i.room_members) < i.room_capacity]:
                    print("Sorry. The room is not available!")
                elif new_room_object in [i.room_name for i in self.rooms if len(i.room_members) < i.room_capacity]:
                    current_room.room_members.remove(person)
                    new_room_object.room_members.append(person)
                    print("{} {} has been allocated to {}".format(person.first_name, person.last_name,
                                                                  new_room_object.room_name))

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
                        unallocated_file.write(
                            person.first_name + " " + person.last_name + " " + person.person_type + " " + person.wants_accommodation + " " + "\n")

                    for person in self.living_space_waiting_list:
                        unallocated_file.write("Living Space Waiting List")
                        unallocated_file.write(
                            person.first_name + " " + person.last_name + " " + person.person_type + " " + person.wants_accommodation + " " + "\n")
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

new_amity.create_room(["Blue"], "office")
# new_amity.create_room(["Mara"], "living_space")
# new_amity.add_person("Robley", "Gori", "fellow", "Y")
new_amity.add_person("Ry", "Gi", "fellow", "N")

new_amity.create_room(["Red"], "office")
# new_amity.add_person("R", "G", "fellow", "Y")
# new_amity.add_person("Robley", "Gori", "fellow", "Y")
# new_amity.add_person("Robley", "Gori", "fellow", "Y")
# new_amity.add_person("Robley", "Gori", "staff", "Y")
# new_amity.add_person("Robley", "Gori", "fellow", "Y")
# new_amity.add_person("Robley", "Gori", "staff", "Y")
# new_amity.add_person("Robley", "Gori", "fellow", "Y")
# new_amity.add_person("Robley", "Gori", "fellow", "Y")
# new_amity.add_person("Rob", "Gori", "staff", "N")


# new_amity.print_allocations()
# print("\n")
# new_amity.print_unallocated()
# print("\n")
# new_amity.print_room("Mara")
# print("\n")
# # new_amity.load_people('people.txt')
# new_amity.print_allocations('allocations.txt')
# print("\n")
# new_amity.print_unallocated('unallocated.txt')
# print("\n")
# new_amity.print_room("Mara")
# print("\n")


person_id = new_amity.rooms[0].room_members[0].person_id
# print("\n\n {}".format(person_id))
new_amity.reallocate_person(person_id, "Red")
