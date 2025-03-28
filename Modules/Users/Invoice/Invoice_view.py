from tkinter import *
from pathlib import Path
import Modules.Main_process as Main_process
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import Api.User_Api as Api
from Modules.Users.Select_Room.Selected_Room_extend import Selected_Room_extend
from datetime import datetime, timedelta
import Api.Main_Api as Main_Api


class Invoice_view:
    def __init__(self, day_in=None, day_out=None):
        self.window = Tk()
        self.window.geometry("966x600")
        self.window.title("Invoice")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=600, width=966, bd=0, highlightthickness=0,
                             relief="ridge")
        self.canvas.place(x=0, y=0)

        OUTPUT_PATH = Path(__file__).parent
        self.assets_frame_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Users" / "Invoice"

        self.window.iconphoto(False, PhotoImage(file=self.relative_to_assets("icon.png", "Frame")))
        self.background_img = PhotoImage(file=self.relative_to_assets("background_invoices.png", "Frame"))
        self.canvas.create_image(483.0, 300.0, image=self.background_img)

        self.entry_total = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_total.place(x=427.48, y=464.49, width=244.75, height=28.68)

        self.button_img_back = PhotoImage(file=self.relative_to_assets("button_back.png", "Frame"))
        self.button_back = Button(image=self.button_img_back, borderwidth=0, highlightthickness=0,
                                  activebackground="#6C9587",
                                  command=lambda: Main_process.Main_process.back_button(self), relief="flat")
        self.button_back.place(x=671.0, y=527.0, width=110.0, height=47.0)

        self.cart_data = []
        self.update_total()
        self.window.mainloop()

    def relative_to_assets(self, path: str, assets_type: str = "Frame") -> Path:
        return self.assets_frame_path / Path(path) if assets_type == "Frame" else Path(path)

    def update_total(self):
        self.entry_total.delete(0, END)
        self.entry_total.insert(0, "1000000")

    def update_cart_data(self):
        self.cart_data = self.load_cart_data(day_in, day_out)
        self.refresh_treeview()
        return self.cart_data

    def load_cart_data(self, day_in=None, day_out=None):
            day_in = day_in or datetime.now().strftime("%d/%m/%Y")
            day_out = day_out or (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")

            rooms = Selected_Room_extend().get_selected_rooms()
            days = (datetime.strptime(day_out, "%d/%m/%Y") - datetime.strptime(day_in, "%d/%m/%Y")).days
            return [{
                "RoomID": room["RoomID"],
                "RoomType": room["RoomType"],
                "Days": days,
                "Price": float(room["Price"] or 0.0),
            } for room in rooms]

if __name__ == "__main__":
    Invoice_view()
