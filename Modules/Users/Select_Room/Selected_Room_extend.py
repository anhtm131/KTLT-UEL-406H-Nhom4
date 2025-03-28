import json
import os
import tkinter as tk
import tkinter.ttk as ttk
from Api.Main_Api import Main_Api
from Modules.Users.Select_Room.Select_Room_view import SelectRoom
from Modules.Users.Cart_and_Customer.Cart_and_Customer_view import CartCustomerDetails


class Select_Room_Extend(SelectRoom):
    def __init__(self):
        super().__init__()

        self.rooms = self.load_rooms_data()
        self.selected_rooms = []
        self.cart_window = None
        self.create_treeview()
        self.button_add.config(command=lambda : self.add_selected_room())
        self.window.mainloop()

    def load_rooms_data(self):
            base_path = os.path.dirname(__file__)
            file_path = os.path.join(base_path, "..", "..", "..", "Data", "rooms.json")
            file_path = os.path.abspath(file_path)

            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)

    def create_treeview(self):
        columns = ("RoomID", "RoomType", "Price", "Status")

        self.rooms_rows = self.rooms
        tree_height = min(max(len(self.rooms_rows), 1), 10)
        frame_height = tree_height * 40 + 30

        frame = tk.Frame(self.window, width=1100, height=frame_height, bg="white", bd=2, relief="ridge")
        frame.place(x=50, y=90)

        style = ttk.Style()
        style.configure("Treeview", rowheight=40, font=("", 12))
        style.configure("Treeview.Heading", font=("Arial", 14, "bold"))

        self.tree = ttk.Treeview(
            master=frame,
            columns=columns,
            show="headings",
            height=tree_height
        )

        self.tree.heading("RoomID", text="Room ID")
        self.tree.heading("RoomType", text="Room Type")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Status", text="Status")

        self.tree.column("RoomID", width=200, anchor="center")
        self.tree.column("RoomType", width=200, anchor="center")
        self.tree.column("Price", width=200, anchor="center")
        self.tree.column("Status", width=200, anchor="center")

        self.tree.pack(padx=10, pady=10)

        for row in self.rooms_rows:
            self.tree.insert("", tk.END, values=(
                row.get("RoomID", ""),
                row.get("RoomType", ""),
                row.get("Price", ""),
                row.get("Status", ""),
            ))

    def add_selected_room(self):
        selected_item = self.tree.focus()

        values = self.tree.item(selected_item)["values"]

        room_data = {
            "RoomID": values[0],
            "RoomType": values[1],
            "Price": values[2]
        }

        if room_data not in self.selected_rooms:
            self.selected_rooms.append(room_data)
            print("Added Room:", room_data)

        print("Current selected rooms:", self.selected_rooms)
        if self.cart_window:
            self.cart_window.update_selected_rooms_table(self.selected_rooms)

    def open_cart_window(self):
        if self.cart_window is None or not tk.Toplevel.winfo_exists(self.cart_window.window):
            self.cart_window = CartCustomerDetails()

        self.cart_window.update_selected_rooms_table(self.selected_rooms)


if __name__ == "__main__":
    Select_Room_Extend()