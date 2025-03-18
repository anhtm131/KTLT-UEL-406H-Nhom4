from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage


class GUI10:
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
        output_path = Path(__file__).parent
        self.assets_path = output_path.parent / "assets" / "frame10"
        icon_path = self.relative_to_assets("login_update.png")
        self.window.iconphoto(False, PhotoImage(file=icon_path))

        # Load background
        self.background_img = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(546.0, 325.0, image=self.background_img)

        # Tạo entries bằng vòng lặp
        self.create_entries()

        # Tạo buttons bằng hàm riêng
        self.create_button_1()
        self.create_button_2()
        self.create_button_3()
        self.create_button_4()
        self.create_button_5()
        self.create_button_6()
        self.create_button_7()
        self.create_button_8()
        self.create_button_9()
        self.create_button_10()
        self.create_button_11()
        self.create_button_12()

        self.window.mainloop()

    # region [ENTRIES]
    def create_entries(self):
        entries_info = [
            ("entry_1.png", 428.1064, 161.4692, 164.9817, 34.5297, 510.5973, 179.7341),
            ("entry_2.png", 428.1064, 227.8868, 164.9817, 34.5297, 510.5973, 246.1517),
            ("entry_3.png", 428.1064, 294.3044, 164.9817, 34.5297, 510.5973, 312.5693),
            ("entry_4.png", 637.9863, 130.2529, 314.251, 39.0992, 795.1118, 150.8025)
        ]
        for info in entries_info:
            self.create_entry(*info)

    def create_entry(self, img_name, x, y, width, height, img_x, img_y):
        entry_image = PhotoImage(file=self.relative_to_assets(img_name))
        self.canvas.create_image(img_x, img_y, image=entry_image)
        entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        entry.place(x=x, y=y, width=width, height=height)
        entry.image = entry_image

    # endregion

    # region [BUTTONS]
    #Button Logout
    def create_button_1(self):
        self.btn_img_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.btn_img_1,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("logout button clicked"),
            relief="flat"
        )
        self.button_1.place(x=6.0, y=584.0, width=119.5039, height=55.0097)

    #Button Quit
    def create_button_2(self):
        self.btn_img_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.btn_img_2,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("quit button clicked"),
            relief="flat"
        )
        self.button_2.place(x=138.0, y=585.0, width=118.8716, height=53.1128)

    #Button Delete
    def create_button_3(self):
        self.btn_img_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.btn_img_3,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("delete button clicked"),
            relief="flat"
        )
        self.button_3.place(x=514.0566, y=359.7763, width=88.5214, height=47.4222)

    #Button Update
    def create_button_4(self):
        self.btn_img_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.btn_img_4,
            borderwidth=0,
            highlightthickness=0,
            activebackground = "#51908D",
            command = lambda: print("update button clicked"),
            relief = "flat"
        )

        self.button_4.place(x=302.9893, y=361.3862, width=85.8724, height=46.4923)

    #Button Create
    def create_button_5(self):
        self.btn_img_5 = PhotoImage(file=self.relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.btn_img_5,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("create button clicked"),
            relief="flat"
        )
        self.button_5.place(x=408.4795, y=360.7221, width=85.8641, height=46.4923)

    #Button Find
    def create_button_6(self):
        self.btn_img_6 = PhotoImage(file=self.relative_to_assets("button_6.png"))
        self.button_6 = Button(
            image=self.btn_img_6,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("find button clicked"),
            relief="flat"
        )
        self.button_6.place(x=958.5605, y=130.2529, width=56.9066, height=41.0992)

    #Button Reload (next to entry)
    def create_button_7(self):
        self.btn_img_7 = PhotoImage(file=self.relative_to_assets("button_7.png"))
        self.button_7 = Button(
            image=self.btn_img_7,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("reload button clicked"),
            relief="flat"
        )
        self.button_7.place(x=1021.1572, y=130.2529, width=56.9066, height=41.0992)

    #Button Sales
    def create_button_8(self):
        self.btn_img_8 = PhotoImage(file=self.relative_to_assets("button_8.png"))
        self.button_8 = Button(
            image=self.btn_img_8,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("sales button clicked"),
            relief="flat"
        )
        self.button_8.place(x=25.292, y=345.2335, width=213.716, height=59.4358)

    #Button Users
    def create_button_9(self):
        self.btn_img_9 = PhotoImage(file=self.relative_to_assets("button_9.png"))
        self.button_9 = Button(
            image=self.btn_img_9,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("users button clicked"),
            relief="flat"
        )
        self.button_9.place(x=25.292, y=421.109, width=209.9222, height=58.8035)

    #Button Price
    def create_button_10(self):
        self.btn_img_10 = PhotoImage(file=self.relative_to_assets("button_10.png"))
        self.button_10 = Button(
            image=self.btn_img_10,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("price button clicked"),
            relief="flat"
        )
        self.button_10.place(x=25.292, y=268.7257, width=213.716, height=60.7004)

    #Button Edit
    def create_button_11(self):
        self.btn_img_11 = PhotoImage(file=self.relative_to_assets("button_11.png"))
        self.button_11 = Button(
            image=self.btn_img_11,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("edit button clicked"),
            relief="flat"
        )
        self.button_11.place(x=25.292, y=188.4241, width=213.716, height=64.4942)

    #Button Overview
    def create_button_12(self):
        self.btn_img_12 = PhotoImage(file=self.relative_to_assets("button_12.png"))
        self.button_12 = Button(
            image=self.btn_img_12,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("overview button clicked"),
            relief="flat"
        )
        self.button_12.place(x=25.292, y=116.9747, width=230.1556, height=60.0681)
    # endregion

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

if __name__ == "__main__":
    GUI10()