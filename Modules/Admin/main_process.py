from tkinter import messagebox
class main_process:
    def quit_application(obj):
        from tkinter import messagebox
        if messagebox.askokcancel("Quit", "Bạn có chắc muốn thoát ứng dụng?"):
            obj.destroy()