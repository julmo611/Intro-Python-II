# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, room_name, room_description, room_item):
        self.room_name = room_name
        self.room_description = room_description
        self.room_item = room_item

    def __str__(self):
        return str(self.__dict__)


# print(Room("dimond", "small room", "Magic"))
