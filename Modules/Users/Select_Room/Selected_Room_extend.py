class Select_Room_Extend:
    @staticmethod
    def add_selected_room(obj):
        selected = obj.tree.selection()
        if not selected:
            return None
        values = obj.tree.item(selected[0], "values")
        room_info = {
            "RoomID": values[0],
            "RoomType": values[1],
            "Price": values[2],
            "Status": values[3]
        }
        obj.tree.delete(selected[0])
        return room_info



