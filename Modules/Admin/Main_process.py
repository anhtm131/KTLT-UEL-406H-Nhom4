from Modules.Admin.Price.Price_view import Price_view
from Modules.Admin.Rooms.Rooms_view import Rooms_view
from Modules.Admin.Sales.Sales_view import Sales_view
from Modules.Admin.Users.Users_view import Users_view
from Modules.Admin.Overview.Overview_view import Overview_view
from tkinter import messagebox

from Modules.Login.Login_view import Login_view


class Main_process:
    @staticmethod
    def overview_button(obj):
        obj.window.destroy()
        Overview_view()

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

