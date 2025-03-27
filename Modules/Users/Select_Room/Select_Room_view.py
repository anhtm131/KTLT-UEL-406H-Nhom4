from tkinter import *
from pathlib import Path


class SelectRoom:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("966x600")
        self.window.title("Select Room")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=600, width=966, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Users" / "Select_Room"

        self.window.iconphoto(False, PhotoImage(file=self.relative_to_assets("icon_select.png")))

        self.background_img = PhotoImage(file=self.relative_to_assets("background_select_room.png"))
        self.canvas.create_image(483.0, 300.0, image=self.background_img)

        self.button_booking_img = PhotoImage(file=self.relative_to_assets("button_booking.png"))
        self.button_booking = Button(image=self.button_booking_img, borderwidth=0, highlightthickness=0, activebackground="#6C947F",
                                      command=lambda: print("Booking button clicked"), relief="flat")
        self.button_booking.place(x=43.0, y=524.0, width=124.0, height=48.0)

        self.button_cart_img = PhotoImage(file=self.relative_to_assets("button_cart.png"))
        self.button_cart = Button(image=self.button_cart_img, borderwidth=0, highlightthickness=0, activebackground="#6C947F",
                                   command=lambda: print("Cart button clicked"), relief="flat")
        self.button_cart.place(x=183.0, y=524.0, width=98.0, height=47.0)

        self.button_invoice_img = PhotoImage(file=self.relative_to_assets("button_invoice.png"))
        self.button_invoice = Button(image=self.button_invoice_img, borderwidth=0, highlightthickness=0, activebackground="#6C947F",
                                      command=lambda: print("Invoice button clicked"), relief="flat")
        self.button_invoice.place(x=791.0, y=524.0, width=124.0, height=47.0)

        self.button_back_img = PhotoImage(file=self.relative_to_assets("button_back.png"))
        self.button_back = Button(image=self.button_back_img, borderwidth=0, highlightthickness=0, activebackground="#6C947F",
                                   command=lambda: print("Back button clicked"), relief="flat")
        self.button_back.place(x=668.0, y=524.0, width=109.0, height=47.0)

        self.button_add_img = PhotoImage(file=self.relative_to_assets("button_add.png"))
        self.button_add = Button(image=self.button_add_img, borderwidth=0, highlightthickness=0, activebackground="#6C947F",command=lambda: print("Add button clicked"), relief="flat")
        self.button_add.place(x=683, y=455, width=80.9, height=36.35)

        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)


if __name__ == "__main__":
    SelectRoom()