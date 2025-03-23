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

        # Entries:
        # Load entry images
        self.entry_images = {
            "entry_1": PhotoImage(file=self.relative_to_assets("entry_1.png")),
            "entry_5": PhotoImage(file=self.relative_to_assets("entry_5.png"))
        }
        self.entries = []

        # Entry 1
        self.canvas.create_image(636.6665 + 232.0 / 2, 197.3333 + 26.6667 / 2, image=self.entry_images["entry_1"])
        self.entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=636.6665, y=197.3333, width=232.0, height=26.6667)
        self.entries.append(self.entry_1)

        # Entry 2
        self.canvas.create_image(636.6665 + 232.0 / 2, 244.0 + 26.6667 / 2, image=self.entry_images["entry_1"])
        self.entry_2 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=636.6665, y=244.0, width=232.0, height=26.6667)
        self.entries.append(self.entry_2)

        # Entry 3
        self.canvas.create_image(636.6665 + 232.0 / 2, 290.6667 + 26.6667 / 2, image=self.entry_images["entry_1"])
        self.entry_3 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_3.place(x=636.6665, y=290.6667, width=232.0, height=26.6667)
        self.entries.append(self.entry_3)

        # Entry 4
        self.canvas.create_image(636.6665 + 232.0 / 2, 337.3333 + 26.6667 / 2, image=self.entry_images["entry_1"])
        self.entry_4 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_4.place(x=636.6665, y=337.3333, width=232.0, height=26.6667)
        self.entries.append(self.entry_4)

        # Entry 5
        self.canvas.create_image(213.3335 + 151.3333 / 2, 162.0 + 21.3333 / 2, image=self.entry_images["entry_5"])
        self.entry_5 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_5.place(x=213.3335, y=162.0, width=151.3333, height=21.3333)
        self.entries.append(self.entry_5)

        # Entry 6
        self.canvas.create_image(213.3335 + 151.3333 / 2, 125.3333 + 21.3333 / 2, image=self.entry_images["entry_5"])
        self.entry_6 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_6.place(x=213.3335, y=125.3333, width=151.3333, height=21.3333)
        self.entries.append(self.entry_6)

        # Buttons
        # Button Booking
        self.btn_img_booking = PhotoImage(file=self.relative_to_assets("button_booking.png"))
        self.button_booking = Button(image=self.btn_img_booking, borderwidth=0, highlightthickness=0, activebackground="#6C9587",
                               command=lambda: print("button_Booking clicked"), relief="flat")
        self.button_booking.place(x=42.9998, y=523.0, width=125.0, height=49.0)

        #Button Cart
        self.btn_img_cart = PhotoImage(file=self.relative_to_assets("button_cart.png"))
        self.button_cart = Button(image=self.btn_img_cart, borderwidth=0, highlightthickness=0, activebackground="#6C9587",
                               command=lambda: print("button_Cart clicked"), relief="flat")
        self.button_cart.place(x=183.0, y=524.0, width=98.0, height=48.0)

        #Button Invoice
        self.btn_img_invoice = PhotoImage(file=self.relative_to_assets("button_invoice.png"))
        self.button_invoice = Button(image=self.btn_img_invoice, borderwidth=0, highlightthickness=0, activebackground="#6C9587",
                               command=lambda: print("button_Invoice clicked"), relief="flat")
        self.button_invoice.place(x=791.0, y=524.0, width=124.0, height=48.0)

        #Button Back
        self.btn_img_back = PhotoImage(file=self.relative_to_assets("button_back.png"))
        self.button_back = Button(image=self.btn_img_back, borderwidth=0, highlightthickness=0, activebackground="#6C9587",
                               command=lambda: print("button_Back clicked"), relief="flat")
        self.button_back.place(x=668.0, y=523.0, width=110.0, height=49.0)

        #Button Confirm
        self.btn_img_confirm = PhotoImage(file=self.relative_to_assets("button_confirm.png"))
        self.button_confirm = Button(image=self.btn_img_confirm, borderwidth=0, highlightthickness=0, activebackground="#6C9587",
                               command=lambda: print("button_5 (Confirm) clicked"), relief="flat")
        self.button_confirm.place(x=645.0, y=407.0, width=104.0, height=42.0)

        #Button Delete
        self.btn_img_delete = PhotoImage(file=self.relative_to_assets("button_delete.png"))
        self.button_delete = Button(image=self.btn_img_delete, borderwidth=0, highlightthickness=0, activebackground="#6C9587",
                               command=lambda: print("button_6 (Delete) clicked"), relief="flat")
        self.button_delete.place(x=390.6665, y=94.6667, width=60.0, height=23.7778)

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
