from tkinter import *
from pathlib import Path


class RoomDetails:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("584x550")
        self.window.title("Room Details")
        self.window.configure(bg="#6C947E")
        self.window.resizable(False, False)

        self.canvas = Canvas(self.window, bg="#6C947E", height=550, width=584, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Users" / "Room_details"

        self.window.iconphoto(False, PhotoImage(file=self.relative_to_assets("icon_room.png")))

        self.background_img = PhotoImage(file=self.relative_to_assets("background_roomdetails.png"))
        self.canvas.create_image(292.0, 275.0, image=self.background_img)


        self.entry_name = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_name.place(x=228.9375, y=151.1875, width=312.125, height=33.7)


        self.entry_phone = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_phone.place(x=228.9375, y=206.71633911132812, width=312.125, height=33.7)


        self.entry_cccd = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_cccd.place(x=228.9375, y=264.625, width=312.125, height=33.7)


        self.entry_time = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_time.place(x=228.9375, y=321.7403564453125, width=312.125, height=33.7)

        self.button_available_img = PhotoImage(file=self.relative_to_assets("button_avai.png"))
        self.button_available = Button(image=self.button_available_img, borderwidth=0, highlightthickness=0, activebackground="#6C947F", command=lambda: print("button_available clicked"), relief="flat")
        self.button_available.place(x=123.0, y=382.0, width=135.0, height=48.0)

        self.button_cleaning_img = PhotoImage(file=self.relative_to_assets("button_cleaning.png"))
        self.button_cleaning = Button(image=self.button_cleaning_img, borderwidth=0, highlightthickness=0, activebackground="#6C947F", command=lambda: print("button_cleaning clicked"), relief="flat")
        self.button_cleaning.place(x=339.0, y=382.0, width=135.0, height=47.0)

        self.button_checkout_img = PhotoImage(file=self.relative_to_assets("button_checkout.png"))
        self.button_checkout = Button(image=self.button_checkout_img, borderwidth=0, highlightthickness=0, activebackground="#6C947F", command=lambda: print("button_checkout clicked"), relief="flat")
        self.button_checkout.place(x=342.0, y=453.0, width=135.0, height=47.0)

        self.button_checkin_img = PhotoImage(file=self.relative_to_assets("button_checkin.png"))
        self.button_checkin = Button(image=self.button_checkin_img, borderwidth=0, highlightthickness=0, activebackground="#6C947F", command=lambda: print("button_checkin clicked"), relief="flat")
        self.button_checkin.place(x=123.0, y=452.0, width=135.0, height=48.0)

        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)


if __name__ == "__main__":
    RoomDetails()