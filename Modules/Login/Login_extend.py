from Modules.Login.Login_view import Login_view
from tkinter import messagebox
from Api import Login_Api
from Modules.Admin.Overview import Overview_view as Overview_admin
from Modules.Users.Overview import Overview_view as Overview_user
from tkinter import *
class Login_extend(Login_view):
    def __init__(self):
        super().__init__()
        self.login_button.config(command=lambda: self.login_button_handle())

    def login_button_handle(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        login_api = Login_Api.Login_Api()
        a = login_api.check_login(username, password)
        if a == -1:
            messagebox.showerror("Warning", "Please enter your username or password")
        elif a == -2:
            messagebox.showerror("Warning", "User not found")
        elif a == -3:
            messagebox.showerror("Warning", "Wrong password")
        else:
            if a == "Admin":
                messagebox.showinfo("Welcome", "Welcome Admin")
                self.window.destroy()
                Main_Admin_view = Overview_admin.Overview_view()
                Main_Admin_view.window.mainloop()
            if a == "User":
                messagebox.showinfo("Welcome", "Welcome User")
                self.window.destroy()
                Main_User_view = Overview_user.MainView()
                Main_User_view.window.mainloop()
        
       
            



