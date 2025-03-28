class Select_Room_Extend:
    @staticmethod
    def add_selected_rooms(select_room_view_instance):
        selected = select_room_view_instance.tree.selection()
        if not selected:
            return []
        cart_items = []
        for item in selected:
            values = select_room_view_instance.tree.item(item, "values")
            item_dict = {
                "RoomID": values[0],
                "RoomType": values[1],
                "Price": values[2],
                "Day in": "",
                "Day out": ""
            }
            cart_items.append(item_dict)

        for item in selected:
            select_room_view_instance.tree.delete(item)
        return cart_items
