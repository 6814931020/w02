class Room:
    def __init__(self, roomCode):
        self.roomCode = roomCode

    def __str__(self):
        return f"Room : {self.roomCode}"