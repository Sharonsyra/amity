from room import Room


class Office(Room):
    """Class living space that inherits class Room."""

    def __init__(self, room_name):
        super(Office, self).__init__(room_name)

    def __repr__(self):
        return "Office % s" % self.room_name
