import json
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

from Modules.Users.Invoice.Invoice_view import Invoice
import Api.User_Api as Api


class Invoice_extend(Invoice):
    def __init__(self):
        super().__init__()

        self.invoices = self.load_invoice_data()
        self.create_treeview()

        self.reload.config(command=lambda: self.refresh_treeview())
        self.window.mainloop()

    def load_invoice_data(self):
        try:
            api = Api.User_Api()
            return api.total_invoice
        except Exception as e:
            print("Lỗi load hóa đơn:", e)
            return []

    def create_treeview(self):
        columns = ("RoomID", "RoomType", "Days", "Price", "DayIn", "DayOut")
        self.tree = ttk.Treeview(self.window, columns=columns, show="headings")

        self.tree.heading("RoomID", text="Room ID")
        self.tree.heading("RoomType", text="Room Type")
        self.tree.heading("Days", text="Days")
        self.tree.heading("Price", text="Price")
        self.tree.heading("DayIn", text="Day In")
        self.tree.heading("DayOut", text="Day Out")

        self.tree.column("RoomID", width=100, anchor="center")
        self.tree.column("RoomType", width=120, anchor="center")
        self.tree.column("Days", width=60, anchor="center")
        self.tree.column("Price", width=100, anchor="center")
        self.tree.column("DayIn", width=100, anchor="center")
        self.tree.column("DayOut", width=100, anchor="center")

        self.tree.place(x=170, y=120, width=630, height=300)

        self.refresh_treeview()

    def refresh_treeview(self):
        self.tree.delete(*self.tree.get_children())
        for invoice in self.invoices:
            for item in invoice.get("Cart", []):
                self.tree.insert("", tk.END, values=(
                    item.get("RoomID", ""),
                    item.get("RoomType", ""),
                    item.get("Days", ""),
                    item.get("Price", ""),
                    item.get("DayIn", ""),
                    item.get("DayOut", "")
                ))


if __name__ == "__main__":
    Invoice_extend()
