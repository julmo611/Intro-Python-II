# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, player_name, room_description, player_weapon=[]):
        self.player_name = player_name
        self.room_description = room_description
        self.player_weapon = player_weapon
