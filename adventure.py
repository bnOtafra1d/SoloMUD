import random
from room import Room
from player import Player

class Adventure:
    def __init__(self):
        self.rooms = []
        self.create_rooms()
        self.player = Player(self.rooms[0])

    def create_rooms(self):
    # Create a list of x rooms with random descriptions and exits
        for i in range(64):
            description = Room.get_random_description()
            room = Room(i, description)
            self.rooms.append(room)

    # Create exits between the rooms
    # This line starts a nested loop that will execute 8 times for each of the 8 rows in the grid.
        for i in range(8):
            # This line starts a nested loop that will execute 8 times for each of the 8 rows in the grid.
            for j in range(8):
                # This line gets the current Room object in the grid based on the current row and column (i and j) and adds it to the room variable.
                room = self.rooms[i * 8 + j]
                # This line checks if the current room is not in the first row of the grid.
                if i > 0:
                    # If the current room is not in the first row, this line sets the north exit of the current room to be the room above it in the grid.
                    room.exits["north"] = self.rooms[(i - 1) * 8 + j]
                    # This line checks if the current room is not in the last row of the grid.
                if i < 7:
                    # If the current room is not in the last row, this line sets the south exit of the current room to be the room below it in the grid.
                    room.exits["south"] = self.rooms[(i + 1) * 8 + j]
                    #  This line checks if the current room is not in the first column of the grid.
                if j > 0:
                    #  If the current room is not in the first column, this line sets the west exit of the current room to be the room to its left in the grid.
                    room.exits["west"] = self.rooms[i * 8 + j - 1]
                    # This line checks if the current room is not in the last column of the grid.
                if j < 7:
                    # If the current room is not in the last column, this line sets the east exit of the current room to be the room to its right in the grid.
                    room.exits["east"] = self.rooms[i * 8 + j + 1]

    def run(self):
        print("Welcome to the adventure!")
        sanity = 0
        while True:
            self.player.current_room.describe()
            sanity += 1
            print(f"Sanity: {'*' * sanity}{'-' * (3 - sanity)}\n")
            if sanity == 3:
                with open('madness_descriptions.txt') as f:
                    descriptions = f.readlines()
                print(random.choice(descriptions).strip())
                print(f"\nYou explored {len(self.player.visited_rooms)} rooms before going insane.")
                self.__init__()
                break
            command = input("\nWhat do you want to do? ")
            if command == "quit":
                print("Thanks for playing!")
                break
            elif command.startswith("go "):
                direction = command.split()[1]
                if direction in self.player.current_room.exits:
                    self.player.current_room = self.player.current_room.exits[direction]
                    self.player.visited_rooms.add(self.player.current_room.id)
                else:
                    print("You can't go that way.")
            else:
                print("I don't understand that command.")

if __name__ == "__main__":
    adventure = Adventure()
    adventure.run()
