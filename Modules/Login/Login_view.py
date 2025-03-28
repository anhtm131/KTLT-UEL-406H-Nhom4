from pathlib import Path
from tkinter import messagebox
from Api import Login_Api
from Modules.Admin.Overview import Overview_view as Overview_admin
from Modules.Users.Overview import Overview_view as Overview_user
from tkinter import *

class Login_view:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("840x600")
        self.window.title("Welcome to Majestic Pearl")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=600,
            width=840,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH.parent.parent / "Images" / "Login"

        self.window.iconphoto(False, PhotoImage(file=self.relative_to_assets("icon_pearl.png")))

        self.background_img = PhotoImage(file=self.relative_to_assets("background_login.png"))
        self.canvas.create_image(420.0, 300.0, image=self.background_img)

        self.entry_image = PhotoImage(file=self.relative_to_assets("entry.png"))


        self.canvas.create_image(558.7, 315.2, image=self.entry_image)
        self.entry_password = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_password.place(x=464.6, y=301.8, width=188.1, height=25.0)


        self.canvas.create_image(558.7, 263.7, image=self.entry_image)
        self.entry_username = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_username.place(x=464.6, y=250.2, width=188.1, height=25.0)

        self.button_login_img = PhotoImage(file=self.relative_to_assets("button_login.png"))
        self.login_button = Button(image=self.button_login_img,borderwidth=0,highlightthickness=0,activebackground="#3D6C49",command=lambda: self.login_button_handle(self) ,relief="flat"
        )
        self.login_button.place(x=518.0, y=348.0, width=81.0, height=41.0)

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)


    @staticmethod
    def login_button_handle(obj):
        username = obj.entry_username.get()
        password = obj.entry_password.get()
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
                obj.window.destroy()
                Main_Admin_view = Overview_admin.Overview_view()
                Main_Admin_view.window.mainloop()
            if a == "User":
                messagebox.showinfo("Welcome", "Welcome User")
                obj.window.destroy()
                Main_User_view = Overview_user.Overview_view()
                Main_User_view.window.mainloop()







