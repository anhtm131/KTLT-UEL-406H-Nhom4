from tkinter import *
from tkinter import messagebox
from Modules.Admin.Overview import Overview_view
#from Modules.Admin.Price import Price_view
from Modules.Admin.Rooms import Rooms_view
from Modules.Admin.Sales import Sales_view
from Modules.Admin.Users import Users_view
from Modules.Login import Login_view

class Overview_process:
    @staticmethod
    def overview_button(obj):
        obj.destroy()
        Overview_view.Overview_view()

    @staticmethod
    def edit_button(obj):
        obj.destroy()
        Rooms_view.Rooms_view()

    @staticmethod
    def price_button(obj):
        obj.destroy()
        Price_view.Price_view()

    @staticmethod
    def sales_button(obj):
        obj.destroy()
        Sales_view.Sales_view()

    @staticmethod
    def users_button(obj):
        obj.destroy()
        Users_view.Users_view()

    @staticmethod
    def log_out_button(obj):
        if messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn thoát không?"):
            obj.destroy()
            Login_view.Login_view()
        else:
            pass
    @staticmethod
    def quit_button(obj):
        if messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn thoát không?"):
            obj.quit()

