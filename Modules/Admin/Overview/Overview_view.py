from tkinter import *
from pathlib import Path
class Overview_view:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1092x650")
        self.window.title("Details")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)
        self.canvas = Canvas(self.window, bg="#FFFFFF", height=650, width=1092, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        OUTPUT_PATH = Path(__file__).parent
        self.assets_frame_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Admin" / "Overview"
        self.assets_WE_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Admin" / "Window_elements"

        self.window.iconphoto(False, PhotoImage(file=self.relative_to_assets("icon_banhrang.png", "Frame")))
        self.background_img = PhotoImage(file=self.relative_to_assets("background_overview.png", "Frame"))
        self.canvas.create_image(546.0, 325.0, image=self.background_img)

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry.png", "Frame"))
        self.canvas.create_image(606.68, 43.62, image=self.entry_image_1)
        self.entry_find = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_find.place(x=410.99, y=22, width=391.39, height=42.26)

        self.button_img_logout = PhotoImage(file=self.relative_to_assets("logout.png", "Window_element"))
        self.logout = Button(image=self.button_img_logout, borderwidth=0, highlightthickness=0, activebackground="#55908B", command=lambda: print("button_logout clicked"), relief="flat")
        self.logout.place(x=7.0, y=586.0, width=117.0, height=51.0)

        self.button_img_quit = PhotoImage(file=self.relative_to_assets("quit.png", "Window_element"))
        self.button_quit = Button(image=self.button_img_quit, borderwidth=0, highlightthickness=0, activebackground="#55908B", command=lambda: print("button_quit clicked"), relief="flat")
        self.button_quit.place(x=138.0, y=586.0, width=117.0, height=51.0)

        self.button_img_cleaning = PhotoImage(file=self.relative_to_assets("button_cleaning.png", "Frame"))
        self.button_cleaning = Button(image=self.button_img_cleaning, borderwidth=0, highlightthickness=0, activebackground="#346B4E", command=lambda: print("button_cleaning clicked"), relief="flat")
        self.button_cleaning.place(x=916.0, y=102.0, width=151.0, height=46.0)

        self.button_img_booking = PhotoImage(file=self.relative_to_assets("button_booked.png", "Frame"))
        self.button_booking = Button(image=self.button_img_booking, borderwidth=0, highlightthickness=0, activebackground="#346B4E", command=lambda: print("button_booked clicked"), relief="flat")
        self.button_booking.place(x=742.0, y=102.0, width=153.0, height=48.0)

        self.button_img_occupied = PhotoImage(file=self.relative_to_assets("button_occupied.png", "Frame"))
        self.button_occupied = Button(image=self.button_img_occupied, borderwidth=0, highlightthickness=0, activebackground="#346B4E", command=lambda: print("button_occupied clicked"), relief="flat")
        self.button_occupied.place(x=572.0, y=102.0, width=156.0, height=47.0)

        self.button_img_avai = PhotoImage(file=self.relative_to_assets("button_avai.png", "Frame"))
        self.button_avai = Button(image=self.button_img_avai, borderwidth=0, highlightthickness=0, activebackground="#346B4E", command=lambda: print("button_available clicked"), relief="flat")
        self.button_avai.place(x=405.0, y=102.0, width=154.0, height=46.0)

        self.button_img_all = PhotoImage(file=self.relative_to_assets("button_all.png", "Frame"))
        self.button_all = Button(image=self.button_img_all, borderwidth=0, highlightthickness=0, activebackground="#346B4E", command=lambda: print("button_all clicked"), relief="flat")
        self.button_all.place(x=284.0, y=99.0, width=109.0, height=49.0)

        self.button_img_sales = PhotoImage(file=self.relative_to_assets("sales.png", "Window_element"))
        self.button_sales = Button(image=self.button_img_sales, borderwidth=0, highlightthickness=0, activebackground="#55908B", command=lambda: print("button_sales clicked"), relief="flat")
        self.button_sales.place(x=25.29, y=345.23, width=213.71, height=59.43)

        self.button_img_users = PhotoImage(file=self.relative_to_assets("user.png", "Window_element"))
        self.button_users = Button(image=self.button_img_users, borderwidth=0, highlightthickness=0, activebackground="#55908B", command=lambda: print("button_users clicked"), relief="flat")
        self.button_users.place(x=25.29, y=421.10, width=209.92, height=58.80)

        self.button_img_price = PhotoImage(file=self.relative_to_assets("price.png", "Window_element"))
        self.button_price = Button(image=self.button_img_price, borderwidth=0, highlightthickness=0, activebackground="#55908B", command=lambda: print("button_price clicked"), relief="flat")
        self.button_price.place(x=25.29, y=268.72, width=213.71, height=60.70)

        self.button_img_edit = PhotoImage(file=self.relative_to_assets("edit.png", "Window_element"))
        self.button_edit = Button(image=self.button_img_edit, borderwidth=0, highlightthickness=0, activebackground="#55908B", command=lambda: print("button_edit clicked"), relief="flat")
        self.button_edit.place(x=25.29, y=188.42, width=213.71, height=64.49)

        self.button_img_overview = PhotoImage(file=self.relative_to_assets("button_overview.png", "Frame"))
        self.button_overview = Button(image=self.button_img_overview, borderwidth=0, highlightthickness=0, activebackground="#55908B", command=lambda: print("button_overview clicked"), relief="flat")
        self.button_overview.place(x=25.29, y=116.97, width=230.15, height=60.06)

        self.button_img_find = PhotoImage(file=self.relative_to_assets("button_find.png", "Frame"))
        self.button_find = Button(image=self.button_img_find, borderwidth=0, highlightthickness=0, activebackground="#55908B", command=lambda: print("button_find clicked"), relief="flat")
        self.button_find.place(x=780.88, y=31.08, width=24.97, height=25.29)

        self.window.mainloop()

    def relative_to_assets(self, path: str, assets_type = str("Frame")):
        if assets_type == "Frame":
            return self.assets_frame_path / Path(path)
        elif assets_type == "Window_element":
            return self.assets_WE_path / Path(path)

if __name__ == "__main__":
    Overview_view()