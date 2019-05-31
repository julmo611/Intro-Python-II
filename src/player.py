# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, player_name, room_description, item=[]):
        self.player_name = player_name
        self.room_description = room_description
        self.item = item

    def __repr__(self):
        return str(f'{self.player_name} {self.room_description} {self.item}')

    def get_item(self, item):
        self.item.append(self.room_description.items)

    def drop_item(self, item):
        self.item.remove(self.room_description.items)
