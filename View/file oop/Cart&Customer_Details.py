from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from pathlib import Path

class GUI4:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("966x600")
        self.window.title("Cart and Customer Details")
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
        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH.parent / "assets" / "frame4"
        icon_path = self.relative_to_assets("icon_cart.png")
        self.window.iconphoto(False, PhotoImage(file=icon_path))

        # Load images
        self.background_img = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(484.0, 300.0, image=self.background_img)

        self.image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.canvas.create_image(254.0, 146.0, image=self.image_2)

        # Create entries
        self.create_entries()

        # Create buttons (full 6 buttons)
        self.create_buttons()

        # Static text
        self.canvas.create_text(
            71.0, 97.0,
            anchor="nw",
            text="P.101 - Deluxe - Price: 3.000.000 ",
            fill="#FFFFFF",
            font=("PTSerif Caption", 16 * -1)
        )

        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

    def create_entries(self):
        entry_data = [
            (636.6665, 197.3333, 232.0, 26.6667),
            (636.6665, 244.0, 232.0, 26.6667),
            (636.6665, 290.6667, 232.0, 26.6667),
            (636.6665, 337.3333, 232.0, 26.6667),
            (213.3335, 162.0, 151.3333, 21.3333),
            (213.3335, 125.3333, 151.3333, 21.3333)
        ]

        self.entries = []

        for i, (x, y, width, height) in enumerate(entry_data, start=1):
            entry_img = PhotoImage(file=self.relative_to_assets(f"entry_{i}.png"))
            self.canvas.create_image(x + width / 2, y + height / 2, image=entry_img)

            entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
            entry.place(x=x, y=y, width=width, height=height)

            # Lưu trữ Entry và Image để tránh bị xóa bởi garbage collector
            self.entries.append((entry, entry_img))

    def create_buttons(self):
        # Button 1 Booking
        self.btn_img_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(image=self.btn_img_1, borderwidth=0, highlightthickness=0, activebackground="#6C9587",
        command=lambda: print("button_Booking clicked"), relief="flat")
        self.button_1.place(x=42.9998, y=523.0, width=125.0, height=49.0)

        # Button 2 Cart
        self.btn_img_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(image=self.btn_img_2, borderwidth=0, highlightthickness=0, activebackground="#6C9587",
        command=lambda: print("button_Cart clicked"), relief="flat")
        self.button_2.place(x=183.0, y=524.0, width=98.0, height=48.0)

        # Button 3 Invoice
        self.btn_img_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(image=self.btn_img_3, borderwidth=0, highlightthickness=0, activebackground="#6C9587",
        command=lambda: print("button_Invoice clicked"), relief="flat")
        self.button_3.place(x=791.0, y=524.0, width=124.0, height=48.0)

        # Button 4 Back
        self.btn_img_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = Button(image=self.btn_img_4, borderwidth=0, highlightthickness=0, activebackground="#6C9587",
        command=lambda: print("button_Back clicked"), relief="flat")
        self.button_4.place(x=668.0, y=523.0, width=110.0, height=49.0)

        # Button 5 (Confirm)
        self.btn_img_5 = PhotoImage(file=self.relative_to_assets("button_5.png"))
        self.button_5 = Button(image=self.btn_img_5, borderwidth=0, highlightthickness=0, activebackground="#6C9587",
        command=lambda: print("button_5 (Confirm) clicked"), relief="flat")
        self.button_5.place(x=645.0, y=407.0, width=104.0, height=42.0)

        # Button 6 (Delete)
        self.btn_img_6 = PhotoImage(file=self.relative_to_assets("button_6.png"))
        self.button_6 = Button(image=self.btn_img_6, borderwidth=0, highlightthickness=0, activebackground="#6C9587",
        command=lambda: print("button_6 (Delete) clicked"), relief="flat")
        self.button_6.place(x=390.6665, y=94.6667, width=60.0, height=23.7778)

if __name__ == "__main__":
    GUI4()
