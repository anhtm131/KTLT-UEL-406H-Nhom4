import json
import os
import tkinter as tk
import tkinter.ttk as ttk
from Api.Main_Api import Main_Api
from Modules.Users.Cart_and_Customer.Cart_and_Customer_view import CartCustomerDetails as BaseCartCustomerDetails

class CartCustomerDetails(BaseCartCustomerDetails):
    def __init__(self):
        super().__init__()

        self.selected_rooms = []
        self.create_selected_rooms_table()
        self.button_confirm.config(command=lambda : self.create_invoice())
        self.window.mainloop()
    def create_selected_rooms_table(self):
        columns = ("RoomID", "RoomType", "Price","Day in","Day out")

        self.tree = ttk.Treeview(self.window, columns=columns, show="headings", height=5)
        self.tree.heading("RoomID", text="Room ID")
        self.tree.heading("RoomType", text="Room Type")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Day in", text="Day in")
        self.tree.heading("Day out", text="Day out")

        self.tree.column("RoomID", width=100, anchor="center")
        self.tree.column("RoomType", width=100, anchor="center")
        self.tree.column("Price", width=100, anchor="center")
        self.tree.column("Day in", width=100, anchor="center")
        self.tree.column("Day out", width=100, anchor="center")


        self.tree.place(x=18, y=128)

    def update_selected_rooms_table(self, rooms):
        print("Updating Cart with rooms:", rooms)
        for item in self.tree.get_children():
            self.tree.delete(item)

        for room in rooms:
            self.tree.insert("", tk.END, values=(
                room["RoomID"],
                room["RoomType"],
                room["Price"]
            ))

if __name__ == "__main__":
    CartCustomerDetails()