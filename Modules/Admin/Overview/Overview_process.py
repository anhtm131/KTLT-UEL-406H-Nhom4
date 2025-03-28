from tkinter import *
from tkinter import messagebox
from Modules.Admin.Price.Price_extend import Price_extend
from Modules.Admin.Rooms.Rooms_extend import Rooms_extend
from Modules.Admin.Sales.Sales_extend import Sales_extend
from Modules.Admin.Users.Users_extend import Users_extend
from Modules.Login import Login_view

class Overview_process:
    '''@staticmethod
    def overview_button(obj):
        obj.destroy()
        Overview_extend()'''

    @staticmethod
    def edit_button(obj):
        obj.window.destroy()
        Rooms_extend()

    @staticmethod
    def price_button(obj):
        obj.destroy()
        Price_extend()

    @staticmethod
    def sales_button(obj):
        obj.destroy()
        Sales_extend()

    @staticmethod
    def users_button(obj):
        obj.destroy()
        Users_extend()

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
