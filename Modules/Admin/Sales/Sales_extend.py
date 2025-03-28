import os
import tkinter as tk
import json
from tkinter import ttk, messagebox
from matplotlib import pyplot as plt
from datetime import datetime
from Modules.Admin.Sales.Sales_view import Sales_view
from Api.Main_Api import Main_Api

class Sales_extend():

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


if __name__ == "__main__":
    Sales_extend()