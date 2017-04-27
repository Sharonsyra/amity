from person import Person


class Staff(Person):
    """Class fellow that inherits class Person."""

    def __init__(self):
        pass

class Fellow(Person):
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name
        self.person_type = "Fellow"

    def __repr__(self):
        return "Fellow {0} {1}".format(self.first_name, self.second_name)

