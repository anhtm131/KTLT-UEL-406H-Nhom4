from tkinter import *
from pathlib import Path


class Invoice:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("966x600")
        self.window.title("Invoice")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=600, width=966, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        OUTPUT_PATH = Path(__file__).parent
        self.assets_frame_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Users" / "Invoice"

        self.window.iconphoto(False, PhotoImage(file=self.relative_to_assets("icon.png", "Frame")))
        self.background_img = PhotoImage(file=self.relative_to_assets("background_invoices.png", "Frame"))
        self.canvas.create_image(483.0, 300.0, image=self.background_img)

        self.entry_total = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_total.place(x=427.48, y=464.49, width=244.75, height=28.68)




        self.button_img_back = PhotoImage(file=self.relative_to_assets("button_back.png", "Frame"))
        self.button_back = Button(image=self.button_img_back, borderwidth=0, highlightthickness=0, activebackground="#6C9587", command=lambda: print("Back button clicked"), relief="flat")
        self.button_back.place(x=671.0, y=527.0, width=110.0, height=47.0)

        self.button_img_booking = PhotoImage(file=self.relative_to_assets("button_booking.png", "Frame"))
        self.button_booking = Button(image=self.button_img_booking, borderwidth=0, highlightthickness=0, activebackground="#6C9587", command=lambda: print("Booking button clicked"), relief="flat")
        self.button_booking.place(x=46.0, y=527.0, width=125.0, height=48.0)

        self.button_img_cart = PhotoImage(file=self.relative_to_assets("button_cart.png", "Frame"))
        self.button_cart = Button(image=self.button_img_cart, borderwidth=0, highlightthickness=0, activebackground="#6C9587", command=lambda: print("Cart button clicked"), relief="flat")
        self.button_cart.place(x=186.0, y=526.0, width=98.0, height=49.0)

        self.button_img_invoice = PhotoImage(file=self.relative_to_assets("button_invoice.png", "Frame"))
        self.button_invoice = Button(image=self.button_img_invoice, borderwidth=0, highlightthickness=0, activebackground="#6C9587", command=lambda: print("Invoice button clicked"), relief="flat")
        self.button_invoice.place(x=795.0, y=527.0, width=124.0, height=47.0)

        #self.window.mainloop()

    def relative_to_assets(self, path: str, assets_type: str = "Frame") -> Path:
        if assets_type == "Frame":
            return self.assets_frame_path / Path(path)


if __name__ == "__main__":
    Invoice()