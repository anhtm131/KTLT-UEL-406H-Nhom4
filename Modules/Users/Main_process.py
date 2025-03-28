
from tkinter import messagebox

from Modules.Login.Login_view import Login_view


class Main_process:
    @staticmethod
    def booking_button(obj):
        obj.window.destroy()
        Overview_view()

    @staticmethod
    def roomdetail_button(obj):
        obj.window.destroy()
        Rooms_view()

    @staticmethod
    def cart_and_customer_button(obj):
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
    def log_out_button(obj):
        if messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn thoát không?"):
            obj.window.destroy()
            Login_view()
        else:
            pass

    @staticmethod
    def quit_button(obj):
        if messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn thoát không?"):
            obj.window.destroy()

