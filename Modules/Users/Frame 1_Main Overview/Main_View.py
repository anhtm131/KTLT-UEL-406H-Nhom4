from tkinter import *
from pathlib import Path

class Main_View:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1095x650")
        self.window.title("Home")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)

        # Canvas setup
        self.canvas = Canvas(
            self.window, bg="#FFFFFF", height=650, width=1095,
            bd=0, highlightthickness=0, relief="ridge")

        self.canvas.place(x=0, y=0)

        # Asset path
        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Users" / "Frame 1_Main Overview"

        # Set window icon
        icon_path = self.relative_to_assets("icon (2).png")
        self.window.iconphoto(False, PhotoImage(file=icon_path))

        # Load images
        self.background_img = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.entry_image = PhotoImage(file=self.relative_to_assets("entry_1.png"))

        # Background
        self.canvas.create_image(548.0, 325.0, image=self.background_img)

        # Entries
        entry_positions = [(606.7, 43.6, 410.992, 21.498, 391.391, 42.261)]

        for i, (x_img, y_img, x_entry, y_entry, width, height) in enumerate(entry_positions, start=1):
            entry_image = PhotoImage(file=self.relative_to_assets(f"entry_{i}.png"))
            self.canvas.create_image(x_img, y_img, image=entry_image)

            entry = Entry(
                bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0, font=("Arial", 12))
            entry.place(x=x_entry, y=y_entry, width=width, height=height)

        # Buttons
        # Button Cleaning
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_cleaning.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#679487",
            bg="#679487",
            command=lambda: print("button_cleaning clicked"),
            relief="flat"
        )
        self.button_1.place(x=834.0, y=104.0, width=184.0, height=56.0)

        #Button book
        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_book.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#679487",
            bg="#679487",
            command=lambda: print("button_book clicked"),
            relief="flat"
        )
        self.button_2.place(x=632.9, y=103.0, width=174.1, height=57.0)

        #Button available
        self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_avai.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#679487",
            bg="#679487",
            command=lambda: print("button_available clicked"),
            relief="flat"
        )
        self.button_3.place(x=214.9, y=103.0, width=174.0, height=54.0)

        #Button all
        self.button_image_4 = PhotoImage(file=self.relative_to_assets("button_all.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#679487",
            bg="#679487",
            command=lambda: print("button_all clicked"),
            relief="flat"
        )
        self.button_4.place(x=70.8, y=104.0, width=110.7, height=53.0)

        #Button occupied
        self.button_image_5 = PhotoImage(file=self.relative_to_assets("button_occupied.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#679487",
            bg="#679487",
            command=lambda: print("button_occupied clicked"),
            relief="flat"
        )
        self.button_5.place(x=422.0, y=103.0, width=174.3, height=55.0)

        #Button logout
        self.button_image_6 = PhotoImage(file=self.relative_to_assets("button_logout.png"))
        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#679487",
            bg="#679487",
            command=lambda: print("button_logout clicked"),
            relief="flat"
        )
        self.button_6.place(x=39.0, y=573.0, width=113.0, height=52.0)

        #Button quit
        self.button_image_7 = PhotoImage(file=self.relative_to_assets("button_quit.png"))
        self.button_7 = Button(
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#679487",
            bg="#679487",
            command=lambda: print("button_quit clicked"),
            relief="flat"
        )
        self.button_7.place(x=168.0, y=573.0, width=118.0, height=52.0)

        #Button booking
        self.button_image_8 = PhotoImage(file=self.relative_to_assets("button_booking.png"))
        self.button_8 = Button(
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#679487",
            bg="#679487",
            command=lambda: print("button_booking clicked"),
            relief="flat"
        )
        self.button_8.place(x=903.0, y=569.0, width=156.0, height=55.0)

        #Button find
        self.button_image_9 = PhotoImage(file=self.relative_to_assets("button_find.png"))
        self.button_9 = Button(
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#D9D9D9",
            bg="#D9D9D9",
            command=lambda: print("button_timkiem clicked"),
            relief="flat"
        )
        self.button_9.place(x=785.0, y=31.0, width=24.97568130493164, height=25.29183006286621)

        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        asset_path = self.assets_path / Path(path)
        return asset_path

if __name__ == "__main__":
    Main_View()
