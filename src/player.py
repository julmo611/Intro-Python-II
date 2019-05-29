# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room, item):
        self.name = name
        self.room = room
        self.item = item

    def __str__(self):
        return str(self.__dict__)

print(Player("julian", "someroom", "money"))

