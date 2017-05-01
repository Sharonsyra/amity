from room import Room


class LivingSpace(Room):
    """Class living space that inherits class Room."""

    def __init__(self, room_name, room_type="living_space"):
        super(LivingSpace, self).__init__(room_name, room_type)
        self.room_capacity = 4
        self.room_members = []

    def __repr__(self):
        return "Living Space %s" % self.room_name
