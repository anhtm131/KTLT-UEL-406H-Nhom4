from tkinter import messagebox
from Modules.Users.Overview.Overview_view import Overview_view
from Modules.Users.Cart_and_Customer.Cart_and_Customer_view import Cart_and_Customer_view
from Modules.Users.Invoice.Invoice_view import Invoice_view
from Modules.Users.Rooms_Details.Room_details_view import Room_detail_view
from Modules.Users.Select_Room.Select_Room_view import Select_Room_view


class Main_process:
    @staticmethod
    def booking_button(obj):
        obj.window.destroy()
        Select_Room_view()

    @staticmethod
    def roomdetail_button(obj):
        obj.window.destroy()
        Room_detail_view()

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
        Overview_view()

    @staticmethod
    def invoices_button(obj):
        obj.window.destroy()
        Invoice_view()

    @staticmethod
    def log_out_button(obj):
        if messagebox.askyesno("Confirm", "Are you sure?"):
            obj.window.destroy()
            Login_view()
        else:
            pass

    @staticmethod
    def quit_button(obj):
        if messagebox.askyesno("Confirm", "Are you sure?"):
            obj.window.destroy()

