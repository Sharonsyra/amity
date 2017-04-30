class Room(object):
    """ super class room """

    def __init__(self, room_name, room_capacity=None, room_type=None):
        self.room_id = id(self)
        self.room_name = room_name
        self.room_capacity = room_capacity
        self.room_type = room_type

    def __repr__(self):
        return "<Room %s>" % self.room_name

