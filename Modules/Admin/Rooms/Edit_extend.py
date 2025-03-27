import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from Rooms_view import Rooms_view
#from Api.Main_Api import Main_Api
from Api.Admin_Api import Admin_Api

class Edit_extend(Rooms_view):
    def __init__(self):
        super().__init__()
        self.api = Admin_Api()

        self.rooms = self.api.get_all_rooms_data()
        self.create_treeview()

        self.button_create.config(command=self.create_room_button_handle())
        self.button_update.config(command=self.update_room_button_handle())
        self.button_delete.config(command=self.delete_room_button_handle())

        self.window.mainloop()

    def create_treeview(self):
        columns = ("RoomID", "RoomType", "Price", "Status")
        self.tree = ttk.Treeview(self.window, columns=columns, show="headings")

        self.tree.heading("RoomID", text="Room ID")
        self.tree.heading("RoomType", text="Room Type")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Status", text="Status")

        self.tree.column("RoomID", width=5, anchor="center")
        self.tree.column("RoomType", width=40, anchor="center")
        self.tree.column("Price", width=40, anchor="center")
        self.tree.column("Status", width=50, anchor="center")

        self.tree.place(x=678, y=180, width=400, height=300)

        self.load_tree_data()
        self.tree.bind("<ButtonRelease-1>", self.display_room_info)

    def load_tree_data(self):
        self.tree.delete(*self.tree.get_children())
        self.rooms = self.api.get_all_rooms_data()
        for room in self.rooms:
            price = str(room["Price"]).replace(",", "")
            self.tree.insert("", tk.END, values=(
                room["RoomID"],
                room["RoomType"],
                price,
                room["Status"]
            ))

    def display_room_info(self, event):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0], "values")

            self.entry_roomid.delete(0, tk.END)
            self.entry_roomid.insert(0, values[0])

            self.entry_roomtype.delete(0, tk.END)
            self.entry_roomtype.insert(0, values[1])

            self.entry_price.delete(0, tk.END)
            self.entry_price.insert(0, values[2])

            self.entry_status.delete(0, tk.END)
            self.entry_status.insert(0, values[3])

    def update_room_button_handle(self):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0], "values")
            room_id = values[0]

            updated_data = {
                "RoomType": self.entry_roomtype.get(),
                "Price": self.entry_price.get().replace(",", ""),
                "Status": self.entry_status.get()
            }

            result = self.api.update_room(updated_data, room_id)
            if result == 0:
                print("Cập nhật thành công!")
            else:
                print("Không có thông tin mới hoặc lỗi!")
            self.load_tree_data()

    def create_room_button_handle(self):
        new_room = {
            "RoomID": self.entry_roomid.get(),
            "RoomType": self.entry_roomtype.get(),
            "Price": self.entry_price.get().replace(",", ""),
            "Status": self.entry_status.get()
        }

        result = self.api.add_new_room(new_room)
        if result == 0:
            print("Tạo phòng thành công!")
        elif result == -1:
            print("Phòng đã tồn tại!")
        elif result == -2:
            print("Thiếu thông tin phòng!")
        self.load_tree_data()

    def delete_room_button_handle(self):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0], "values")
            room_id = values[0]
            result = self.api.remove_room(room_id)
            if result == 0:
                print("Xoá thành công!")
            else:
                print("Không tìm thấy phòng để xoá!")
            self.load_tree_data()

if __name__ == "__main__":
    Edit_extend()
