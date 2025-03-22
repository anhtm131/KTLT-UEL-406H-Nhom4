from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage


class Invoice:
    def __init__(self):
        self.window = Tk()
        self.window.title("Invoice")
        self.window.geometry("966x600")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)

        # Canvas setup
        self.canvas = Canvas(self.window,
            bg="#FFFFFF",
            height=600,
            width=966,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        # Asset path
        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Users" / "Frame 5_Invoice"

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

        # Entry
        entry_img = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.canvas.create_image(527.0, 314.3333, image=entry_img)
        entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        entry.place(x=404.6665, y=300.0, width=244.6667, height=26.6667)

        # Buttons
        # Button Back
        self.btn_back_img = PhotoImage(file=self.relative_to_assets("button_back.png"))
        self.button_back = Button(
            image=self.btn_back_img, borderwidth=0, highlightthickness=0,
            activebackground="#6C9587", command=lambda: print("button_back clicked"), relief="flat"
        )
        self.button_back.place(x=671.0, y=527.0, width=110.0, height=47.0)

        #Button Booking
        self.btn_booking_img = PhotoImage(file=self.relative_to_assets("button_booking.png"))
        self.button_booking = Button(
            image=self.btn_booking_img, borderwidth=0, highlightthickness=0,
            activebackground="#6C9587", command=lambda: print("button_booking clicked"), relief="flat"
        )
        self.button_booking.place(x=46.0, y=527.0, width=125.0, height=48.0)

        #Button Cart
        self.btn_cart_img = PhotoImage(file=self.relative_to_assets("button_cart.png"))
        self.button_cart = Button(
            image=self.btn_cart_img, borderwidth=0, highlightthickness=0,
            activebackground="#6C9587", command=lambda: print("button_cart clicked"), relief="flat"
        )
        self.button_cart.place(x=186.0, y=526.0, width=98.0, height=49.0)

        #Button Invoice
        self.btn_invoice_img = PhotoImage(file=self.relative_to_assets("button_invoice.png"))
        self.button_invoice = Button(
            image=self.btn_invoice_img, borderwidth=0, highlightthickness=0,
            activebackground="#6C9587", command=lambda: print("button_invoice clicked"), relief="flat"
        )
        self.button_invoice.place(x=795.0, y=527.0, width=124.0, height=47.0)

        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)


if __name__ == "__main__":
    Invoice()
