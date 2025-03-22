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

        # Entries
        self.entry_images = {
            "entry_1": PhotoImage(file=self.relative_to_assets("entry_1.png")),
            "entry_4": PhotoImage(file=self.relative_to_assets("entry_4.png"))
        }

        entry_data = [
            (428.1064, 161.4692, 164.9817, 34.5297, "entry_1"),
            (637.9863, 130.2529, 314.251, 39.0992, "entry_4"),
            (428.1064, 227.8868, 164.9817, 34.5297,"entry_1"),
            (428.1064, 294.3044, 164.9817, 34.5297,"entry_1")]
        self.entries = []
        for x, y, width, height, img_key in entry_data:
            self.canvas.create_image(x + width / 2, y + height / 2, image=self.entry_images[img_key])
            entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
            entry.place(x=x, y=y, width=width, height=height)
            self.entries.append(entry)

        # Tạo buttons
        self.btn_img_1 = PhotoImage(file=self.relative_to_assets("button_logout.png"))
        self.button_1 = Button(
            image=self.btn_img_1,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("logout button clicked"),
            relief="flat"
        )
        self.button_1.place(x=6.0, y=584.0, width=119.5039, height=55.0097)

        self.btn_img_2 = PhotoImage(file=self.relative_to_assets("button_quit.png"))
        self.button_2 = Button(
            image=self.btn_img_2,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("quit button clicked"),
            relief="flat"
        )
        self.button_2.place(x=138.0, y=585.0, width=118.8716, height=53.1128)

        self.btn_img_3 = PhotoImage(file=self.relative_to_assets("button_delete.png"))
        self.button_3 = Button(
            image=self.btn_img_3,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("delete button clicked"),
            relief="flat"
        )
        self.button_3.place(x=514.0566, y=359.7763, width=88.5214, height=47.4222)

        self.btn_img_4 = PhotoImage(file=self.relative_to_assets("button_update.png"))
        self.button_4 = Button(
            image=self.btn_img_4,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("update button clicked"),
            relief="flat"
        )
        self.button_4.place(x=302.9893, y=361.3862, width=85.8724, height=46.4923)

        self.btn_img_5 = PhotoImage(file=self.relative_to_assets("button_create.png"))
        self.button_5 = Button(
            image=self.btn_img_5,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("create button clicked"),
            relief="flat"
        )
        self.button_5.place(x=408.4795, y=360.7221, width=85.8641, height=46.4923)

        self.btn_img_6 = PhotoImage(file=self.relative_to_assets("button_find.png"))
        self.button_6 = Button(
            image=self.btn_img_6,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("find button clicked"),
            relief="flat"
        )
        self.button_6.place(x=958.5605, y=130.2529, width=56.9066, height=41.0992)

        self.btn_img_7 = PhotoImage(file=self.relative_to_assets("button_reload.png"))
        self.button_7 = Button(
            image=self.btn_img_7,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("reload button clicked"),
            relief="flat"
        )
        self.button_7.place(x=1021.1572, y=130.2529, width=56.9066, height=41.0992)

        self.btn_img_8 = PhotoImage(file=self.relative_to_assets("button_sales.png"))
        self.button_8 = Button(
            image=self.btn_img_8,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("sales button clicked"),
            relief="flat"
        )
        self.button_8.place(x=25.292, y=345.2335, width=213.716, height=59.4358)

        self.btn_img_9 = PhotoImage(file=self.relative_to_assets("button_users.png"))
        self.button_9 = Button(
            image=self.btn_img_9,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("users button clicked"),
            relief="flat"
        )
        self.button_9.place(x=25.292, y=421.109, width=209.9222, height=58.8035)

        self.btn_img_10 = PhotoImage(file=self.relative_to_assets("button_price.png"))
        self.button_10 = Button(
            image=self.btn_img_10,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("price button clicked"),
            relief="flat"
        )
        self.button_10.place(x=25.292, y=268.7257, width=213.716, height=60.7004)

        self.btn_img_11 = PhotoImage(file=self.relative_to_assets("button_edit.png"))
        self.button_11 = Button(
            image=self.btn_img_11,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("edit button clicked"),
            relief="flat"
        )
        self.button_11.place(x=25.292, y=188.4241, width=213.716, height=64.4942)

        self.btn_img_12 = PhotoImage(file=self.relative_to_assets("button_overview.png"))
        self.button_12 = Button(
            image=self.btn_img_12,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#51908D",
            command=lambda: print("overview button clicked"),
            relief="flat"
        )
        self.button_12.place(x=25.292, y=116.9747, width=230.1556, height=60.0681)

        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)


if __name__ == "__main__":
    Change_login_info()