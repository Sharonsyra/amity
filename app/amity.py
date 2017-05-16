import logging
import os
import random
import sqlite3

from office import Office
from living_space import LivingSpace
from fellow import Fellow
from staff import Staff


class Amity(object):
    """Amity class has functions that create rooms, add people, allocate
    people to rooms, reallocate people to different rooms, load people
    and print allocated and unallocated people"""

    def __init__(self):
        """Amity class constructor"""
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
        """Function to create offices and living spaces!"""
        rooms = ""
        for room in room_list:
            if room in [room_object.room_name for room_object in self.rooms]:
                print("cannot create room {} . The room already exists."
                      .format(room))
                rooms += "cannot create room {} . The room already exists."\
                    .format(room)

            else:
                if room_type == "office":
                    office = Office(room)
                    self.rooms.append(office)
                    self.offices.append(office)
                    print("Office {} of id - {} successfully created"
                          .format(office.room_name.upper(), office.room_id))
                    rooms += "Office {} of id - {} successfully created"\
                        .format(office.room_name.upper(), office.room_id)

                elif room_type == "living_space":
                    living_space = LivingSpace(room)
                    self.rooms.append(living_space)
                    self.living_spaces.append(living_space)
                    print("Living Space {} of id - {} successfully created"
                          .format(living_space.room_name,
                                  living_space.room_id))
                    rooms += "Living Space {} of id - {} successfully "\
                             "created"\
                        .format(living_space.room_name, living_space.room_id)
        return rooms

    def add_person(self, first_name, last_name, person_type,
                   wants_accommodation):
        """Function to add a person to the system, allocate them to rooms and/or
        living spaces and add them to the waiting list if full rooms"""
        people = ""
        if person_type.lower() == "staff":
            staff = Staff(first_name, last_name)
            # add staff to people
            self.people.append(staff)
            self.staff.append(staff)
            print("{} {} of id {} has been added to the system"
                  .format(staff.first_name, staff.last_name, staff.person_id))
            people += "{} {} of id {} has been added to the system"\
                .format(staff.first_name, staff.last_name, staff.person_id)

            # Allocate staff to a random empty office
            if len([room_object for room_object in self.offices if
                   len(room_object.room_members) < room_object.room_capacity]):
                office_allocated = random.choice([room_object for room_object
                                                  in self.offices if
                                                  len(room_object.room_members) <
                                                  room_object.room_capacity])
                office_allocated.room_members.append(staff)
                print("{} {} has been allocated {}"
                      .format(staff.first_name, staff.last_name,
                              office_allocated))
                people += "{} {} has been allocated {}"\
                    .format(staff.first_name, staff.last_name,
                            office_allocated)
            else:
                self.waiting_list.append(staff)
                self.office_waiting_list.append(staff)
                print("{} {} has been added to the office waiting list"
                      .format(staff.first_name, staff.last_name))
                people += "{} {} has been added to the office waiting list"\
                    .format(staff.first_name, staff.last_name)

            if wants_accommodation == "Y":
                print("Staff cannot be allocated a living space!")
                people += "Staff cannot be allocated a living space!"

        elif person_type.lower() == "fellow":
            fellow = Fellow(first_name, last_name)
            # add fellow to people
            self.people.append(fellow)
            self.fellows.append(fellow)
            people += "{} {} of id {} has been added to the system"\
                .format(first_name, last_name, fellow.person_id)
            print("{} {} of id {} has been added to the system"
                  .format(first_name, last_name, fellow.person_id))
            # Give them an office first
            if len([room_object for room_object in self.offices if
                    len(room_object.room_members)
                    < room_object.room_capacity]):
                office_allocated = random.choice([room_object for room_object in
                                                  self.offices if
                                                  len(room_object.room_members)
                                                  < room_object.room_capacity])
                office_allocated.room_members.append(fellow)
                print("{} {} has been allocated {}"
                      .format(fellow.first_name, fellow.last_name,
                              office_allocated))
                people += "{} {} has been allocated {}"\
                    .format(fellow.first_name, fellow.last_name,
                            office_allocated)
            else:
                self.waiting_list.append(fellow)
                self.office_waiting_list.append(fellow)
                print("{} {} has been added to the office waiting list"
                    .format(fellow.first_name, fellow.last_name))
                people += "{} {} has been added to the office waiting list"\
                    .format(fellow.first_name, fellow.last_name)

            if wants_accommodation == "Y":
                # Get the list of available living spaces
                if len([room_object for room_object in self.living_spaces if
                        len(room_object.room_members)
                       < room_object.room_capacity]):
                    living_space_allocated = \
                        random.choice([room_object for room_object in
                                       self.living_spaces if
                                       len(room_object.room_members) <
                                       room_object.room_capacity])
                    living_space_allocated.room_members.append(fellow)
                    print("{} {} has been allocated {}"
                          .format(fellow.first_name, fellow.last_name,
                                  living_space_allocated))
                    people += "{} {} has been allocated {}"\
                        .format(fellow.first_name, fellow.last_name,
                                living_space_allocated)

                else:
                    self.waiting_list.append(fellow)
                    self.living_space_waiting_list.append(fellow)
                    print("{} {} has been added to the living space "
                          "waiting list".format(fellow.first_name,
                                                fellow.last_name))
                    people += "{} {} has been added to the living space "\
                              "waiting list".format(fellow.first_name,
                                                    fellow.last_name)
        else:
            print("Person type can only be fellow or staff")
            people += "Person type can only be fellow or staff"

        return people

    def print_person_id(self):
        """Function to print people in amity details"""
        for person in self.people:
            print("{} {} {}".format(person.person_id, person.first_name,
                                    person.last_name))

    def person_object(self, person_identifier):
        """Function to return a person object form the person identifier"""
        if person_identifier in [person.person_id for person in self.people]:
            for person in [person for person in self.people]:
                return person
        else:
            return None

    def check_room(self, new_room):
        """Function to check if a room exists in amity."""
        new_room_object = [room for room in self.rooms if room.room_name ==
                           new_room]
        if len(new_room_object):
            room = new_room_object[0]
            return room
        else:
            return 'Room does not exist'

    def check_old_office(self, person):
        """Function to check the current allocated office"""
        for room in self.offices:
            if person in [person for person in room.room_members]:
                return room

    def check_old_living_space(self, person):
        """Function to check the current allocated living space"""
        for room in self.living_spaces:
            if person in [person for person in room.room_members]:
                return room

    def allocate(self):
        """Function to allocate people in the office and living space waiting
         list"""
        allocate = ""
        if len([room_object for room_object in self.offices if
                len(room_object.room_members) < room_object.room_capacity]):
            if len(self.office_waiting_list):
                for person in self.office_waiting_list:

                    office_allocated = random.choice([room for room in
                                                      self.offices if
                                                      len(room.room_members) <
                                                      room.room_capacity])
                    office_allocated.room_members.append(person)
                    self.office_waiting_list.remove(person)
                    print("{} {} of id {} has been allocated {}"
                          .format(person.first_name, person.last_name,
                                  person.person_id, room))
                    allocate += "{} {} of id {} has been allocated {}"\
                        .format(person.first_name, person.last_name,
                                person.person_id, room)
            else:
                print("There are no people in the office waiting list")
        else:
            print("There are no available offices at the moment")

        if len([room_object for room_object in self.living_spaces if
                len(room_object.room_members) < room_object.room_capacity]):
            if len(self.living_space_waiting_list):
                for person in self.living_space_waiting_list:
                    living_space_allocated = \
                        random.choice([room for room in self.living_spaces if
                                       len(room.room_members) <
                                       room.room_capacity])
                    living_space_allocated.room_members.append(person)
                    self.living_space_waiting_list.remove(person)
                    print("{} {} of id {} has been allocated {}"
                          .format(person.first_name, person.last_name,
                                  person.person_id, living_space_allocated))
                    allocate += "{} {} of {} has been allocated {}"\
                        .format(person.first_name, person.last_name,
                                person.person_id, living_space_allocated)
            else:
                print("There are no people in the living space waiting list")
        else:
            print("There are no available living spaces at the moment")
            allocate += "There are no available living spaces at the moment"

        return allocate

    def reallocate_person(self, person_identifier, new_room):
        """Function to reallocate individuals from one room to another"""
        person = self.person_object(person_identifier)
        """Check if person identifier exists"""
        if person:
            old_office = self.check_old_office(person)
            old_living_space = self.check_old_living_space(person)
            new_rm = self.check_room(new_room)
            """Check if room exists"""
            if new_rm == "Room does not exist":
                print("Sorry. Room {} does not exist in the system."
                      .format(new_room))
                return "Sorry. Room {} does not exist in the system."\
                    .format(new_room)

            if len(new_rm.room_members) >= new_rm.room_capacity:
                print("The room is fully occupied")
                return "The room is fully occupied"

            if person in [person for person in new_rm.room_members]:
                print("The person is already a room member!")
                return "The person is already a room member!"

            """Living space reallocation"""
            if new_rm in self.living_spaces:
                if person in self.staff:
                    print("Staff cannot be allocated to living spaces!")
                    return "Staff cannot be allocated to living spaces!"
                elif person in self.fellows:
                    if old_living_space:
                        new_rm.room_members.append(person)
                        old_living_space.room_members.remove(person)
                        print("{} {} of id {} has been reallocated "\
                              "from {} to {}".format(person.first_name,
                                                     person.last_name,
                                                     person_identifier,
                                                     old_living_space,
                                                     new_room))
                        return "{} {} of id {} has been reallocated "\
                               "from {} to {}".format(person.first_name,
                                                      person.last_name,
                                                      person_identifier,
                                                      old_living_space,
                                                      new_room)
                    elif old_living_space is None:
                        print("Person is not allocated to a living space "\
                              "allocate the person using allocate")

            """Office reallocation"""
            if new_rm in self.offices:
                if old_office:
                    new_rm.room_members.append(person)
                    old_office.room_members.remove(person)
                    print("{} {} of id {} has been reallocated from {} "\
                          "to {}".format(person.first_name, person.last_name,
                                         person_identifier, old_office, 
                                         new_room))
                    return "{} {} of id {} has been reallocated from {} "\
                           "to {}".format(person.first_name, person.last_name,
                                          person_identifier, old_office,
                                          new_room)
                elif old_office is None:
                    print("Person is not allocated to an office "\
                          "allocate the person using allocate")

        else:
            print("Sorry the person identifier does not exist in the system")
            return "Sorry the person identifier does not exist in the system"

    def load_people(self, txt_file=None):
        """Function to load people from a text file"""
        txt_file = './files/' + txt_file
        try:
            try:
                with open(txt_file, 'r') as person_file:
                    for line in person_file:
                        first_name = line.split()[0]
                        last_name = line.split()[1]
                        person_type = line.split()[2].lower()
                        if len(line.split()) == 4:
                            wants_accommodation = line.split()[3].upper()
                        else:
                            wants_accommodation = "N"
                        self.add_person(first_name, last_name, person_type,
                                        wants_accommodation)
                        print("\n")
                    print("Data successfully loaded to amity!")
            except IndexError:
                print("The file does not have specified data!")
        except IOError:
            print("File not found")

    def print_allocations(self, args=None):
        """Function to print occupied rooms and their occupants to a text
        file and to the screen"""
        allocations = ""
        for room in self.rooms:
            if len(room.room_members):
                allocations += "These are the rooms and their allocations"
                allocations += "\n"
                allocations += room.room_name
                allocations += "\n"
                allocations += "---------------------------------------\n"
                for person in room.room_members:
                    allocations += "{} {}\n".format(person, person.person_id)
        if not self.rooms:
            allocations += "There are no rooms in the system. Create rooms"\
                           " and add people to display the allocations"
            allocations += "\n"
        print(allocations)

        if args:
            txt = './files/'+args
            with open(txt, "w") as allocated_file:
                allocated_file.write(allocations)
                allocations += "Data has been dumped to file"
        return allocations

    def print_unallocated(self, args=None):
        """Function to print people in the waiting list to text file and to
         the screen"""
        un_allocations = ""
        if len(self.waiting_list) == 0:
            print("There are no people in the waiting list!")
        if len(self.waiting_list):
            un_allocations += "These are the people in the waiting list\n"
            un_allocations += "Office waiting list\n"
            un_allocations += "---------------------------------------\n"
            for person in self.office_waiting_list:
                un_allocations += "{} {}\n".format(person, person.person_id)
            un_allocations += "Living Space waiting list\n"
            un_allocations += "---------------------------------------\n"
            for person in self.living_space_waiting_list:
                un_allocations += "{} {}\n".format(person, person.person_id)
        print(un_allocations)

        if args:
            txt = './files/' + args
            with open(txt, "w") as unallocated_file:
                unallocated_file.write(un_allocations)
                un_allocations += "Data has been dumped to file"
        return un_allocations

    def print_room(self, room):
        """Function that outputs the occupants of a room"""
        if room in [i.room_name for i in self.rooms]:
            print(room)
            print("---------------------------------------")
            for r in self.rooms:
                if room in r.room_name:
                    for person in r.room_members:
                        print person, person.person_id
        else:
            print("The room does not exist in the system")
        return self

    def save_state(self, database="amity.db"):
        """Function to save people to a database"""
        if database:
            database = './files/' + database
        else:
            database = './files/'
        database = database if database else "amity.db"
        connection = sqlite3.connect(database)
        cc = connection.cursor()
        cc.execute('''DROP TABLE IF EXISTS room''')
        cc.execute('''CREATE TABLE room( room_id INTEGER , room_name text,
 room_capacity INTEGER , room_type text, allocations text )''')
        for room in self.rooms:
            allocations = []
            room_id = room.room_id
            room_name = room.room_name
            room_capacity = room.room_capacity
            room_type = room.room_type
            for person in room.room_members:
                allocations.append(str(person.person_id))
            allocations = ",".join(allocations)
            cc.execute("INSERT INTO room (room_id, room_name, room_capacity,"
                       " room_type, allocations) VALUES (?,?,?,?,?)",
                         (room_id, room_name, room_capacity, room_type, 
                          allocations))

        cc.execute('''DROP TABLE IF EXISTS person''')
        cc.execute(
            '''CREATE TABLE person(person_id INTEGER , first_name text, 
last_name text, person_type text, wants_accommodation text )''')

        for person in self.people:
            person_id = person.person_id
            first_name = person.first_name
            last_name = person.last_name
            person_type = person.person_type
            wants_accommodation = person.wants_accommodation
            cc.execute("INSERT INTO person (person_id, first_name, last_name,"
                       "person_type, wants_accommodation) VALUES (?,?,?,?,?)",
                (person_id, first_name, last_name, person_type, 
                 wants_accommodation))

        cc.execute("""DROP TABLE IF EXISTS office_waiting_list""")
        cc.execute("""CREATE TABLE office_waiting_list
                             (person_type text, first_name text, last_name text, 
                             person_id INTEGER)""")
        for person in self.office_waiting_list:
            person_type = person.person_type
            first_name = person.first_name
            last_name = person.last_name
            person_id = person.person_id
            cc.execute("INSERT INTO office_waiting_list (person_type,"\
                " first_name, last_name, person_id) VALUES (?,?,?,?)",
                         (person_type, first_name, last_name, person_id))

        cc.execute("""DROP TABLE IF EXISTS living_space_waiting_list""")
        cc.execute("""CREATE TABLE living_space_waiting_list
                                     (person_type text, first_name text, 
                                     last_name text, person_id   INTEGER)""")
        for person in self.living_space_waiting_list:
            person_type = person.person_type
            first_name = person.first_name
            last_name = person.last_name
            person_id = person.person_id
            cc.execute("INSERT INTO living_space_waiting_list (person_type, "
                       "first_name, last_name, person_id) VALUES (?,?,?,?)",
                       (person_type, first_name, last_name, person_id))

        connection.commit()
        connection.close()
        print "Data successfully saved to database!"

    def load_state(self, database=None):
        database = './files/' + database
        """Function to load people from a database"""
        try:
            db = database if database else "amity.db"
            connection = sqlite3.connect(db)
            cc = connection.cursor()
            cc.execute("SELECT * FROM person")
            people = cc.fetchall()
            for person in people:
                if person[2] == 'staff':
                    staff = Staff(person[1], person[2], person[3])
                    staff.person_id = person[0]
                    self.people.append(staff)
                    self.staff.append(staff)

                else:
                    fellow = Fellow(person[1], person[2], person[3])
                    fellow.person_id = person[0]
                    self.people.append(fellow)
                    self.fellows.append(fellow)

            cc.execute("SELECT * FROM room")
            rooms = cc.fetchall()
            for room in rooms:
                if room[2] == 6:
                    office = Office(room[1])
                    office.room_id = room[0]
                    office.room_members = [person for person in self.people if
                                           person.person_id in [int(str(person_id))
                                                                for person_id in
                                                                room[4].split(',')]
                                           ]
                    self.rooms.append(office)
                    self.offices.append(office)
                else:
                    living_space = LivingSpace(room[1])
                    living_space.room_id = room[0]
                    living_space.room_members = [person for person in self.people
                                                 if person.person_id in
                                                 [int(str(person_id)) for
                                                  person_id in room[4].split(',')]
                                                 ]
                    self.rooms.append(living_space)
                    self.living_spaces.append(living_space)

            cc.execute("SELECT * FROM office_waiting_list")
            office_waiting_list = cc.fetchall()
            for person_object in office_waiting_list:
                for individual in self.people:
                    if individual.id == person_object[3]:
                        self.waiting_list.append(individual)
                        self.office_waiting_list.append(individual)

            cc.execute("SELECT * FROM living_space_waiting_list")
            living_space_waiting_list = cc.fetchall()
            for person_object in living_space_waiting_list:
                for individual in self.people:
                    if individual.id == person_object[3]:
                        self.waiting_list.append(individual)
                        self.living_space_waiting_list.append(individual)

            connection.commit()
            connection.close()
            print("Data successfully loaded to amity!")
        except Exception as error:
            print(error)
