class Selected_Room_extend:
    selected_rooms = []

    @classmethod
    def add_selected_room(cls, tree):
        selected_item = tree.selection()
        if not selected_item:
            return None

        room_data = tree.item(selected_item[0], "values")
        room_info = {
            "RoomID": room_data[0],
            "RoomType": room_data[1],
            "Price": room_data[2],
            "Status": room_data[3]
        }

        cls.selected_rooms.append(room_info)
        tree.delete(selected_item[0])
        return room_info

    @classmethod
    def get_selected_rooms(cls):
        return cls.selected_rooms
