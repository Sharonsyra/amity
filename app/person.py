class Person(object):
    def __init__(self, id, names, person_type):
        self.names = names
        self.person_type = person_type
        self.id = id(self)

    def __repr__(self):
        return "Person {}".format(self.id)


class Fellow(Person):
    def __init__(self, first_name, second_name, person_type="Fellow"):
        self.first_name = first_name
        self.second_name = second_name
        self.person_type = "Fellow"

    def __repr__(self):
        return "Fellow {0} {1}".format(self.first_name, self.second_name)


class Staff(Person):
    def __init__(self, first_name, second_name, person_type="Staff"):
        self.first_name = first_name
        self.second_name = second_name
        self.person_type = "Staff"

    def __repr__(self):
        return "Staff {0} {1}".format(self.first_name, self.second_name)

fellows = ["Gyan Mutugi"]
staff = ["Marlene Mwendwa"]
newFellow = Fellow("Robley", "Gori")
newStaff = Staff("Leah", "Mukiri")
fellows.append(newFellow)
staff.append(newStaff)
print(staff)
print(fellows)