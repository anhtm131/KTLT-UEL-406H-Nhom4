from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

class GUI8:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1092x650")
        self.window.title("Room Type & Price")
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
        self.assets_path = output_path.parent / "assets" / "frame8"
        icon_path = self.relative_to_assets("room type.png")
        self.window.iconphoto(False, PhotoImage(file=icon_path))

        # Load background
        self.background_img = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(546.0, 325.0, image=self.background_img)

        # Entries
        entry_image = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.canvas.create_image(761.9164, 530.18, image=entry_image)
        entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        entry.place(x=490.0293, y=509.6303, width=543.7743, height=39.0992)

        # Buttons
        #Button Logout
        self.btn_img_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(image=self.btn_img_1,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground="#51908D",
                               command=lambda: print("button_logout clicked"), relief="flat")
        self.button_1.place(x=6.0, y=584.0, width=119.5039, height=55.0097)

        #Button quit
        self.btn_img_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(image=self.btn_img_2,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground="#51908D",
                               command=lambda: print("button_quit clicked"), relief="flat")
        self.button_2.place(x=137.208, y=584.8735, width=118.8716, height=53.1128)

        #Button sales
        self.btn_img_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(image=self.btn_img_3,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground="#51908D",
                               command=lambda: print("button_sales clicked"), relief="flat")
        self.button_3.place(x=25.292, y=345.2335, width=213.716, height=59.4358)

        #Button users
        self.btn_img_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = Button(image=self.btn_img_4,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground="#51908D",
                               command=lambda: print("button_users clicked"), relief="flat")
        self.button_4.place(x=25.292, y=421.109, width=209.9222, height=58.8035)

        #Button price
        self.btn_img_5 = PhotoImage(file=self.relative_to_assets("button_5.png"))
        self.button_5 = Button(image=self.btn_img_5,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground="#51908D",
                               command=lambda: print("button_price clicked"), relief="flat")
        self.button_5.place(x=25.292, y=268.7258, width=213.716, height=60.7004)

        #Button edit
        self.btn_img_6 = PhotoImage(file=self.relative_to_assets("button_6.png"))
        self.button_6 = Button(image=self.btn_img_6,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground="#51908D",
                               command=lambda: print("button_edit clicked"), relief="flat")
        self.button_6.place(x=25.292, y=188.4242, width=213.716, height=64.4942)

        #Button overview
        self.btn_img_7 = PhotoImage(file=self.relative_to_assets("button_7.png"))
        self.button_7 = Button(image=self.btn_img_7,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground="#51908D",
                               command=lambda: print("button_overview clicked"), relief="flat")
        self.button_7.place(x=25.292, y=116.9747, width=230.1556, height=60.0681)

        #Button update
        self.btn_img_8 = PhotoImage(file=self.relative_to_assets("button_8.png"))
        self.button_8 = Button(image=self.btn_img_8,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground="#51908D",
                               command=lambda: print("button_update clicked"), relief="flat")
        self.button_8.place(x=622.1787, y=563.3755, width=92.1864, height=46.4923)

        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

if __name__ == "__main__":
    GUI8()