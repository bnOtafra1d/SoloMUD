# Define class for player entity.
class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.visited_rooms = set()
        # Santiy increases by one to every room visited by default.
        # 0 (zero) sanity implies a stable mental state.
        # The high this number go the less stable of a mental state the player has.
        self.sanity = 0
