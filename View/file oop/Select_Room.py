from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

class GUI3:
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
        BASE_DIR = Path(__file__).resolve().parent.parent
        self.assets_path = BASE_DIR / "assets" / "frame3"
        icon_path = self.relative_to_assets("select.png")
        self.window.iconphoto(False, PhotoImage(file=icon_path))

        # Load images
        self.background_img = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(483.0, 300.0, image=self.background_img)

        # Load button images
        self.button_images = [PhotoImage(file=self.relative_to_assets(f"button_{i}.png")) for i in range(1, 6)]

        # Entry
        entry_image = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.canvas.create_image(465.333, 104.333, image=entry_image)
        entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        entry.place(x=165.333, y=89.333, width=600.667, height=28.0)

        # Buttons
        self.button_booking()
        self.button_cart()
        self.button_invoice()
        self.button_back()
        self.button_add()

        self.window.mainloop()

    def button_booking(self):
        button = Button(image=self.button_images[0],
                        borderwidth=0,
                        highlightthickness=0,
                        activebackground="#6C9587", bg="#6C9587",
                        command=lambda: print("button_1 clicked"), relief="flat")
        button.place(x=43.0, y=524.0, width=124.0, height=48.0)

    def button_cart(self):
        button = Button(image=self.button_images[1],
                        borderwidth=0,
                        highlightthickness=0,
                        activebackground="#6C9587", bg="#6C9587",
                        command=lambda: print("button_2 clicked"), relief="flat")
        button.place(x=183.0, y=524.0, width=98.0, height=47.0)

    def button_invoice(self):
        button = Button(image=self.button_images[2],
                        borderwidth=0,
                        highlightthickness=0,
                        activebackground="#6C9587", bg="#6C9587",
                        command=lambda: print("button_3 clicked"), relief="flat")
        button.place(x=791.0, y=524.0, width=124.0, height=47.0)

    def button_back(self):
        button = Button(image=self.button_images[3],
                        borderwidth=0,
                        highlightthickness=0,
                        activebackground="#6C9587", bg="#6C9587",
                        command=lambda: print("button_4 clicked"), relief="flat")
        button.place(x=668.0, y=524.0, width=109.0, height=47.0)

    def button_add(self):
        button = Button(image=self.button_images[4],
                        borderwidth=0,
                        highlightthickness=0,
                        activebackground="#6C9587", bg="#6C9587",
                        command=lambda: print("button_5 clicked"), relief="flat")
        # Điều chỉnh vị trí để nút "Add" nằm bên trong Entry
        button.place(x=710.0, y=92.667, width=52.667, height=23.667)

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

if __name__ == "__main__":
    GUI3()
