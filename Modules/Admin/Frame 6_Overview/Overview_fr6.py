from tkinter import *
from pathlib import Path

class Overview:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1092x650")
        self.window.title("Details")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)

        # Canvas setup
        self.canvas = Canvas(
            self.window, bg="#FFFFFF", height=650, width=1092,
            bd=0, highlightthickness=0, relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        # Asset path
        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Admin" / "Frame 6_Overview"

        icon_path = self.relative_to_assets("icon_banhrang.png")
        self.window.iconphoto(False, PhotoImage(file=icon_path))

        # Load background
        self.background_img = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(546.0, 325.0, image=self.background_img)

        # Entry
        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.canvas.create_image(606.68, 43.62, image=self.entry_image_1)
        self.entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=410.99, y=21.49, width=391.39, height=42.26)

        # Buttons
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_logout.png"))
        self.button_1 = Button(
            image=self.button_image_1, borderwidth=0, highlightthickness=0,
            activebackground="#55908B",
            command=lambda: print("button_logout clicked"), relief="flat"
        )
        self.button_1.place(x=7.0, y=586.0, width=117.0, height=51.0)

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_quit.png"))
        self.button_2 = Button(
            image=self.button_image_2, borderwidth=0, highlightthickness=0,
            activebackground="#55908B",
            command=lambda: print("button_quit clicked"), relief="flat"
        )
        self.button_2.place(x=138.0, y=586.0, width=117.0, height=51.0)

        self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_cleaning.png"))
        self.button_3 = Button(
            image=self.button_image_3, borderwidth=0, highlightthickness=0,
            activebackground="#346B4E",
            command=lambda: print("button_cleaning clicked"), relief="flat"
        )
        self.button_3.place(x=916.0, y=102.0, width=151.0, height=46.0)

        self.button_image_4 = PhotoImage(file=self.relative_to_assets("button_booking.png"))
        self.button_4 = Button(
            image=self.button_image_4, borderwidth=0, highlightthickness=0,
            activebackground="#346B4E",
            command=lambda: print("button_booked clicked"), relief="flat"
        )
        self.button_4.place(x=742.0, y=102.0, width=153.0, height=48.0)

        self.button_image_5 = PhotoImage(file=self.relative_to_assets("button_occupied.png"))
        self.button_5 = Button(
            image=self.button_image_5, borderwidth=0, highlightthickness=0,
            activebackground="#346B4E",
            command=lambda: print("button_occupied clicked"), relief="flat"
        )
        self.button_5.place(x=572.0, y=102.0, width=156.0, height=47.0)

        self.button_image_6 = PhotoImage(file=self.relative_to_assets("button_avai.png"))
        self.button_6 = Button(
            image=self.button_image_6, borderwidth=0, highlightthickness=0,
            activebackground="#346B4E",
            command=lambda: print("button_available clicked"), relief="flat"
        )
        self.button_6.place(x=405.0, y=102.0, width=154.0, height=46.0)

        self.button_image_7 = PhotoImage(file=self.relative_to_assets("button_all.png"))
        self.button_7 = Button(
            image=self.button_image_7, borderwidth=0, highlightthickness=0,
            activebackground="#346B4E",
            command=lambda: print("button_all clicked"), relief="flat"
        )
        self.button_7.place(x=284.0, y=99.0, width=109.0, height=49.0)

        self.button_image_8 = PhotoImage(file=self.relative_to_assets("button_sales.png"))
        self.button_8 = Button(
            image=self.button_image_8, borderwidth=0, highlightthickness=0,
            activebackground="#55908B",
            command=lambda: print("button_sales clicked"), relief="flat"
        )
        self.button_8.place(x=25.29, y=345.23, width=213.71, height=59.43)

        self.button_image_9 = PhotoImage(file=self.relative_to_assets("button_users.png"))
        self.button_9 = Button(
            image=self.button_image_9, borderwidth=0, highlightthickness=0,
            activebackground="#55908B",
            command=lambda: print("button_users clicked"), relief="flat"
        )
        self.button_9.place(x=25.29, y=421.10, width=209.92, height=58.80)

        self.button_image_10 = PhotoImage(file=self.relative_to_assets("button_price.png"))
        self.button_10 = Button(
            image=self.button_image_10, borderwidth=0, highlightthickness=0,
            activebackground="#55908B",
            command=lambda: print("button_price clicked"), relief="flat"
        )
        self.button_10.place(x=25.29, y=268.72, width=213.71, height=60.70)

        self.button_image_11 = PhotoImage(file=self.relative_to_assets("button_edit.png"))
        self.button_11 = Button(
            image=self.button_image_11, borderwidth=0, highlightthickness=0,
            activebackground="#55908B",
            command=lambda: print("button_edit clicked"), relief="flat"
        )
        self.button_11.place(x=25.29, y=188.42, width=213.71, height=64.49)

        self.button_image_12 = PhotoImage(file=self.relative_to_assets("button_overview.png"))
        self.button_12 = Button(
            image=self.button_image_12, borderwidth=0, highlightthickness=0,
            activebackground="#55908B",
            command=lambda: print("button_overview clicked"), relief="flat"
        )
        self.button_12.place(x=25.29, y=116.97, width=230.15, height=60.06)

        self.button_image_13 = PhotoImage(file=self.relative_to_assets("button_find.png"))
        self.button_13 = Button(
            image=self.button_image_13, borderwidth=0, highlightthickness=0,
            activebackground="#55908B",
            command=lambda: print("button_find clicked"), relief="flat"
        )
        self.button_13.place(x=780.88, y=31.08, width=24.97, height=25.29)

        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

if __name__ == "__main__":
    Overview()
