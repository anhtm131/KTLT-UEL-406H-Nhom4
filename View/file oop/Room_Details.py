from tkinter import *
from pathlib import Path

class GUI2:
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
        BASE_DIR = Path(__file__).resolve().parent.parent
        self.assets_path = BASE_DIR / "assets" / "frame2"
        icon_path = self.relative_to_assets("ic_room.png")
        self.window.iconphoto(False, PhotoImage(file=icon_path))

        # Load images
        self.background_img = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(292.0, 275.0, image=self.background_img)

        # Entries
        entry_positions = [
            (228.9375, 149.1875),
            (228.9375, 204.71633911132812),
            (228.9375, 262.625),
            (228.9375, 319.7403564453125)
        ]

        for i, (x, y) in enumerate(entry_positions, start=1):
            entry_image = PhotoImage(file=self.relative_to_assets(f"entry_{i}.png"))
            self.canvas.create_image(385.0, y + 18, image=entry_image)
            entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
            entry.place(x=x, y=y, width=312.125, height=33.7)

        # Buttons
        #Button available
        self.btn_img_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(image=self.btn_img_1,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground="#6C947F",
                               command=lambda: print("button_available clicked"), relief="flat")
        self.button_1.place(x=123.0, y=382.0, width=135.0, height=48.0)

        #button cleaning
        self.btn_img_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(image=self.btn_img_2,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground="#6C947F",
                               command=lambda: print("button_cleaning clicked"), relief="flat")
        self.button_2.place(x=339.0, y=382.0, width=135.0, height=47.0)

        #Button checkout
        self.btn_img_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(image=self.btn_img_3,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground="#6C947F",
                               command=lambda: print("button_checkout clicked"), relief="flat")
        self.button_3.place(x=342.0, y=453.0, width=135.0, height=47.0)

        #Button checkin
        self.btn_img_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = Button(image=self.btn_img_4,
                               borderwidth=0,
                               highlightthickness=0,
                               activebackground="#6C947F",
                               command=lambda: print("button_checkin clicked"), relief="flat")
        self.button_4.place(x=123.0, y=452.0, width=135.0, height=48.0)

        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

if __name__ == "__main__":
    GUI2()
