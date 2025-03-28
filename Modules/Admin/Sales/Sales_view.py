from pathlib import Path
from tkinter import *
import tkinter as tk
import os
from tkinter import ttk, messagebox
from matplotlib import pyplot as plt
from datetime import datetime


import Modules.Main_process as Main_process
from Api.Admin_Api import Admin_Api
class Sales_view:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1092x650")
        self.window.title("Report Information")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)
        self.admin_api = Admin_Api()
        self.canvas = Canvas(self.window, bg="#FFFFFF", height=650, width=1092, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Admin" / "Sales"
        self.assets_WE_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Admin" / "Window_elements"

        self.window.iconphoto(False, PhotoImage(file=self.relative_to_assets("icon_report.png", "Frame")))
        self.background_img = PhotoImage(file=self.relative_to_assets("background_sales.png", "Frame"))
        self.canvas.create_image(546.0, 325.0, image=self.background_img)

        self.entry_from = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_from.place(x=369.8926, y=568.9047, width=148.5895, height=30.2471)

        self.entry_to = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_to.place(x=574.125, y=568.9047, width=148.5895, height=30.2471)

        self.button_img_logout = PhotoImage(file=self.relative_to_assets("logout.png", "Window_element"))
        self.logout = Button(image=self.button_img_logout, borderwidth=0, highlightthickness=0, activebackground="#55908B",
                             command=lambda: Main_process.Main_process.log_out_button(self), relief="flat")
        self.logout.place(x=7.0, y=586.0, width=117.0, height=51.0)

        self.button_img_quit = PhotoImage(file=self.relative_to_assets("quit.png", "Window_element"))
        self.button_quit = Button(image=self.button_img_quit, borderwidth=0, highlightthickness=0, activebackground="#55908B",
                                  command=lambda: Main_process.Main_process.quit_button(self), relief="flat")
        self.button_quit.place(x=138.0, y=586.0, width=117.0, height=51.0)

        self.button_img_visualize = PhotoImage(file=self.relative_to_assets("button_visualize.png", "Frame"))
        self.visualize = Button(image=self.button_img_visualize, borderwidth=0, highlightthickness=0, activebackground="#51908D",
                                command=lambda: self.visualize_sales_data(), relief="flat")
        self.visualize.place(x=892.8018, y=563, width=160.6031, height=41.0992)

        self.button_img_search = PhotoImage(file=self.relative_to_assets("button_search.png", "Frame"))
        self.search = Button(image=self.button_img_search, borderwidth=0, highlightthickness=0, activebackground="#51908D",
                             command=lambda: self.filter_by_date_range(), relief="flat")
        self.search.place(x=741.6836, y=563, width=134.679, height=41.0992)

        self.button_img_sales = PhotoImage(file=self.relative_to_assets("sales.png", "Window_element"))
        self.sales = Button(image=self.button_img_sales, borderwidth=0, highlightthickness=0, activebackground="#51908D",
                            command=lambda: print("sales"), relief="flat")
        self.sales.place(x=25.292, y=345.2335, width=213.716, height=59.4358)

        self.button_img_users = PhotoImage(file=self.relative_to_assets("user.png", "Window_element"))
        self.users = Button(image=self.button_img_users, borderwidth=0, highlightthickness=0, activebackground="#51908D",
                            command=lambda: Main_process.Main_process.users_button(self), relief="flat")
        self.users.place(x=25.292, y=421.109, width=209.9222, height=58.8035)

        self.button_img_price = PhotoImage(file=self.relative_to_assets("price.png", "Window_element"))
        self.price = Button(image=self.button_img_price, borderwidth=0, highlightthickness=0, activebackground="#51908D",
                            command=lambda: Main_process.Main_process.price_button(self), relief="flat")
        self.price.place(x=25.292, y=268.7258, width=213.716, height=60.7004)

        self.button_img_edit = PhotoImage(file=self.relative_to_assets("edit.png", "Window_element"))
        self.edit = Button(image=self.button_img_edit, borderwidth=0, highlightthickness=0, activebackground="#51908D",
                           command=lambda: Main_process.Main_process.edit_button(self), relief="flat")
        self.edit.place(x=25.292, y=188.4242, width=213.716, height=64.4942)

        self.button_img_overview = PhotoImage(file=self.relative_to_assets("overview.png", "Window_element"))
        self.overview = Button(image=self.button_img_overview, borderwidth=0, highlightthickness=0, activebackground="#51908D",
                               command=lambda: Main_process.Main_process.overview_button(self), relief="flat")
        self.overview.place(x=25.292, y=112.5486, width=230.1556, height=60.0681)
        self.create_treeview()
    def create_treeview(self):
        columns = ("InvoiceID", "Invoice_Date", "Total")
        self.tree = ttk.Treeview(self.window, columns=columns, show="headings")

        self.tree.heading("InvoiceID", text="Invoice ID")
        self.tree.heading("Invoice_Date", text="Invoice Date")
        self.tree.heading("Total", text="Total")

        self.tree.column("InvoiceID", width=100, anchor="center")
        self.tree.column("Invoice_Date", width=120, anchor="center")
        self.tree.column("Total", width=100, anchor="center")

        self.tree.place(x=300, y=180, width=753, height=300)

        self.load_tree_data()
    def load_tree_data(self):
        self.tree.delete(*self.tree.get_children())
        self.invoices = self.admin_api.get_all_invoices_data()
        for invoice in self.invoices:
            self.tree.insert("", tk.END, values=(
                invoice["InvoiceID"],
                invoice["Invoice_Date"],
                invoice["Total"]
            ))
    def filter_by_date_range(self):
        from_date_str = self.entry_from.get()
        to_date_str = self.entry_to.get()

        try:
            from_date = datetime.strptime(from_date_str, "%d/%m/%Y")
            to_date = datetime.strptime(to_date_str, "%d/%m/%Y")

            self.tree.delete(*self.tree.get_children())

            for invoice in self.invoices:
                invoice_date = datetime.strptime(invoice["Invoice_Date"], "%d/%m/%Y")
                if from_date <= invoice_date <= to_date:
                    self.tree.insert("", tk.END, values=(
                        invoice["InvoiceID"],
                        invoice["Invoice_Date"],
                        invoice["Total"]
                    ))
        except ValueError:
            messagebox.showerror("Error", "Date format error dd/mm/yyyy")

    def visualize_sales_data(self):
        dates = []
        totals = []

        for item in self.tree.get_children():
            values = self.tree.item(item, "values")
            dates.append(values[1])  # Invoice_Date
            totals.append(int(values[2]))  # Total

        if not dates:
            messagebox.showinfo("Notification", "No data to visualize.")
            return

        plt.figure(figsize=(10, 5))
        plt.gcf().canvas.manager.set_window_title("Sales Report")

        plt.plot(dates, totals, marker='o', linestyle='-', color='green')
        plt.xticks(rotation=45)
        plt.xlabel("Invoice Date")
        plt.ylabel("Total (VND)")
        plt.title("Sales by Invoice Date")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def filter_by_date_range(self):
        from_date_str = self.entry_from.get()
        to_date_str = self.entry_to.get()

        try:
            from_date = datetime.strptime(from_date_str, "%d/%m/%Y")
            to_date = datetime.strptime(to_date_str, "%d/%m/%Y")

            self.tree.delete(*self.tree.get_children())

            for invoice in self.invoices:
                invoice_date = datetime.strptime(invoice["Invoice_Date"], "%d/%m/%Y")
                if from_date <= invoice_date <= to_date:
                    self.tree.insert("", tk.END, values=(
                        invoice["InvoiceID"],
                        invoice["Invoice_Date"],
                        invoice["Total"]
                    ))
        except ValueError:
            messagebox.showerror("Error", "Date format error dd/mm/yyyy")

    def relative_to_assets(self, path: str, assets_type: str = "Frame") -> Path:
        if assets_type == "Frame":
            return self.assets_path / Path(path)
        elif assets_type == "Window_element":
            return self.assets_WE_path / Path(path)
if __name__ == "__main__":
    app = Sales_view()
    app.window.mainloop()
