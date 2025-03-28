from tkinter import *
from tkinter import messagebox
from Modules.Login.Login_extend import Login_extend
from Modules.Users.Select_Room import Select_Room_extend
class Overview_process:
    @staticmethod
    def booking_button(obj):
        obj.destroy()
        pass
    @staticmethod
    def log_out_button(obj):
        if messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn thoát không?"):
            obj.destroy()
            Login_extend()
        else:
            pass
    @staticmethod
    def quit_button(obj):
        if messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn thoát không?"):
            obj.quit()
