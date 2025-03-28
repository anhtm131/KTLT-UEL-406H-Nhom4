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
from Modules.Users.Cart_and_Customer.Cart_and_Customer_view import Cart_and_Customer_view

class Invoice_view:
    def __init__(self, day_in=None, day_out=None):
        self.window = Tk()
        self.window.geometry("966x600")
        self.window.title("Invoice")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)
        #cart_and_customer = Cart_and_Customer_view()
        #self.load_cart_data_invoice = cart_and_customer.update_cart_data()
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


        self.create_treeview()
        self.load_cart_data_invoice()
        self.refresh_treeview()
        self.window.mainloop()

    def relative_to_assets(self, path: str, assets_type: str = "Frame") -> Path:
        return self.assets_frame_path / Path(path) if assets_type == "Frame" else Path(path)

    def create_treeview(self):
        columns = ("RoomID", "RoomType", "Days", "Price", "DayIn", "DayOut")
        self.tree = ttk.Treeview(self.window, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")

        self.tree.place(x=170, y=120, width=630, height=300)

    def refresh_treeview(self):
        self.tree.delete(*self.tree.get_children())


    def load_cart_data_invoice(self):
        pass



if __name__ == "__main__":
    Invoice_view()