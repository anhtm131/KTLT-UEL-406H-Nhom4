class Overview_extend:
    @staticmethod
    def search_room(obj):
        query = obj.entry.get().strip().lower()
        obj.filtered_rooms = [
            room for room in obj.rooms
            if query in str(room['RoomID']).lower()
        ]
        obj.create_room_frames()

