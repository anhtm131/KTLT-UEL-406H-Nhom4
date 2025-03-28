from tkinter import *
from pathlib import Path

import Modules.Main_process as Main_process



class Overview_view:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1095x650")
        self.window.title("Home")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=650, width=1095, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Users" / "Overview"

        self.window.iconphoto(False, PhotoImage(file=self.relative_to_assets("icon_home.png")))

        self.background_img = PhotoImage(file=self.relative_to_assets("background_overview.png"))
        self.canvas.create_image(548.0, 325.0, image=self.background_img)

        self.entry_img = PhotoImage(file=self.relative_to_assets("entry.png"))
        self.canvas.create_image(606.7, 43.6, image=self.entry_img)
        self.entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0, font=("Arial", 12))
        self.entry.place(x=410.992, y=22, width=391.391, height=42.261)

        # Buttons
        self.cleaning_btn_img = PhotoImage(file=self.relative_to_assets("button_cleaning.png"))
        self.cleaning_btn = Button(image=self.cleaning_btn_img, borderwidth=0, highlightthickness=0, activebackground="#679487", bg="#679487", command=lambda: print("Cleaning button clicked"), relief="flat")
        self.cleaning_btn.place(x=834.0, y=104.0, width=184.0, height=56.0)

        self.book_btn_img = PhotoImage(file=self.relative_to_assets("button_booked.png"))
        self.book_btn = Button(image=self.book_btn_img, borderwidth=0, highlightthickness=0, activebackground="#679487", bg="#679487", command=lambda: print("Book button clicked"), relief="flat")
        self.book_btn.place(x=632.9, y=103.0, width=174.1, height=57.0)

        self.available_btn_img = PhotoImage(file=self.relative_to_assets("button_avai.png"))
        self.available_btn = Button(image=self.available_btn_img, borderwidth=0, highlightthickness=0, activebackground="#679487", bg="#679487", command=lambda: print("Available button clicked"), relief="flat")
        self.available_btn.place(x=214.9, y=103.0, width=174.0, height=54.0)

        self.all_btn_img = PhotoImage(file=self.relative_to_assets("button_all.png"))
        self.all_btn = Button(image=self.all_btn_img, borderwidth=0, highlightthickness=0, activebackground="#679487", bg="#679487", command=lambda: print("All button clicked"), relief="flat")
        self.all_btn.place(x=70.8, y=104.0, width=110.7, height=53.0)

        self.occupied_btn_img = PhotoImage(file=self.relative_to_assets("button_occupied.png"))
        self.occupied_btn = Button(image=self.occupied_btn_img, borderwidth=0, highlightthickness=0, activebackground="#679487", bg="#679487", command=lambda: print("Occupied button clicked"), relief="flat")
        self.occupied_btn.place(x=422.0, y=103.0, width=174.3, height=55.0)

        self.logout_btn_img = PhotoImage(file=self.relative_to_assets("button_logout.png"))
        self.logout_btn = Button(image=self.logout_btn_img, borderwidth=0, highlightthickness=0, activebackground="#679487", bg="#679487", command=lambda: Main_process.Main_process.log_out_button(self), relief="flat")
        self.logout_btn.place(x=39.0, y=573.0, width=113.0, height=52.0)

        self.quit_btn_img = PhotoImage(file=self.relative_to_assets("button_quit.png"))
        self.quit_btn = Button(image=self.quit_btn_img, borderwidth=0, highlightthickness=0, activebackground="#679487", bg="#679487", command=lambda: Main_process.Main_process.quit_button(self), relief="flat")
        self.quit_btn.place(x=168.0, y=573.0, width=118.0, height=52.0)

        self.booking_btn_img = PhotoImage(file=self.relative_to_assets("button_booking.png"))
        self.booking_btn = Button(image=self.booking_btn_img, borderwidth=0, highlightthickness=0, activebackground="#679487", bg="#679487", command=lambda: Main_process.Main_process.Select_Room_button(self), relief="flat")
        self.booking_btn.place(x=903.0, y=569.0, width=156.0, height=55.0)

        self.find_btn_img = PhotoImage(file=self.relative_to_assets("button_find.png"))
        self.find_btn = Button(image=self.find_btn_img, borderwidth=0, highlightthickness=0, activebackground="#D9D9D9", bg="#D9D9D9", command=lambda: print("Find button clicked"), relief="flat")
        self.find_btn.place(x=785.0, y=31.0, width=25.0, height=25.3)

        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

if __name__ == "__main__":
    app = Overview_view()
    app.window.mainloop()