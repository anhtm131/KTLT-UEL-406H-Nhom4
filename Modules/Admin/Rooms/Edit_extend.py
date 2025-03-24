import json
import tkinter as tk
from tkinter import ttk

from Rooms_view import Rooms_view


class Edit_extend(Rooms_view):
    def __init__(self):
        super().__init__()

        self.rooms = self.load_room_data()
        self.create_treeview()

        self.button_create.config(command=lambda: self.create_room())
        self.button_update.config(command=lambda: self.update_room())
        self.button_delete.config(command=lambda: self.delete_room())

        self.window.mainloop()

    def load_room_data(self):
        try:
            with open(r'D:\KTLT_Final/Data\rooms.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        except Exception as e:
            print("Lỗi load data:", e)
            return []

    def save_room_data(self):
        try:
            with open(r'D:\KTLT_DoAnCuoiKy_Final\Data\rooms.json', 'w', encoding='utf-8') as file:
                json.dump(self.rooms, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print("Lỗi lưu data:", e)

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

        for room in self.rooms:
            price = str(room["Price"]).replace(",", "")  # Loại bỏ dấu phẩy nếu có
            self.tree.insert("", tk.END, values=(
                room["RoomID"],
                room["RoomType"],
                price,
                room["Status"]
            ))

        self.tree.bind("<ButtonRelease-1>", self.display_room_info)

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

    def update_room(self):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0], "values")
            for room in self.rooms:
                if room["RoomID"] == values[0]:
                    room["RoomType"] = self.entry_roomtype.get()
                    room["Price"] = self.entry_price.get().replace(",", "")
                    room["Status"] = self.entry_status.get()
                    break
            self.save_room_data()
            self.refresh_treeview()

    def create_room(self):
        new_room = {
            "RoomID": self.entry_roomid.get(),
            "RoomType": self.entry_roomtype.get(),
            "Price": self.entry_price.get().replace(",", ""),
            "Status": self.entry_status.get()
        }
        self.rooms.append(new_room)
        self.save_room_data()
        self.refresh_treeview()

    def delete_room(self):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0], "values")
            self.rooms = [room for room in self.rooms if room["RoomID"] != values[0]]
            self.save_room_data()
            self.refresh_treeview()

    def refresh_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for room in self.rooms:
            price = str(room["Price"]).replace(",", "")
            self.tree.insert("", tk.END, values=(
                room["RoomID"],
                room["RoomType"],
                price,
                room["Status"]
            ))

if __name__ == "__main__":
    Edit_extend()
