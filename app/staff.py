from person import Person


class Staff(Person):
    """Class staff that inherits class Person."""

    def __init__(self, first_name, last_name, person_type="staff", wants_accommodation="N"):
        super(Staff, self).__init__(first_name, last_name, person_type, wants_accommodation)

    def __repr__(self):
        return "Staff {} {}".format(self.first_name, self.last_name)

