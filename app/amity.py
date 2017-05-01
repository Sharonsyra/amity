import os
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
        self.available_rooms = []
        self.offices = []
        self.available_offices = []
        self.living_spaces = []
        self.available_living_spaces = []
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

    def add_person(self, first_name, last_name, person_type, wants_accommodation):
        if person_type == "staff":
            staff = Staff(first_name, last_name)
            # add staff to people
            self.people.append(staff)
            self.staff.append(staff)
            print("{} {} has been added to the system".format(staff.first_name, staff.last_name))
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
            print("{} {} has been added to the system".format(first_name, last_name))
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
                    self.living_space_waiting_list.append(fellow)
                    print("{} {} has been added to the living space waiting list".format(fellow.first_name,
                                                                                         fellow.last_name))

        return self


# new_amity = Amity()
# new_amity.create_room(["Blue"], "office")
# new_amity.create_room(["Mara"], "living_space")
#
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
#
#
# for room in new_amity.rooms:
#     print (room.room_name)
#     print(room.room_members)
#     print("")
#
# print(new_amity.living_space_waiting_list)
# print(new_amity.office_waiting_list)
