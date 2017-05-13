from abc import ABCMeta

class Room(object):
    """ super class room """
    __metaclass__ = ABCMeta

    def __init__(self, room_name, room_capacity=None, room_type=None,
                 room_members=[]):
        self.room_id = id(self)
        self.room_name = room_name
        self.room_capacity = room_capacity
        self.room_type = room_type
        self.room_members = room_members

    def __repr__(self):
        return "<Room {}>".format(self.room_name)
