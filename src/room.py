# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, room_name, description, n_to=None, s_to=None, e_to=None, w_to=None, items=None):
        self.room_name = room_name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
