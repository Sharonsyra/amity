from room import Room


class Office(Room):
    """Class office that inherits class Room."""

    def __init__(self, room_name, room_type="office", room_capacity=6):
        super(Office, self).__init__(room_name, room_type, room_capacity)
        self.room_members = []

    def __repr__(self):
        return "Office %s" % self.room_name
