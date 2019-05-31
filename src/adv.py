import sys
from room import Room
from player import Player
from item import Item

# print(sys.version)


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


item = {
    "Dragon Armour":   Item("Dragon Armour", "What did you have to go and do that for? Here, take this Dragon Potion and leave me alone!"),
    "Magic sword":    Item("Magic sword", "Take this, the Magic Sword. Twice the size and twice as powerful as all your other close range weapons."),
    "Chicken Drumstick":  Item("Chicken Drumstick", "Here you are Sir Knight, a wart covered and cabbage smelling old crone I may be but I always keep my promises: I grant you my reward!	"),
    "Hammer":   Item("Hammer", "It'll smash anything and it won't fall apart like a club"),
    "Flaming Longbow":  Item("Flaming Longbow", "more powerful than a crossbow, the option of flaming arrows, it is truly the weapon of noblemen."),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].n_to = room['overlook']
room['narrow'].n_to = room['treasure']
room['foyer'].s_to = room['outside']
room['overlook'].s_to = room['foyer']
room['foyer'].e_to = room['narrow']
room['treasure'].s_to = room['narrow']
room['narrow'].w_to = room['foyer']


# Link rooms with items

room['outside'].items = item["Dragon Armour"]
room['foyer'].items = item["Magic sword"]
room['overlook'].items = item["Chicken Drumstick"]
room['narrow'].items = item["Hammer"]
room['treasure'].items = item["Flaming Longbow"]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


player = Player(input("Enter your name: "), room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def walking_player(direction):
    error = "\n-----There is no room here, please try again------\n"
    tagain = "\n Can you read the description please? \n"
    if direction == 'n':
        if player.room_description.n_to is not None:
            player.room_description = player.room_description.n_to
        else:
            print(tagain)

    elif direction == 's':
        if player.room_description.s_to is not None:
            player.room_description = player.room_description.s_to
        else:
            print(tagain)

    elif direction == 'e':
        if player.room_description.e_to is not None:
            player.room_description = player.room_description.e_to
        else:
            print(tagain)

    elif direction == 'w':
        if player.room_description.w_to is not None:
            player.room_description = player.room_description.w_to
        else:
            print(tagain)
    elif direction == 'p':
        if Player.get_item:
            player.get_item(item)
            print(f"This is your new inventory: {player.item}")
    elif direction == 'd':
        if Player.drop_item:
            player.drop_item(item)
            print(player.item)
    elif direction == 'in':
        if Player.get_item:
            print(
                f"====================================\nYour inventory:\n{player.item}\n======================================")
        else:
            print("You don't have any item")
    else:
        print(error)


while True:
    print(f"My warrior's name: {player.player_name}")
    print(
        f"I'm here: {player.room_description.room_name}\nDescription: {player.room_description.description} \n")
    walk = input(
        "Walk to North(n), South(s), East(e), or West(w)\n Drop item(d), Pickup item(p), See inventory(in),\nQuit Game(q): \nNext move -> ")
    walking_player(walk)
    if walk == 'q':
        print("Game Over")
        break
