import tkinter as tk

class Rooms_extend():

    @staticmethod
    def update_room_button_handle(obj):
        selected = obj.tree.selection()
        if selected:
            values = obj.tree.item(selected[0], "values")
            room_id = values[0]

            updated_data = {
                "RoomType": obj.combo_roomtype.get(),
                "Price": obj.entry_price.get().replace(",", ""),
                "Status": obj.entry_status.get()
            }

            result = obj.admin_api.update_room(updated_data, room_id)
            if result == 0:
                print("Cập nhật thành công!")
            else:
                print("Không có thông tin mới hoặc lỗi!")
            obj.load_tree_data()
    @staticmethod
    def create_room_button_handle(obj):
        new_room = {
            "RoomID": obj.entry_roomid.get(),
            "RoomType": obj.combo_roomtype.get(),
            "Price": obj.entry_price.get().replace(",", ""),
            "Status": obj.entry_status.get()
        }

        result = obj.admin_api.add_new_room(new_room)
        if result == 0:
            print("Tạo phòng thành công!")
        elif result == -1:
            print("Phòng đã tồn tại!")
        elif result == -2:
            print("Thiếu thông tin phòng!")
        obj.load_tree_data()
    @staticmethod
    def delete_room_button_handle(obj):
        selected = obj.tree.selection()
        if selected:
            values = obj.tree.item(selected[0], "values")
            room_id = values[0]
            result = obj.admin_api.remove_room(room_id)
            if result == 0:
                print("Xoá thành công!")
            else:
                print("Không tìm thấy phòng để xoá!")
            obj.load_tree_data()
    @staticmethod
    def search_room(obj):
        keyword = obj.entry_find.get().strip()
        filtered_rooms = [room for room in obj.rooms if keyword.lower() in str(room["RoomID"]).lower()]
        obj.tree.delete(*obj.tree.get_children())
        for room in filtered_rooms:
            price = str(room["Price"]).replace(",", "")
            obj.tree.insert("", tk.END, values=(
                room["RoomID"],
                room["RoomType"],
                price,
                room["Status"]
            ))
    @staticmethod
    def reset_view(obj):
        obj.entry_find.delete(0, tk.END)
        obj.entry_roomid.delete(0, tk.END)
        obj.combo_roomtype.set('')
        obj.entry_price.delete(0, tk.END)
        obj.entry_status.delete(0, tk.END)
        obj.load_tree_data()


if __name__ == "__main__":
    Rooms_extend()
