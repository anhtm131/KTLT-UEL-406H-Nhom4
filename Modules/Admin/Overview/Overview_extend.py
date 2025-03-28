

from Api.Main_Api import Main_Api

class Overview_extend:
    def __init__(self):
        super().__init__()

    def search_room(self):
        query = self.entry_find.get().strip().lower()
        self.filtered_rooms = [
            room for room in self.rooms
            if query in str(room['RoomID']).lower()
        ]
        self.create_room_frames()


if __name__ == "__main__":
    app = Overview_extend()
    app.run()

