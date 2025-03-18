from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

class GUI5:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1092x650")
        self.window.configure(bg="#FFFFFF")
        self.window.title("Report Information")
        self.window.resizable(False, False)

        # Canvas setup
        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=650,
            width=1092,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        # Asset path
        output_path = Path(__file__).parent
        self.assets_path = output_path.parent / "assets" / "frame9"

        icon_path = self.relative_to_assets("icon_report.png")
        self.window.iconphoto(False, PhotoImage(file=icon_path))

        # Load background
        self.background_img = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(546.0, 325.0, image=self.background_img)

        # Entries
        self.create_entry("entry_1.png", 369.8926, 565.9047, 148.5895, 30.2471, 444.1873, 582.0282) # From
        self.create_entry("entry_2.png", 574.125, 565.9047, 148.5895, 30.2471, 648.4197, 582.0282) # To

        # Button 1 (Logout)
        self.btn_img_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(image=self.btn_img_1, borderwidth=0, highlightthickness=0, activebackground="#51908D",
        command=lambda: print("logout button clicked"), relief="flat")
        self.button_1.place(x=6.0, y=584.0, width=119.5039, height=55.0097)

        # Button 2 (Quit)
        self.btn_img_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(image=self.btn_img_2, borderwidth=0, highlightthickness=0, activebackground="#51908D",
        command=lambda: print("quit button clicked"), relief="flat")
        self.button_2.place(x=138.0, y=585.0, width=118.8716, height=53.1128)

        # Button 3 (Visualize)
        self.btn_img_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(image=self.btn_img_3, borderwidth=0, highlightthickness=0, activebackground="#51908D",
        command=lambda: print("visualize button clicked"), relief="flat")
        self.button_3.place(x=892.8018, y=560.214, width=160.6031, height=41.0992)

        # Button 4 (Search)
        self.btn_img_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = Button(image=self.btn_img_4, borderwidth=0, highlightthickness=0, activebackground="#51908D",
        command=lambda: print("search button clicked"), relief="flat")
        self.button_4.place(x=741.6836, y=560.214, width=134.679, height=41.0992)

        # Button 5 (Sales)
        self.btn_img_5 = PhotoImage(file=self.relative_to_assets("button_5.png"))
        self.button_5 = Button(image=self.btn_img_5, borderwidth=0, highlightthickness=0, activebackground="#51908D",
        command=lambda: print("sales button clicked"), relief="flat")
        self.button_5.place(x=25.292, y=345.2335, width=213.716, height=59.4358)

        # Button 6 (Users)
        self.btn_img_6 = PhotoImage(file=self.relative_to_assets("button_6.png"))
        self.button_6 = Button(image=self.btn_img_6, borderwidth=0, highlightthickness=0, activebackground="#51908D",
        command=lambda: print("users button clicked"), relief="flat")
        self.button_6.place(x=25.292, y=421.109, width=209.9222, height=58.8035)

        # Button 7 (Price)
        self.btn_img_7 = PhotoImage(file=self.relative_to_assets("button_7.png"))
        self.button_7 = Button(image=self.btn_img_7, borderwidth=0, highlightthickness=0, activebackground="#51908D",
        command=lambda: print("price button clicked"), relief="flat")
        self.button_7.place(x=25.292, y=268.7258, width=213.716, height=60.7004)

        # Button 8 (Edit)
        self.btn_img_8 = PhotoImage(file=self.relative_to_assets("button_8.png"))
        self.button_8 = Button(image=self.btn_img_8, borderwidth=0, highlightthickness=0, activebackground="#51908D",
        command=lambda: print("edit button clicked"), relief="flat")
        self.button_8.place(x=25.292, y=188.4242, width=213.716, height=64.4942)

        # Button 9 (Overview)
        self.btn_img_9 = PhotoImage(file=self.relative_to_assets("button_9.png"))
        self.button_9 = Button(image=self.btn_img_9, borderwidth=0, highlightthickness=0, activebackground="#51908D",
        command=lambda: print("overview button clicked"), relief="flat")
        self.button_9.place(x=25.292, y=112.5486, width=230.1556, height=60.0681)

        self.window.mainloop()

    def create_entry(self, img_name, x, y, width, height, img_x, img_y):
        entry_image = PhotoImage(file=self.relative_to_assets(img_name))
        self.canvas.create_image(img_x, img_y, image=entry_image)

        entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        entry.place(x=x, y=y, width=width, height=height)
        entry.image = entry_image

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

if __name__ == "__main__":
    GUI5()
