from tkinter import *
from tkinter import messagebox
from Modules.Login import Login_view

class Overview_process:
    @staticmethod
    def edit_button(obj):
        obj.destroy()
        Se

    @staticmethod
    def log_out_button(obj):
        if messagebox.askyesno("Confirm", "Are you sure?"):
            obj.destroy()
            Login_view.Login_view()
        else:
            pass
    @staticmethod
    def quit_button(obj):
        if messagebox.askyesno("Confirm", "Are you sure?"):
            obj.quit()
