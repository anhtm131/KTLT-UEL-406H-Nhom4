import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from Rooms_view import Rooms_view
from Api import Main_Api
from Api.Main_Api import Api


class Edit_extend(Rooms_view):
    def __init__(self):
        super().__init__()
        self.api = Api()

        self.rooms = self.api.get_all_rooms_data()
        self.create_treeview()

        self.button_create.config(command=self.create_room)
        self.button_update.config(command=self.update_room)
        self.button_delete.config(command=self.delete_room)

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

    def update_room(self):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0], "values")
            room_id = values[0]

            updated_data = {
                "RoomType": self.entry_roomtype.get(),
                "Price": self.entry_price.get().replace(",", ""),
                "Status": self.entry_status.get()
            }

            self.api.rooms_collection.update_one(
                {"RoomID": room_id},
                {"$set": updated_data}
            )
            self.load_tree_data()

    def create_room(self):
        new_room = {
            "RoomID": self.entry_roomid.get(),
            "RoomType": self.entry_roomtype.get(),
            "Price": self.entry_price.get().replace(",", ""),
            "Status": self.entry_status.get()
        }
        self.api.rooms_collection.insert_one(new_room)
        self.load_tree_data()

    def delete_room(self):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0], "values")
            room_id = values[0]

            self.api.rooms_collection.delete_one({"RoomID": room_id})
            self.load_tree_data()


if __name__ == "__main__":
    Edit_extend()
