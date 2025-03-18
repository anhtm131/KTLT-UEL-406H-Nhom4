from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage


class GUI5:
    def __init__(self):
        self.window = Tk()
        self.window.title("Invoice")
        self.window.geometry("966x600")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)

        # Canvas setup
        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=600,
            width=966,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        # Asset path
        output_path = Path(__file__).parent
        self.assets_path = output_path.parent / "assets" / "frame5"

        icon_path = self.relative_to_assets("icon.png")
        self.window.iconphoto(False, PhotoImage(file=icon_path))

        # Load background
        self.background_img = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(483.0, 300.0, image=self.background_img)

        # Draw green rectangle
        self.canvas.create_rectangle(
            168.6665, 96.6667, 797.3332, 339.3333, fill="#346B4E", outline=""
        )

        # Static text
        self.canvas.create_text(
            278.6665, 300.0,
            anchor="nw",
            text="Total Cost:",
            fill="#FFFFFF",
            font=("PTSerif Caption", 20 * -1)
        )

        # Entries
        entries_data = [
            ("entry_1.png", 404.6665, 300.0, 244.6667, 26.6667, 527.0, 314.3333),
        ]

        self.entries = []
        for data in entries_data:
            self.entries.append(self.create_entry(*data))

        # Buttons
        #Button back
        self.create_button("button_1.png", 671.0, 527.0, 110.0, 47.0,
                           command=lambda: print("button_back clicked"))

        #Button booking
        self.create_button("button_2.png", 46.0, 527.0, 125.0, 48.0,
                           command=lambda: print("button_booking clicked"))

        #Button cart
        self.create_button("button_3.png", 186.0, 526.0, 98.0, 49.0,
                           command=lambda: print("button_cart clicked"))

        #button invoice
        self.create_button("button_4.png", 795.0, 527.0, 124.0, 47.0,
                           command=lambda: print("button_invoice clicked"))

        self.window.mainloop()

    def create_button(self, img_name, x, y, width, height, command):
        button_image = PhotoImage(file=self.relative_to_assets(img_name))
        button = Button(
            image=button_image,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#6C9587",
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
    GUI5()
