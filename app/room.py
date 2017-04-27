class Room(object):
    """ super class room """

    def __init__(self, room_name):
        self.room_id = id(self)
        self.room_name = room_name

    def __repr__(self):
        return "<Room %s>" % self.room_name

    @property
    def room_type(self):
        return self.__class__.__name__