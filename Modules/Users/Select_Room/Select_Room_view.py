from tkinter import *
from pathlib import Path
import Modules.Main_process as Main_process
from Modules.Users.Select_Room.Selected_Room_extend import Select_Room_Extend
import json
import os
import tkinter as tk
import tkinter.ttk as ttk
from Api.Main_Api import Main_Api
#from Modules.Users.Cart_and_Customer.Cart_and_Customer_view import CartCustomerDetails

class Select_Room_view:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("966x600")
        self.window.title("Select Room")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=600, width=966, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Users" / "Select_Room"

        self.window.iconphoto(False, PhotoImage(file=self.relative_to_assets("icon_select.png")))

        self.background_img = PhotoImage(file=self.relative_to_assets("background_select_room.png"))
        self.canvas.create_image(483.0, 300.0, image=self.background_img)


        self.button_cart_img = PhotoImage(file=self.relative_to_assets("button_cart.png"))
        self.button_cart = Button(image=self.button_cart_img, borderwidth=0, highlightthickness=0, activebackground="#6C947F",
                                   command=lambda: Main_process.Main_process.cart_and_customer_button(self), relief="flat")
        self.button_cart.place(x=183.0, y=524.0, width=98.0, height=47.0)



        self.button_back_img = PhotoImage(file=self.relative_to_assets("button_back.png"))
        self.button_back = Button(image=self.button_back_img, borderwidth=0, highlightthickness=0, activebackground="#6C947F",
                                   command=lambda: Main_process.Main_process.back_button(self), relief="flat")
        self.button_back.place(x=668.0, y=524.0, width=109.0, height=47.0)

        self.button_add_img = PhotoImage(file=self.relative_to_assets("button_add.png"))
        self.button_add = Button(image=self.button_add_img, borderwidth=0, highlightthickness=0, activebackground="#6C947F",command=lambda: print("Add button clicked"), relief="flat")
        self.button_add.place(x=683, y=455, width=80.9, height=36.35)

        self.rooms = self.load_room_data()
        self.create_treeview()
        #self.window.mainloop()

    def load_room_data(self):
        return [
            {
                "RoomID": room.get("RoomID"),
                "RoomType": room.get("RoomType"),
                "Price": room.get("Price"),
                "Status": room.get("Status")
            }
            for room in Main_Api().get_all_rooms_data()
        ]

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
    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)


if __name__ == "__main__":
    app = Select_Room_view()
    app.window.mainloop()
