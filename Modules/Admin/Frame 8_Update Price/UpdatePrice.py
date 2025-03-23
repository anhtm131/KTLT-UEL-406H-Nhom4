from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

class Update_Price:
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
        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Admin" / "Frame 8_Update Price"
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
        self.btn_logout = PhotoImage(file=self.relative_to_assets("button_logout.png"))
        self.button_logout = Button(image=self.btn_logout,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground="#51908D",
                               command=lambda: print("button_logout clicked"), relief="flat")
        self.button_logout.place(x=6.0, y=584.0, width=119.5039, height=55.0097)

        #Button quit
        self.btn_quit = PhotoImage(file=self.relative_to_assets("button_quit.png"))
        self.button_quit = Button(image=self.btn_quit,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground="#51908D",
                               command=lambda: print("button_quit clicked"), relief="flat")
        self.button_quit.place(x=137.208, y=584.8735, width=118.8716, height=53.1128)

        #Button sales
        self.btn_sales = PhotoImage(file=self.relative_to_assets("button_sales.png"))
        self.button_sales = Button(image=self.btn_sales,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground="#51908D",
                               command=lambda: print("button_sales clicked"), relief="flat")
        self.button_sales.place(x=25.292, y=345.2335, width=213.716, height=59.4358)

        #Button users
        self.btn_users = PhotoImage(file=self.relative_to_assets("button_users.png"))
        self.button_users = Button(image=self.btn_users,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground="#51908D",
                               command=lambda: print("button_users clicked"), relief="flat")
        self.button_users.place(x=25.292, y=421.109, width=209.9222, height=58.8035)

        #Button price
        self.btn_price = PhotoImage(file=self.relative_to_assets("button_price.png"))
        self.button_price = Button(image=self.btn_price,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground="#51908D",
                               command=lambda: print("button_price clicked"), relief="flat")
        self.button_price.place(x=25.292, y=268.7258, width=213.716, height=60.7004)

        #Button edit
        self.btn_edit = PhotoImage(file=self.relative_to_assets("button_edit.png"))
        self.button_edit = Button(image=self.btn_edit,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground="#51908D",
                               command=lambda: print("button_edit clicked"), relief="flat")
        self.button_edit.place(x=25.292, y=188.4242, width=213.716, height=64.4942)

        #Button overview
        self.btn_overview = PhotoImage(file=self.relative_to_assets("button_overview.png"))
        self.button_overview = Button(image=self.btn_overview,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground="#51908D",
                               command=lambda: print("button_overview clicked"), relief="flat")
        self.button_overview.place(x=25.292, y=116.9747, width=230.1556, height=60.0681)

        #Button update
        self.btn_update = PhotoImage(file=self.relative_to_assets("button_update.png"))
        self.button_update = Button(image=self.btn_update,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground="#51908D",
                               command=lambda: print("button_update clicked"), relief="flat")
        self.button_update.place(x=622.1787, y=563.3755, width=92.1864, height=46.4923)

        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

if __name__ == "__main__":
    Update_Price()