from tkinter import *
from pathlib import Path


class CartCustomerDetails:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("966x600")
        self.window.title("Cart and Customer Details")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)

        # Canvas setup
        self.canvas = Canvas(self.window, bg="#FFFFFF", height=600, width=966, bd=0, highlightthickness=0,
                             relief="ridge")
        self.canvas.place(x=0, y=0)

        # Asset path
        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Users" / "Frame 4_Cart and Customer Details"

        # Icon setup
        icon_path = self.relative_to_assets("icon_cart.png")
        self.window.iconphoto(False, PhotoImage(file=icon_path))

        # Load background images
        self.background_img = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(484.0, 300.0, image=self.background_img)

        self.image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.canvas.create_image(254.0, 146.0, image=self.image_2)

        # Entries
        self.entry_images = {
            "entry_1": PhotoImage(file=self.relative_to_assets("entry_1.png")),
            "entry_5": PhotoImage(file=self.relative_to_assets("entry_5.png"))}
        entry_data = [
            (636.6665, 197.3333, 232.0, 26.6667, "entry_1"),
            (636.6665, 244.0, 232.0, 26.6667, "entry_1"),
            (636.6665, 290.6667, 232.0, 26.6667, "entry_1"),
            (636.6665, 337.3333, 232.0, 26.6667, "entry_1"),
            (213.3335, 162.0, 151.3333, 21.3333, "entry_5"),
            (213.3335, 125.3333, 151.3333, 21.3333, "entry_5")]

        self.entries = []
        for x, y, width, height, img_key in entry_data:
            self.canvas.create_image(x + width / 2, y + height / 2, image=self.entry_images[img_key])
            entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
            entry.place(x=x, y=y, width=width, height=height)
            self.entries.append(entry)

        # Buttons
        # Button Booking
        self.btn_img_1 = PhotoImage(file=self.relative_to_assets("button_booking.png"))
        self.button_1 = Button(image=self.btn_img_1, borderwidth=0, highlightthickness=0, activebackground="#6C9587",
                               command=lambda: print("button_Booking clicked"), relief="flat")
        self.button_1.place(x=42.9998, y=523.0, width=125.0, height=49.0)

        #Button Cart
        self.btn_img_2 = PhotoImage(file=self.relative_to_assets("button_cart.png"))
        self.button_2 = Button(image=self.btn_img_2, borderwidth=0, highlightthickness=0, activebackground="#6C9587",
                               command=lambda: print("button_Cart clicked"), relief="flat")
        self.button_2.place(x=183.0, y=524.0, width=98.0, height=48.0)

        #Button Invoice
        self.btn_img_3 = PhotoImage(file=self.relative_to_assets("button_invoice.png"))
        self.button_3 = Button(image=self.btn_img_3, borderwidth=0, highlightthickness=0, activebackground="#6C9587",
                               command=lambda: print("button_Invoice clicked"), relief="flat")
        self.button_3.place(x=791.0, y=524.0, width=124.0, height=48.0)

        #Button Back
        self.btn_img_4 = PhotoImage(file=self.relative_to_assets("button_back.png"))
        self.button_4 = Button(image=self.btn_img_4, borderwidth=0, highlightthickness=0, activebackground="#6C9587",
                               command=lambda: print("button_Back clicked"), relief="flat")
        self.button_4.place(x=668.0, y=523.0, width=110.0, height=49.0)

        #Button Confirm
        self.btn_img_5 = PhotoImage(file=self.relative_to_assets("button_confirm.png"))
        self.button_5 = Button(image=self.btn_img_5, borderwidth=0, highlightthickness=0, activebackground="#6C9587",
                               command=lambda: print("button_5 (Confirm) clicked"), relief="flat")
        self.button_5.place(x=645.0, y=407.0, width=104.0, height=42.0)

        #Button Delete
        self.btn_img_6 = PhotoImage(file=self.relative_to_assets("button_delete.png"))
        self.button_6 = Button(image=self.btn_img_6, borderwidth=0, highlightthickness=0, activebackground="#6C9587",
                               command=lambda: print("button_6 (Delete) clicked"), relief="flat")
        self.button_6.place(x=390.6665, y=94.6667, width=60.0, height=23.7778)

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

if __name__ == "__main__":
    CartCustomerDetails()
