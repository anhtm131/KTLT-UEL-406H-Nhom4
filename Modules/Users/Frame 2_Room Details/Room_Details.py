from tkinter import *
from pathlib import Path

class Room_details:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("584x550")
        self.window.title("Room Details")
        self.window.configure(bg="#6C947E")
        self.window.resizable(False, False)

        # Canvas setup
        self.canvas = Canvas(self.window, bg="#6C947E", height=550, width=584, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        # Asset path
        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Users" / "Frame 2_Room Details"

        # Icon setup
        icon_path = self.relative_to_assets("ic_room.png")
        self.window.iconphoto(False, PhotoImage(file=icon_path))

        # Load images
        self.background_img = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(292.0, 275.0, image=self.background_img)

        #Entries
        # Load entry image
        self.entry_image = PhotoImage(file=self.relative_to_assets("entry_1.png"))

        # Load entry image
        self.entry_image = PhotoImage(file=self.relative_to_assets("entry_1.png"))

        # Entry 1
        self.canvas.create_image(385.0, 149.1875 + 18 + 2, image=self.entry_image)
        self.entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=228.9375, y=149.1875 + 2, width=312.125, height=33.7)

        # Entry 2
        self.canvas.create_image(385.0, 204.71633911132812 + 18 + 2, image=self.entry_image)
        self.entry_2 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=228.9375, y=204.71633911132812 + 2, width=312.125, height=33.7)

        # Entry 3
        self.canvas.create_image(385.0, 262.625 + 18 + 2, image=self.entry_image)
        self.entry_3 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_3.place(x=228.9375, y=262.625 + 2, width=312.125, height=33.7)

        # Entry 4
        self.canvas.create_image(385.0, 319.7403564453125 + 18 + 2, image=self.entry_image)
        self.entry_4 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_4.place(x=228.9375, y=319.7403564453125 + 2, width=312.125, height=33.7)

        # Buttons
        # Button available
        self.btn_img_avai = PhotoImage(file=self.relative_to_assets("button_avai.png"))
        self.button_avai = Button(image=self.btn_img_avai,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground="#6C947F",
                               command=lambda: print("button_available clicked"), relief="flat")
        self.button_avai.place(x=123.0, y=382.0, width=135.0, height=48.0)

        # Button Cleaning
        self.btn_img_cleaning = PhotoImage(file=self.relative_to_assets("button_cleaning.png"))
        self.button_cleaning = Button(image=self.btn_img_cleaning,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground="#6C947F",
                               command=lambda: print("button_cleaning clicked"), relief="flat")
        self.button_cleaning.place(x=339.0, y=382.0, width=135.0, height=47.0)

        # Button Checkout
        self.btn_img_checkout = PhotoImage(file=self.relative_to_assets("button_checkout.png"))
        self.button_checkout = Button(image=self.btn_img_checkout,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground="#6C947F",
                               command=lambda: print("button_checkout clicked"), relief="flat")
        self.button_checkout.place(x=342.0, y=453.0, width=135.0, height=47.0)

        # Button Checkin
        self.btn_img_checkin = PhotoImage(file=self.relative_to_assets("button_checkin.png"))
        self.button_checkin = Button(image=self.btn_img_checkin,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground="#6C947F",
                               command=lambda: print("button_checkin clicked"), relief="flat")
        self.button_checkin.place(x=123.0, y=452.0, width=135.0, height=48.0)

        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

if __name__ == "__main__":
    Room_details()
