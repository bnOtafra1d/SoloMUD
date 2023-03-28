import random

class Room:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.exits = {}

    def describe(self):
        print(self.description)
        print("\nExits:", ", ".join(self.exits.keys()) or "None")

    @staticmethod
    def get_random_description():
        with open('room_descriptions.txt') as f:
            descriptions = f.readlines()
        return random.choice(descriptions).strip()
