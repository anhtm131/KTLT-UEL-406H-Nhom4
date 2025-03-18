from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

class LoginGUI:
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
        output_path = Path(__file__).parent
        self.assets_path = output_path.parent / "assets" / "framelogin"

        icon_path = self.relative_to_assets("icon pearl.png")
        self.window.iconphoto(False, PhotoImage(file=icon_path))

        # Load background image
        self.image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(420.0, 300.0, image=self.image_1)

        # Entry 1
        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.canvas.create_image(558.7, 315.2, image=self.entry_image_1)
        self.entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=464.6, y=301.8, width=188.1, height=25.0)

        # Entry 2
        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.canvas.create_image(558.7, 263.7, image=self.entry_image_2)
        self.entry_2 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=464.6, y=250.2, width=188.1, height=25.0)

        # Button login
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
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
        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.forgot_button = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#3B6A4F",
            command=lambda: print("button_con mắt mở clicked"),
            relief="flat"
        )
        self.forgot_button.place(x=620.0, y=218.0, width=41.0, height=21.0)

        # Button con mắt nhắm
        self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.cancel_button = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#294631",
            command=lambda: print("button_con mắt nhắm clicked"),
            relief="flat"
        )
        self.cancel_button.place(x=614.0, y=337.0, width=42.0, height=23.0)

        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

if __name__ == "__main__":
    LoginGUI()
