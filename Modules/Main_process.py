from Modules.Admin.Price.Price_view import Price_view
from Modules.Admin.Rooms.Rooms_view import Rooms_view
from Modules.Admin.Sales.Sales_view import Sales_view
from Modules.Admin.Users.Users_view import Users_view
import Modules.Admin.Overview.Overview_view as mao
import Modules.Users.Overview.Overview_view as muo
from Modules.Users.Cart_and_Customer.Cart_and_Customer_view import Cart_and_Customer_view
from Modules.Users.Invoice.Invoice_view import Invoice_view

from Modules.Users.Select_Room.Select_Room_view import Select_Room_view
from tkinter import messagebox
import Modules.Login.Login_view as lgv


class Main_process:
    @staticmethod
    def overview_button(obj):
        obj.window.destroy()
        mao.Overview_view()

    @staticmethod
    def edit_button(obj):
        obj.window.destroy()
        Rooms_view()

    @staticmethod
    def price_button(obj):
        obj.window.destroy()
        Price_view()

    @staticmethod
    def sales_button(obj):
        obj.window.destroy()
        Sales_view()

    @staticmethod
    def users_button(obj):
        obj.window.destroy()
        Users_view()

    @staticmethod
    def booking_button(obj):
        obj.window.destroy()
        Select_Room_view()

    @staticmethod
    def cart_and_customer_button(obj):
        obj.window.destroy()
        Cart_and_Customer_view()

    @staticmethod
    def Select_Room_button(obj):
        obj.window.destroy()
        Select_Room_view()

    @staticmethod
    def back_button(obj):
        obj.window.destroy()
        muo.Overview_view()

    @staticmethod
    def invoices_button(obj):
        obj.window.destroy()
        Invoice_view()

    @staticmethod
    def log_out_button(obj):
        if messagebox.askyesno("Confirm", "Are you sure?"):
            obj.window.destroy()
            lgv.Login_view()
        else:
            pass

    @staticmethod
    def quit_button(obj):
        if messagebox.askyesno("Confirm", "Are you sure?"):
            obj.window.destroy()

