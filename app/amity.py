import random
import sqlite3

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
        rooms = ""
        for room in room_list:
            if room in [room_object.room_name for room_object in self.rooms]:
                print("cannot create room {} . The room already exists.".format(room))
                rooms += "cannot create room {} . The room already exists.".format(room)

            else:
                if room_type == "office":
                    office = Office(room)
                    self.rooms.append(office)
                    self.offices.append(office)
                    print("Office {} of id - {} successfully created".format(office.room_name.upper(), office.room_id))
                    rooms += "Office {} of id - {} successfully created".format(office.room_name.upper(), office.room_id)

                elif room_type == "living_space":
                    living_space = LivingSpace(room)
                    self.rooms.append(living_space)
                    self.living_spaces.append(living_space)
                    print("Living Space {} of id - {} successfully created".format(living_space.room_name,
                                                                                   living_space.room_id))
                    rooms += "Living Space {} of id - {} successfully created".format(living_space.room_name,
                                                                                   living_space.room_id)
        return rooms

    def add_person(self, first_name, last_name, person_type, wants_accommodation):
        people = ""
        if person_type.lower() == "staff":
            staff = Staff(first_name, last_name)
            # add staff to people
            self.people.append(staff)
            self.staff.append(staff)
            print("{} {} of id {} has been added to the system".format(staff.first_name, staff.last_name, staff.person_id))
            people += "{} {} of id {} has been added to the system".format(staff.first_name, staff.last_name, staff.person_id)

            # Allocate staff to a random empty office
            if len([room_object for room_object in self.offices if len(room_object.room_members) < room_object.room_capacity]) > 0:
                office_allocated = random.choice([i for i in self.offices if len(i.room_members) < i.room_capacity])
                office_allocated.room_members.append(staff)
                print("{} {} has been allocated {}".format(staff.first_name, staff.last_name, office_allocated))
                people += "{} {} has been allocated {}".format(staff.first_name, staff.last_name, office_allocated)
            else:
                self.waiting_list.append(staff)
                self.office_waiting_list.append(staff)
                print("{} {} has been added to the office waiting list".format(staff.first_name, staff.last_name))
                people += "{} {} has been added to the office waiting list".format(staff.first_name, staff.last_name)

            if wants_accommodation == "Y":
                print("Staff cannot be allocated a living space!")
                people += "Staff cannot be allocated a living space!"

        elif person_type.lower() == "fellow":
            fellow = Fellow(first_name, last_name)
            # add fellow to people
            self.people.append(fellow)
            self.fellows.append(fellow)
            people += "{} {} of id {} has been added to the system".format(first_name, last_name, fellow.person_id)
            print("{} {} of id {} has been added to the system".format(first_name, last_name, fellow.person_id))
            # Give them an office first
            if len([i for i in self.offices if len(i.room_members) < i.room_capacity]) > 0:
                office_allocated = random.choice([i for i in self.offices if len(i.room_members) < i.room_capacity])
                office_allocated.room_members.append(fellow)
                print("{} {} has been allocated {}".format(fellow.first_name, fellow.last_name, office_allocated))
                people += "{} {} has been allocated {}".format(fellow.first_name, fellow.last_name, office_allocated)
            else:
                self.waiting_list.append(fellow)
                self.office_waiting_list.append(fellow)
                print("{} {} has been added to the office waiting list".format(fellow.first_name, fellow.last_name))
                people += "{} {} has been added to the office waiting list".format(fellow.first_name, fellow.last_name)

            if wants_accommodation == "Y":
                # Get the list of available living spaces
                if len([i for i in self.living_spaces if len(i.room_members) < i.room_capacity]) > 0:
                    living_space_allocated = random.choice([i for i in self.living_spaces if len(i.room_members) < i.room_capacity])
                    living_space_allocated.room_members.append(fellow)
                    print("{} {} has been allocated {}".format(fellow.first_name, fellow.last_name,
                                                               living_space_allocated))
                    people += "{} {} has been allocated {}".format(fellow.first_name, fellow.last_name,
                                                               living_space_allocated)

                else:
                    self.waiting_list.append(fellow)
                    self.living_space_waiting_list.append(fellow)
                    print("{} {} has been added to the living space waiting list".format(fellow.first_name,
                                                                                         fellow.last_name))
                    people += "{} {} has been added to the living space waiting list".format(fellow.first_name,
                                                                                     fellow.last_name)
        else:
            print("Person type can only be fellow or staff")
            people += "Person type can only be fellow or staff"

        return people

    def print_person_id(self):
        for person in self.people:
            print("{} {} {}".format(person.person_id, person.first_name, person.last_name))
            return "{} {} {}".format(person.person_id, person.first_name, person.last_name)

    def person_object(self, person_identifier):
        if person_identifier in [p.person_id for p in self.people]:
            for p in [p for p in self.people]:
                return p
        else:
            return None

    def check_room(self, new_room):
        new_room_object = [room for room in self.rooms if room.room_name == new_room]
        if len(new_room_object):
            room = new_room_object[0]
            return room
        else:
            return 'Room does not exist'

    def check_old_office(self, person):
        for room in self.offices:
            if person in [p for p in room.room_members]:
                return room

    def check_old_living_space(self, person):
        for room in self.living_spaces:
            if person in [p for p in room.room_members]:
                return room

    def reallocate_person(self, person_identifier, new_room):
        person = self.person_object(person_identifier)
        """Check if person identifier exists"""
        if person:
            old_office = self.check_old_office(person)
            old_living_space = self.check_old_living_space(person)
            new_rm = self.check_room(new_room)
            """Check if room exists"""
            if new_rm == "Room does not exist":
                print("Sorry. Room {} does not exist in the system.".format(new_room))
                return "Sorry. Room {} does not exist in the system.".format(new_room)

            if len(new_rm.room_members) >= new_rm.room_capacity:
                print("The room is fully occupied")
                return "The room is fully occupied"

            if person in [p for p in new_rm.room_members]:
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
                        print("{} {} of id {} has been reallocated from {} to {}".format(
                            person.first_name, person.last_name, person_identifier, old_living_space, new_room))
                        return "{} {} of id {} has been reallocated from {} to {}".format(
                            person.first_name, person.last_name, person_identifier, old_living_space, new_room)
                    else:
                        if person in self.living_space_waiting_list:
                            new_rm.room_members.append(person)
                            print("{} {} of id {} has been allocated to {}".format(person.first_name,
                                                                                   person.last_name,
                                                                                   person_identifier, new_room))
                            return "{} {} of id {} has been allocated to {}".format(person.first_name,
                                                                                   person.last_name,
                                                                                   person_identifier, new_room)
                        else:
                            pass

            """Office reallocation"""
            if new_rm in self.offices:
                if old_office:
                    new_rm.room_members.append(person)
                    old_office.room_members.remove(person)
                    print("{} {} of id {} has been reallocated from {} to {}".format(
                        person.first_name, person.last_name, person_identifier, old_office, new_room))
                    return "{} {} of id {} has been reallocated from {} to {}".format(
                        person.first_name, person.last_name, person_identifier, old_office, new_room)
                else:
                    if person in self.office_waiting_list:
                        new_rm.room_members.append(person)
                        print("{} {} of id {} has been allocated to {}".format(
                            person.first_name, person.last_name, person_identifier, new_room))
                        return "{} {} of id {} has been allocated to {}".format(
                            person.first_name, person.last_name, person_identifier, new_room)
                    else:
                        pass
        else:
            print("Sorry the person identifier does not exist in the system")
            return "Sorry the person identifier does not exist in the system"

    def load_people(self, txt_file=None):
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
                    self.add_person(first_name, last_name, person_type, wants_accommodation)
                    print("\n")
        except IOError:
            print("File not found")

    def print_allocations(self, args=None):
        allocations = ""
        for room in self.rooms:
            if len(room.room_members) != 0:
                allocations += "\n"
                allocations += room.room_name
                allocations += "\n"
                allocations += "---------------------------------------\n"
                for person in room.room_members:
                    allocations += "{} {}\n".format(person, person.person_id)
            elif len(room.room_members) == 0:
                allocations += "There are no people in the system"
                break
        if not self.rooms:
            allocations += "There are no rooms in the system. Create rooms and add people to display the allocations"
            allocations += "\n"
        print(allocations)

        if args:
            with open(args, "w") as allocated_file:
                allocated_file.write(allocations)

    def print_unallocated(self, args=None):
        un_allocations = ""
        if len(self.waiting_list) == 0:
            un_allocations += "There are no unallocated people"
        elif len(self.waiting_list) != 0:
            un_allocations += "Office waiting list\n"
            un_allocations += "---------------------------------------\n"
            for person in self.office_waiting_list:
                un_allocations += "{0} {1}\n".format(person, person.person_id)
            un_allocations += "Living Space waiting list\n"
            un_allocations += "---------------------------------------\n"
            for person in self.living_space_waiting_list:
                un_allocations += "{0} {1}\n".format(person, person.person_id)
        print(un_allocations)

        if args:
            with open(args, "w") as unallocated_file:
                unallocated_file.write(un_allocations)

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

    def save_state(self, database="amity.db"):
        database = database if database else "amity.db"
        connection = sqlite3.connect(database)
        cc = connection.cursor()
        cc.execute('''DROP TABLE IF EXISTS room''')
        cc.execute('''CREATE TABLE room( room_id INTEGER , room_name text, room_capacity INTEGER , room_type text, allocations text )''')
        for room in self.rooms:
            allocations = ""
            room_id = room.room_id
            room_name = room.room_name
            room_capacity = room.room_capacity
            room_type = room.room_type
            for person in room.room_members:
                allocations += person.first_name + " " + person.last_name + "," + " "
            cc.execute("INSERT INTO room (room_id, room_name, room_capacity, room_type, allocations) VALUES (?,?,?,?,?)",
                         (room_id, room_name, room_capacity, room_type, allocations))

        cc.execute('''DROP TABLE IF EXISTS person''')
        cc.execute(
            '''CREATE TABLE person(person_id INTEGER , first_name text, last_name text, person_type text, wants_accommodation text )''')

        for person in self.people:
            person_id = person.person_id
            first_name = person.first_name
            last_name = person.last_name
            person_type = person.person_type
            wants_accommodation = person.wants_accommodation
            cc.execute("INSERT INTO person (person_id, first_name, last_name, person_type, wants_accommodation) VALUES (?,?,?,?,?)",
                (person_id, first_name, last_name, person_type, wants_accommodation))

        cc.execute("""DROP TABLE IF EXISTS office_waiting_list""")
        cc.execute("""CREATE TABLE office_waiting_list
                             (person_type text, first_name text, last_name text, person_id INTEGER)""")
        for person in self.office_waiting_list:
            person_type = person.person_type
            first_name = person.first_name
            last_name = person.last_name
            person_id = person.person_id
            cc.execute("INSERT INTO office_waiting_list (person_type, first_name, last_name, person_id) VALUES (?,?,?,?)",
                         (person_type, first_name, last_name, person_id))

        cc.execute("""DROP TABLE IF EXISTS living_space_waiting_list""")
        cc.execute("""CREATE TABLE living_space_waiting_list
                                     (person_type text, first_name text, last_name text, person_id   INTEGER)""")
        for person in self.living_space_waiting_list:
            person_type = person.person_type
            first_name = person.first_name
            last_name = person.last_name
            person_id = person.person_id
            cc.execute("INSERT INTO living_space_waiting_list (person_type, first_name, last_name, person_id) VALUES (?,?,?,?)",
                       (person_type, first_name, last_name, person_id))

        connection.commit()
        connection.close()
        print "Data successfully saved to database!"

    def load_state(self, database="amity.db"):
        database = database if database else "amity.db"
        connection = sqlite3.connect(database)
        cc = connection.cursor()
        cc.execute("SELECT * FROM person")
        people = cc.fetchall()
        for person in people:
            if person[2] == 'staff':
                staff = Staff(person[1], person[2], person[3])
                staff.id = person[0]
                self.people.append(staff)

            else:
                fellow = Fellow(person[1], person[2], person[3])
                fellow.id = person[0]
                self.people.append(fellow)

        cc.execute("SELECT * FROM room")
        rooms = cc.fetchall()
        for room in rooms:
            if room[2] == 6:
                office = Office(room[1], room[3])
                office.id = room[0]
                self.rooms.append(office)
            else:
                living_space = LivingSpace(room[1], room[3])
                living_space.id = room[0]
                self.rooms.append(living_space)

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


