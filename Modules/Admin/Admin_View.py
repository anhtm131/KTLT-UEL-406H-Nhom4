from tkinter import *
from pathlib import Path

class Admin_View:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1092x650")
        self.window.title("Details")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)

        # Canvas setup
        self.canvas = Canvas(
            self.window, bg="#FFFFFF", height=650, width=1092,
            bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        # Asset path
        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH.parent.parent /"Images"/ "Admin" / "Frame 6_Overview"


        icon_path = self.assets_path/("icon_banhrang.png")
        self.window.iconphoto(False, PhotoImage(file=icon_path))

        # Load background
        self.background_img = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(546.0, 325.0, image=self.background_img)

        # Entry
        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.canvas.create_image(606.68, 43.62, image=self.entry_image_1)
        self.entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=410.99, y=21.49, width=391.39, height=42.26)

        # Buttons
        self.button_img_logout = PhotoImage(file=self.relative_to_assets("button_logout.png"))
        self.button_1 = Button(
            image=self.button_img_logout, borderwidth=0, highlightthickness=0,
            activebackground="#55908B",
            command=lambda: print("button_logout clicked"), relief="flat"
        )
        self.button_1.place(x=7.0, y=586.0, width=117.0, height=51.0)

        self.button_img_quit = PhotoImage(file=self.relative_to_assets("button_quit.png"))
        self.button_2 = Button(
            image=self.button_img_quit, borderwidth=0, highlightthickness=0,
            activebackground="#55908B",
            command=lambda: print("button_quit clicked"), relief="flat"
        )
        self.button_2.place(x=138.0, y=586.0, width=117.0, height=51.0)

        self.button_img_sales = PhotoImage(file=self.relative_to_assets("button_sales.png"))
        self.button_sales = Button(
            image=self.button_img_sales, borderwidth=0, highlightthickness=0,
            activebackground="#55908B",
            command=lambda: print("button_sales clicked"), relief="flat"
        )
        self.button_sales.place(x=25.29, y=345.23, width=213.71, height=59.43)

        self.button_img_users = PhotoImage(file=self.relative_to_assets("button_users.png"))
        self.button_users = Button(
            image=self.button_img_users, borderwidth=0, highlightthickness=0,
            activebackground="#55908B",
            command=lambda: print("button_users clicked"), relief="flat"
        )
        self.button_users.place(x=25.29, y=421.10, width=209.92, height=58.80)

        self.button_img_price = PhotoImage(file=self.relative_to_assets("button_price.png"))
        self.button_price = Button(
            image=self.button_img_price, borderwidth=0, highlightthickness=0,
            activebackground="#55908B",
            command=lambda: print("button_price clicked"), relief="flat"
        )
        self.button_price.place(x=25.29, y=268.72, width=213.71, height=60.70)

        self.button_img_edit = PhotoImage(file=self.relative_to_assets("button_edit.png"))
        self.button_edit = Button(
            image=self.button_img_edit, borderwidth=0, highlightthickness=0,
            activebackground="#55908B",
            command=lambda: print("button_edit clicked"), relief="flat"
        )
        self.button_edit.place(x=25.29, y=188.42, width=213.71, height=64.49)

        self.button_img_overview = PhotoImage(file=self.relative_to_assets("button_overview.png"))
        self.button_overview = Button(
            image=self.button_img_overview, borderwidth=0, highlightthickness=0,
            activebackground="#55908B",
            command=lambda: print("button_overview clicked"), relief="flat"
        )
        self.button_overview.place(x=25.29, y=116.97, width=230.15, height=60.06)

        self.button_img_find = PhotoImage(file=self.relative_to_assets("button_find.png"))
        self.button_find = Button(
            image=self.button_img_find, borderwidth=0, highlightthickness=0,
            activebackground="#55908B",
            command=lambda: print("button_find clicked"), relief="flat"
        )
        self.button_find.place(x=780.88, y=31.08, width=24.97, height=25.29)

        self.window.mainloop()
    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

if __name__ == "__main__":
    Admin_View()
