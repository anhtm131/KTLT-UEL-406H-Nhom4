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
        self.entries = []
        entry_data = [
            ("entry_1.png", 677.1885, 122.033, 282.0039, 39.0992, 818.1904, 142.5826),
            ("entry_2.png", 451.459, 400.2433, 170.7198, 35.9377, 536.8189, 419.2121),
            ("entry_3.png", 451.459, 159.9709, 170.7198, 35.9377, 536.8189, 178.9397),
            ("entry_4.png", 451.459, 239.64, 170.7198, 35.9377, 536.8189, 258.6089),
            ("entry_5.png", 451.459, 319.9417, 170.7198, 35.9377, 536.8189, 338.9106),
        ]

        for img_name, x, y, width, height, img_x, img_y in entry_data:
            entry_image = PhotoImage(file=self.relative_to_assets(img_name))
            self.canvas.create_image(img_x, img_y, image=entry_image)
            entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
            entry.place(x=x, y=y, width=width, height=height)
            entry.image = entry_image
            self.entries.append(entry)

        # Buttons
        self.btn_img_logout = PhotoImage(file=self.relative_to_assets("button_logout.png"))
        self.button_logout = Button(image=self.btn_img_logout, borderwidth=0, highlightthickness=0,
                                    activebackground="#6C9587",
                                    command=lambda: print("Logout clicked"), relief="flat")
        self.button_logout.place(x=6.0, y=583.6089, width=119.5039, height=55.0097)

        self.btn_img_quit = PhotoImage(file=self.relative_to_assets("button_quit.png"))
        self.button_quit = Button(image=self.btn_img_quit, borderwidth=0, highlightthickness=0,
                                  activebackground="#6C9587",
                                  command=lambda: print("Quit clicked"), relief="flat")
        self.button_quit.place(x=137.0, y=584.0, width=119.0, height=55.0)

        self.btn_img_find = PhotoImage(file=self.relative_to_assets("button_find.png"))
        self.button_find = Button(image=self.btn_img_find, borderwidth=0, highlightthickness=0,
                                  activebackground="#6C9587",
                                  command=lambda: print("Find clicked"), relief="flat")
        self.button_find.place(x=966.1484, y=122.033, width=56.9066, height=41.0992)

        self.btn_img_reset = PhotoImage(file=self.relative_to_assets("button_reset.png"))
        self.button_reset = Button(image=self.btn_img_reset, borderwidth=0, highlightthickness=0,
                                   activebackground="#6C9587",
                                   command=lambda: print("Reset clicked"), relief="flat")
        self.button_reset.place(x=1028.7451, y=122.033, width=56.9066, height=41.0992)

        self.btn_img_update = PhotoImage(file=self.relative_to_assets("button_update.png"))
        self.button_update = Button(image=self.btn_img_update, borderwidth=0, highlightthickness=0,
                                    activebackground="#6C9587",
                                    command=lambda: print("Update clicked"), relief="flat")
        self.button_update.place(x=308.5605, y=474.6403, width=88.5214, height=47.4222)

        self.btn_img_delete = PhotoImage(file=self.relative_to_assets("button_delete.png"))
        self.button_delete = Button(image=self.btn_img_delete, borderwidth=0, highlightthickness=0,
                                    activebackground="#6C9587",
                                    command=lambda: print("Delete clicked"), relief="flat")
        self.button_delete.place(x=529.2314, y=474.6403, width=88.5214, height=47.4222)

        self.btn_img_create = PhotoImage(file=self.relative_to_assets("button_create.png"))
        self.button_create = Button(image=self.btn_img_create, borderwidth=0, highlightthickness=0,
                                    activebackground="#6C9587",
                                    command=lambda: print("Create clicked"), relief="flat")
        self.button_create.place(x=419.2119, y=474.6403, width=88.5214, height=47.4222)

        self.btn_img_sales = PhotoImage(file=self.relative_to_assets("button_sales.png"))
        self.button_sales = Button(image=self.btn_img_sales, borderwidth=0, highlightthickness=0,
                                   activebackground="#6C9587",
                                   command=lambda: print("Sales clicked"), relief="flat")
        self.button_sales.place(x=25.2915, y=345.2334, width=213.7159, height=59.4358)

        self.btn_img_users = PhotoImage(file=self.relative_to_assets("button_users.png"))
        self.button_users = Button(image=self.btn_img_users, borderwidth=0, highlightthickness=0,
                                   activebackground="#6C9587",
                                   command=lambda: print("Users clicked"), relief="flat")
        self.button_users.place(x=25.2915, y=421.1089, width=209.9222, height=58.8035)

        self.btn_img_price = PhotoImage(file=self.relative_to_assets("button_price.png"))
        self.button_price = Button(image=self.btn_img_price, borderwidth=0, highlightthickness=0,
                                   activebackground="#6C9587",
                                   command=lambda: print("Price clicked"), relief="flat")
        self.button_price.place(x=25.2915, y=268.7256, width=213.7159, height=60.7004)

        self.btn_img_edit = PhotoImage(file=self.relative_to_assets("button_edit.png"))
        self.button_edit = Button(image=self.btn_img_edit, borderwidth=0, highlightthickness=0,
                                  activebackground="#6C9587",
                                  command=lambda: print("Edit clicked"), relief="flat")
        self.button_edit.place(x=25.2915, y=188.4241, width=213.7159, height=64.4942)

        self.btn_img_overview = PhotoImage(file=self.relative_to_assets("button_overview.png"))
        self.button_overview = Button(image=self.btn_img_overview, borderwidth=0, highlightthickness=0,
                                      activebackground="#6C9587",
                                      command=lambda: print("Overview clicked"), relief="flat")
        self.button_overview.place(x=25.2915, y=116.9747, width=230.1556, height=60.0681)

        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)


if __name__ == "__main__":
    Display_room_info()