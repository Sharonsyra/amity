class Person(object):
    """ Class person adds people to amity """

    def __init__(self, first_name, last_name):
        self.p_id = id(self)
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return "<Person %s %s>" % (self.first_name, self.last_name)
