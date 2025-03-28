from tkinter import messagebox
from Modules.Login.Login_view import Login_view


class main_process:

    @staticmethod
    def quit_application(obj):
        if messagebox.askokcancel("Thoát", "Bạn có chắc muốn thoát ứng dụng?"):
            obj.destroy()

    @staticmethod
    def log_out_button(obj):
        if messagebox.askyesno("Đăng xuất", "Bạn có chắc chắn muốn đăng xuất không?"):
            obj.destroy()
            Login_view()
