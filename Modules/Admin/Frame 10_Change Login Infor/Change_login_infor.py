from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage


class Change_login_info:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1092x650")
        self.window.title("Update Login Information")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)

        # Canvas setup
        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=650,
            width=1092,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        # Asset path
        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Admin" / "Frame 10_Update login information"
        icon_path = self.relative_to_assets("login_update.png")
        self.window.iconphoto(False, PhotoImage(file=icon_path))

        # Load background
        self.background_img = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(546.0, 325.0, image=self.background_img)

        # Load entry images
        self.entry_img_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_img_4 = PhotoImage(file=self.relative_to_assets("entry_4.png"))

        self.entries = []

        # Entry 1
        self.canvas.create_image(428.1064 + 164.9817 / 2, 161.4692 + 34.5297 / 2, image=self.entry_img_1)
        self.entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=428.1064, y=161.4692, width=164.9817, height=34.5297)
        self.entries.append(self.entry_1)

        # Entry 2
        self.canvas.create_image(637.9863 + 314.251 / 2, 130.2529 + 39.0992 / 2, image=self.entry_img_4)
        self.entry_2 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=637.9863, y=130.2529, width=314.251, height=39.0992)
        self.entries.append(self.entry_2)

        # Entry 3
        self.canvas.create_image(428.1064 + 164.9817 / 2, 227.8868 + 34.5297 / 2, image=self.entry_img_1)
        self.entry_3 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_3.place(x=428.1064, y=227.8868, width=164.9817, height=34.5297)
        self.entries.append(self.entry_3)

        # Entry 4
        self.canvas.create_image(428.1064 + 164.9817 / 2, 294.3044 + 34.5297 / 2, image=self.entry_img_1)
        self.entry_4 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_4.place(x=428.1064, y=294.3044, width=164.9817, height=34.5297)
        self.entries.append(self.entry_4)

        # Tạo buttons
        self.btn_logout = PhotoImage(file=self.relative_to_assets("button_logout.png"))
        self.button_logout = Button(
            image=self.btn_logout,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("logout button clicked"),
            relief="flat"
        )
        self.button_logout.place(x=6.0, y=584.0, width=119.5039, height=55.0097)

        self.btn_quit = PhotoImage(file=self.relative_to_assets("button_quit.png"))
        self.button_quit = Button(
            image=self.btn_quit,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("quit button clicked"),
            relief="flat"
        )
        self.button_quit.place(x=138.0, y=585.0, width=118.8716, height=53.1128)

        self.btn_delete = PhotoImage(file=self.relative_to_assets("button_delete.png"))
        self.button_delete = Button(
            image=self.btn_delete,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("delete button clicked"),
            relief="flat"
        )
        self.button_delete.place(x=514.0566, y=359.7763, width=88.5214, height=47.4222)

        self.btn_update = PhotoImage(file=self.relative_to_assets("button_update.png"))
        self.button_update = Button(
            image=self.btn_update,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("update button clicked"),
            relief="flat"
        )
        self.button_update.place(x=302.9893, y=361.3862, width=85.8724, height=46.4923)

        self.btn_create = PhotoImage(file=self.relative_to_assets("button_create.png"))
        self.button_create = Button(
            image=self.btn_create,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("create button clicked"),
            relief="flat"
        )
        self.button_create.place(x=408.4795, y=360.7221, width=85.8641, height=46.4923)

        self.btn_find = PhotoImage(file=self.relative_to_assets("button_find.png"))
        self.button_find = Button(
            image=self.btn_find,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("find button clicked"),
            relief="flat"
        )
        self.button_find.place(x=958.5605, y=130.2529, width=56.9066, height=41.0992)

        self.btn_reload = PhotoImage(file=self.relative_to_assets("button_reload.png"))
        self.button_reload = Button(
            image=self.btn_reload,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("reload button clicked"),
            relief="flat"
        )
        self.button_reload.place(x=1021.1572, y=130.2529, width=56.9066, height=41.0992)

        self.btn_sales = PhotoImage(file=self.relative_to_assets("button_sales.png"))
        self.button_sales = Button(
            image=self.btn_sales,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("sales button clicked"),
            relief="flat"
        )
        self.button_sales.place(x=25.292, y=345.2335, width=213.716, height=59.4358)

        self.btn_users = PhotoImage(file=self.relative_to_assets("button_users.png"))
        self.button_users = Button(
            image=self.btn_users,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("users button clicked"),
            relief="flat"
        )
        self.button_users.place(x=25.292, y=421.109, width=209.9222, height=58.8035)

        self.btn_price = PhotoImage(file=self.relative_to_assets("button_price.png"))
        self.button_price = Button(
            image=self.btn_price,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("price button clicked"),
            relief="flat"
        )
        self.button_price.place(x=25.292, y=268.7257, width=213.716, height=60.7004)

        self.btn_edit = PhotoImage(file=self.relative_to_assets("button_edit.png"))
        self.button_edit = Button(
            image=self.btn_edit,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("edit button clicked"),
            relief="flat"
        )
        self.button_edit.place(x=25.292, y=188.4241, width=213.716, height=64.4942)

        self.btn_overview = PhotoImage(file=self.relative_to_assets("button_overview.png"))
        self.button_overview = Button(
            image=self.btn_overview,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("overview button clicked"),
            relief="flat"
        )
        self.button_overview.place(x=25.292, y=116.9747, width=230.1556, height=60.0681)

        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)


if __name__ == "__main__":
    Change_login_info()