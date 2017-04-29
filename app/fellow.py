from person import Person


class Fellow(Person):
    """Class fellow that inherits class Person."""
    def __init__(self, first_name, last_name):
        super(Fellow, self).__init__(first_name, last_name)

    def __repr__(self):
        return "Fellow {} {}".format(self.first_name, self.last_name)

