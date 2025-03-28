from tkinter import *
from pathlib import Path
import tkinter as tk
import Modules.Main_process as Main_process
import tkinter.ttk as ttk
from Api.User_Api import User_Api
#from Modules.Users.Select_Room.Selected_Room_extend import Selected_Room_extend
from Modules.Users.Select_Room.Select_Room_view import Select_Room_view
from Modules.Users.Select_Room.Selected_Room_extend import Selected_Room_extend

class Cart_and_Customer_view:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("966x600")
        self.window.title("Cart and Customer Details")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=600, width=966, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Users" / "Cart_and_Customer"
        self.window.iconphoto(False, PhotoImage(file=self.relative_to_assets("icon_cart.png")))

        self.background_img = PhotoImage(file=self.relative_to_assets("background_cart_and_customer.png"))
        self.canvas.create_image(484.0, 300.0, image=self.background_img)

        self.entry_dayin = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_dayin.place(x=224.08, y=392, width=151.39, height=23.33)

        self.entry_dayout = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_dayout.place(x=224.08, y=428.67, width=151.39, height=23.33)

        self.btn_img_invoice = PhotoImage(file=self.relative_to_assets("button_invoice.png"))
        self.button_invoice = Button(image=self.btn_img_invoice, borderwidth=0, highlightthickness=0,activebackground="#6C9587", command=lambda: Main_process.Main_process.invoices_button(self))
        self.button_invoice.place(x=791.0, y=524.0, width=124.0, height=48.0)

        self.btn_img_back = PhotoImage(file=self.relative_to_assets("button_back.png"))
        self.button_back = Button(image=self.btn_img_back, borderwidth=0, highlightthickness=0, activebackground="#6C9587", command=lambda:Main_process.Main_process.back_button(self),relief="flat")
        self.button_back.place(x=668.0, y=523.0, width=110.0, height=49.0)

        self.btn_img_add = PhotoImage(file=self.relative_to_assets("button_add.png"))
        self.button_add = Button(image=self.btn_img_add, borderwidth=0, highlightthickness=0,activebackground="#6C9587", command=lambda: self.update_selected_room_dates(),relief="flat")
        self.button_add.place(x=234.75, y=470.67, width=52.68, height=23.67)

        self.btn_img_remove = PhotoImage(file=self.relative_to_assets("button_remove.png"))
        self.button_remove = Button(image=self.btn_img_remove, borderwidth=0, highlightthickness=0,activebackground="#6C9587", command=lambda: self.remove_selected_room(),relief="flat")
        self.button_remove.place(x=299.44, y=470.67, width=76.03, height=23.33)

        self.selected_rooms = []
        self.api = User_Api()
        self.create_selected_rooms_table()
        self.update_selected_rooms_table()

        self.window.mainloop()

    def create_selected_rooms_table(self):
        columns = ("RoomID", "RoomType", "Price", "Day in", "Day out")

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
        self.tree.bind("<ButtonRelease-1>", self.on_treeview_click)
        self.rooms = self.load_room_data()
    def on_treeview_click(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            values = self.tree.item(selected_item[0], "values")
            self.selected_room_id = values[0]

    def get_entry_data(self):
        day_in = self.entry_dayin.get().strip()
        day_out = self.entry_dayout.get().strip()
        return day_in, day_out

    def update_selected_room_dates(self):
        day_in, day_out = self.get_entry_data()
        if day_in is None or day_out is None:
            return

        for item in self.tree.get_children():
            values = self.tree.item(item, "values")
            if values[0] == self.selected_room_id:
                self.tree.item(item, values=(values[0], values[1], values[2], day_in, day_out))
                break
    def update_selected_rooms_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for room in self.rooms:
            self.tree.insert("", tk.END, values=(
                room["RoomID"],
                room["RoomType"],
                room["Price"],
                "",
                ""
            ))

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

    def load_room_data(self):
        selected_manager = Selected_Room_extend()
        room_info = selected_manager.get_selected_rooms()
        if not room_info:
            return []

        return [{
            "RoomID": room["RoomID"],
            "RoomType": room["RoomType"],
            "Price": room["Price"],
            "Status": room["Status"]
        } for room in room_info]

    def load_cart_data(self, day_in=None, day_out=None):
            api = Api.User_Api()
            rooms = Selected_Room_extend().get_selected_rooms()
            days = (day_out_date - day_in_date).days
            cart = [{
                "RoomID": room["RoomID"],
                "RoomType": room["RoomType"],
                "Days": days,
                "Price": float(room["Price"]) if room["Price"] else 0.0,
                "DayIn": day_in,
                "DayOut": day_out
            } for room in rooms]
            return cart
    def update_cart_data(self):
        day_in = self.entry_dayin.get().strip()
        day_out = self.entry_dayout.get().strip()
        self.cart_data = self.load_cart_data(day_in, day_out)
        self.refresh_treeview()
        return self.cart_data
    def remove_selected_room(self):
        selected_item = self.tree.selection()
        for item in selected_item:
            self.tree.delete(item)
if __name__ == "__main__":
    app = Cart_and_Customer_view()
    app.window.mainloop()