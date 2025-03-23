from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage


class Display_room_info:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1092x650")
        self.window.configure(bg="#FFFFFF")
        self.window.title("Display Room Information")
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
        self.assets_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Admin" / "Frame 7_Update Room Information"
        icon_path = self.relative_to_assets("ic_infor.png")
        self.window.iconphoto(False, PhotoImage(file=icon_path))

        # Load background
        self.background_img = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(546.0, 325.0, image=self.background_img)

        # Entries
        # Entry 1
        self.entry_img_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.canvas.create_image(818.1904, 142.5826, image=self.entry_img_1)
        self.entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=677.1885, y=122.033, width=282.0039, height=39.0992)

        # Entry 2
        self.entry_img_2 = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        self.canvas.create_image(536.8189, 419.2121, image=self.entry_img_2)
        self.entry_2 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=451.459, y=400.2433, width=170.7198, height=35.9377)

        # Entry 3
        self.entry_img_3 = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        self.canvas.create_image(536.8189, 178.9397, image=self.entry_img_3)
        self.entry_3 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_3.place(x=451.459, y=159.9709, width=170.7198, height=35.9377)

        # Entry 4
        self.entry_img_4 = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        self.canvas.create_image(536.8189, 258.6089, image=self.entry_img_4)
        self.entry_4 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_4.place(x=451.459, y=239.64, width=170.7198, height=35.9377)

        # Entry 5
        self.entry_img_5 = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        self.canvas.create_image(536.8189, 338.9106, image=self.entry_img_5)
        self.entry_5 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_5.place(x=451.459, y=319.9417, width=170.7198, height=35.9377)

        # Buttons
        self.btn_logout = PhotoImage(file=self.relative_to_assets("button_logout.png"))
        self.button_logout = Button(image=self.btn_logout, borderwidth=0, highlightthickness=0,
                                    activebackground="#6C9587",
                                    command=lambda: print("Logout clicked"), relief="flat")
        self.button_logout.place(x=6.0, y=583.6089, width=119.5039, height=55.0097)

        self.btn_quit = PhotoImage(file=self.relative_to_assets("button_quit.png"))
        self.button_quit = Button(image=self.btn_quit, borderwidth=0, highlightthickness=0,
                                  activebackground="#6C9587",
                                  command=lambda: print("Quit clicked"), relief="flat")
        self.button_quit.place(x=137.0, y=584.0, width=119.0, height=55.0)

        self.btn_find = PhotoImage(file=self.relative_to_assets("button_find.png"))
        self.button_find = Button(image=self.btn_find, borderwidth=0, highlightthickness=0,
                                  activebackground="#6C9587",
                                  command=lambda: print("Find clicked"), relief="flat")
        self.button_find.place(x=966.1484, y=122.033, width=56.9066, height=41.0992)

        self.btn_reset = PhotoImage(file=self.relative_to_assets("button_reset.png"))
        self.button_reset = Button(image=self.btn_reset, borderwidth=0, highlightthickness=0,
                                   activebackground="#6C9587",
                                   command=lambda: print("Reset clicked"), relief="flat")
        self.button_reset.place(x=1028.7451, y=122.033, width=56.9066, height=41.0992)

        self.btn_update = PhotoImage(file=self.relative_to_assets("button_update.png"))
        self.button_update = Button(image=self.btn_update, borderwidth=0, highlightthickness=0,
                                    activebackground="#6C9587",
                                    command=lambda: print("Update clicked"), relief="flat")
        self.button_update.place(x=308.5605, y=474.6403, width=88.5214, height=47.4222)

        self.btn_delete = PhotoImage(file=self.relative_to_assets("button_delete.png"))
        self.button_delete = Button(image=self.btn_delete, borderwidth=0, highlightthickness=0,
                                    activebackground="#6C9587",
                                    command=lambda: print("Delete clicked"), relief="flat")
        self.button_delete.place(x=529.2314, y=474.6403, width=88.5214, height=47.4222)

        self.btn_create = PhotoImage(file=self.relative_to_assets("button_create.png"))
        self.button_create = Button(image=self.btn_create, borderwidth=0, highlightthickness=0,
                                    activebackground="#6C9587",
                                    command=lambda: print("Create clicked"), relief="flat")
        self.button_create.place(x=419.2119, y=474.6403, width=88.5214, height=47.4222)

        self.btn_sales = PhotoImage(file=self.relative_to_assets("button_sales.png"))
        self.button_sales = Button(image=self.btn_sales, borderwidth=0, highlightthickness=0,
                                   activebackground="#6C9587",
                                   command=lambda: print("Sales clicked"), relief="flat")
        self.button_sales.place(x=25.2915, y=345.2334, width=213.7159, height=59.4358)

        self.btn_users = PhotoImage(file=self.relative_to_assets("button_users.png"))
        self.button_users = Button(image=self.btn_users, borderwidth=0, highlightthickness=0,
                                   activebackground="#6C9587",
                                   command=lambda: print("Users clicked"), relief="flat")
        self.button_users.place(x=25.2915, y=421.1089, width=209.9222, height=58.8035)

        self.btn_price = PhotoImage(file=self.relative_to_assets("button_price.png"))
        self.button_price = Button(image=self.btn_price, borderwidth=0, highlightthickness=0,
                                   activebackground="#6C9587",
                                   command=lambda: print("Price clicked"), relief="flat")
        self.button_price.place(x=25.2915, y=268.7256, width=213.7159, height=60.7004)

        self.btn_edit = PhotoImage(file=self.relative_to_assets("button_edit.png"))
        self.button_edit = Button(image=self.btn_edit, borderwidth=0, highlightthickness=0,
                                  activebackground="#6C9587",
                                  command=lambda: print("Edit clicked"), relief="flat")
        self.button_edit.place(x=25.2915, y=188.4241, width=213.7159, height=64.4942)

        self.btn_overview = PhotoImage(file=self.relative_to_assets("button_overview.png"))
        self.button_overview = Button(image=self.btn_overview, borderwidth=0, highlightthickness=0,
                                      activebackground="#6C9587",
                                      command=lambda: print("Overview clicked"), relief="flat")
        self.button_overview.place(x=25.2915, y=116.9747, width=230.1556, height=60.0681)

        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)


if __name__ == "__main__":
    Display_room_info()