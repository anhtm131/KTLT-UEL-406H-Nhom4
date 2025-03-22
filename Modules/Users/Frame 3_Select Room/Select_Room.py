from tkinter import *
from pathlib import Path


class Select_Room:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("966x600")
        self.window.title("Select Room")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)

        # Canvas setup
        self.canvas = Canvas(self.window, bg="#FFFFFF", height=600, width=966, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        # Asset path
        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Users" / "Frame 3_Select Room"

        # Icon setup
        icon_path = self.relative_to_assets("select.png")
        self.window.iconphoto(False, PhotoImage(file=icon_path))

        # Load background
        self.background_img = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(483.0, 300.0, image=self.background_img)

        # Entry
        self.entry_image = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.canvas.create_image(465.333, 104.333, image=self.entry_image)
        self.entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry.place(x=165.333, y=89.333, width=600.667, height=28.0)

        # Buttons
        # Button Booking
        self.btn_img_1 = PhotoImage(file=self.relative_to_assets("button_booking.png"))
        self.button_1 = Button(image=self.btn_img_1, borderwidth=0, highlightthickness=0, activebackground="#6C947F",
                               command=lambda: print("button_booking clicked"), relief="flat")
        self.button_1.place(x=43.0, y=524.0, width=124.0, height=48.0)

        # Button Cart
        self.btn_img_2 = PhotoImage(file=self.relative_to_assets("button_cart.png"))
        self.button_2 = Button(image=self.btn_img_2, borderwidth=0, highlightthickness=0, activebackground="#6C947F",
                               command=lambda: print("button_cart clicked"), relief="flat")
        self.button_2.place(x=183.0, y=524.0, width=98.0, height=47.0)

        # Button Invoice
        self.btn_img_3 = PhotoImage(file=self.relative_to_assets("button_invoice.png"))
        self.button_3 = Button(image=self.btn_img_3, borderwidth=0, highlightthickness=0, activebackground="#6C947F",
                               command=lambda: print("button_invoice clicked"), relief="flat")
        self.button_3.place(x=791.0, y=524.0, width=124.0, height=47.0)

        # Button Back
        self.btn_img_4 = PhotoImage(file=self.relative_to_assets("button_back.png"))
        self.button_4 = Button(image=self.btn_img_4, borderwidth=0, highlightthickness=0, activebackground="#6C947F",
                               command=lambda: print("button_back clicked"), relief="flat")
        self.button_4.place(x=668.0, y=524.0, width=109.0, height=47.0)

        # Button Add
        self.btn_img_5 = PhotoImage(file=self.relative_to_assets("button_add.png"))
        self.button_5 = Button(image=self.btn_img_5, borderwidth=0, highlightthickness=0, activebackground="#6C947F",
                               command=lambda: print("button_add clicked"), relief="flat")
        self.button_5.place(x=710.0, y=92.667, width=52.667, height=23.667)

        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)


if __name__ == "__main__":
    Select_Room()
