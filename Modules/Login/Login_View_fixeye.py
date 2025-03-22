from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

class Login:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("840x600")
        self.window.title("Welcome to Majestic Pearl")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)

        # Canvas setup
        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=600,
            width=840,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        # Asset path
        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH.parent.parent / "Images" / "Login"

        icon_path = self.relative_to_assets("icon pearl.png")
        self.window.iconphoto(False, PhotoImage(file=icon_path))

        # Load background image
        self.image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(420.0, 300.0, image=self.image_1)

        # Entries
        self.entry_image = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entries = []
        positions = [(558.7, 315.2, 464.6, 301.8), (558.7, 263.7, 464.6, 250.2)]

        for i, (img_x, img_y, entry_x, entry_y) in enumerate(positions, start=1):
            self.canvas.create_image(img_x, img_y, image=self.entry_image)
            entry = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
            entry.place(x=entry_x, y=entry_y, width=188.1, height=25.0)
            self.entries.append(entry)

        # Button login
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_login.png"))
        self.login_button = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#3D6C49",
            command=lambda: print("button_login clicked"),
            relief="flat"
        )
        self.login_button.place(x=512.0, y=348.0, width=81.0, height=41.0)

        # Button con mắt mở
        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_open_eye.png"))
        self.forgot_button = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#3B6A4F",
            command=lambda: print("button_openeye clicked"),
            relief="flat"
        )
        self.forgot_button.place(x=620.0, y=218.0, width=41.0, height=21.0)

        # Button con mắt nhắm
        self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_close_eye.png"))
        self.cancel_button = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#294631",
            command=lambda: print("button_close eye clicked"),
            relief="flat"
        )
        self.cancel_button.place(x=614.0, y=337.0, width=42.0, height=23.0)

        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

if __name__ == "__main__":
    Login()
