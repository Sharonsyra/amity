from abc import ABCMeta

class Person(object):
    """ Class person adds people to amity """
    __metaclass__ = ABCMeta

    def __init__(self, first_name, last_name, person_type=None,
                 wants_accommodation=""):
        self.person_id = id(self)
        self.first_name = first_name
        self.last_name = last_name
        self.person_type = person_type
        self.wants_accommodation = wants_accommodation

    def __repr__(self):
        return "<Person {} {}>".format(self.first_name,
                                       self.last_name)
