from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage


class GUI7:
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
        output_path = Path(__file__).parent
        self.assets_path = output_path.parent / "assets" / "frame7"
        icon_path = self.relative_to_assets("ic_infor.png")
        self.window.iconphoto(False, PhotoImage(file=icon_path))

        # Load background
        self.background_img = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(546.0, 325.0, image=self.background_img)

        # Entries - tối ưu bằng vòng lặp
        entries_data = [
            ("entry_1.png", 677.1885, 122.033, 282.0039, 39.0992, 818.1904, 142.5826),
            ("entry_2.png", 451.459, 400.2433, 170.7198, 35.9377, 536.8189, 419.2121),
            ("entry_3.png", 451.459, 159.9709, 170.7198, 35.9377, 536.8189, 178.9397),
            ("entry_4.png", 451.459, 239.64, 170.7198, 35.9377, 536.8189, 258.6089),
            ("entry_5.png", 451.459, 319.9417, 170.7198, 35.9377, 536.8189, 338.9106),
        ]

        self.entries = []
        for data in entries_data:
            self.entries.append(self.create_entry(*data))

        # Buttons
        self.create_button("button_1.png", 6.0, 583.6089, 119.5039, 55.0097,
                           command=lambda: print("button_logout clicked"))

        self.create_button("button_2.png", 137.0, 584.0, 119.0, 55.0,
                           command=lambda: print("button_quit clicked"))

        self.create_button("button_3.png", 966.1484, 122.033, 56.9066, 41.0992,
                           command=lambda: print("button_tim_kiem clicked"))

        self.create_button("button_4.png", 1028.7451, 122.033, 56.9066, 41.0992,
                           command=lambda: print("button_reset clicked"))

        self.create_button("button_5.png", 308.5605, 474.6403, 88.5214, 47.4222,
                           command=lambda: print("button_update clicked"))

        self.create_button("button_6.png", 529.2314, 474.6403, 88.5214, 47.4222,
                           command=lambda: print("button_delete clicked"))

        self.create_button("button_7.png", 419.2119, 474.6403, 88.5214, 47.4222,
                           command=lambda: print("button_create clicked"))

        self.create_button("button_8.png", 25.2915, 345.2334, 213.7159, 59.4358,
                           command=lambda: print("button_sales clicked"))

        self.create_button("button_9.png", 25.2915, 421.1089, 209.9222, 58.8035,
                           command=lambda: print("button_users clicked"))

        self.create_button("button_10.png", 25.2915, 268.7256, 213.7159, 60.7004,
                           command=lambda: print("button_price clicked"))

        self.create_button("button_11.png", 25.2915, 188.4241, 213.7159, 64.4942,
                           command=lambda: print("button_edit clicked"))

        self.create_button("button_12.png", 25.2915, 116.9747, 230.1556, 60.0681,
                           command=lambda: print("button_overview clicked"))

        self.window.mainloop()

    def create_button(self, img_name, x, y, width, height, command):
        button_image = PhotoImage(file=self.relative_to_assets(img_name))
        button = Button(
            image=button_image,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#56908B",
            command=command,
            relief="flat"
        )
        button.image = button_image
        button.place(x=x, y=y, width=width, height=height)

    def create_entry(self, img_name, x, y, width, height, img_x, img_y):
        entry_image = PhotoImage(file=self.relative_to_assets(img_name))
        self.canvas.create_image(img_x, img_y, image=entry_image)

        entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        entry.place(x=x, y=y, width=width, height=height)
        entry.image = entry_image
        return entry

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)


if __name__ == "__main__":
    GUI7()
