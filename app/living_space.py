from room import Room


class LivingSpace(Room):
    """Class living space that inherits class Room."""

    def __init__(self, room_name):
        super(LivingSpace,self).__init__(room_name)

    def __repr__(self):
        return "LivingSpace %s" % self.room_name