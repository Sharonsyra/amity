class Person(object):
    """ Class person adds people to amity """

    def __init__(self, id, f_name, s_name):
        self.p_id = id
        self.f_name = f_name
        self.s_name = s_name

    def __repr__(self):
        return "<Person %s>" % selfw