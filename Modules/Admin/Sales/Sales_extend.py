import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from Modules.Admin.Sales.Sales_view import Sales_view


class Sales_extend(Sales_view):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    Sales_extend()
