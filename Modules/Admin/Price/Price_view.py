from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

class Price_view:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1092x650")
        self.window.title("Room Type & Price")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=650, width=1092, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Admin" / "Price"
        self.assets_WE_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Admin" / "Window_elements"

        self.window.iconphoto(False, PhotoImage(file=self.relative_to_assets("Price.png", "Price")))
        self.background_img = PhotoImage(file=self.relative_to_assets("background_price.png", "Price"))
        self.canvas.create_image(546.0, 325.0, image=self.background_img)

        self.entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry.place(x=490.0293, y=512.6303, width=512, height=39.0992)

        self.button_img_logout = PhotoImage(file=self.relative_to_assets("logout.png", "Window_element"))
        self.logout = Button(image=self.button_img_logout, borderwidth=0, highlightthickness=0, activebackground="#55908B", command=lambda: print("button_logout clicked"), relief="flat")
        self.logout.place(x=7.0, y=586.0, width=117.0, height=51.0)

        self.button_img_quit = PhotoImage(file=self.relative_to_assets("quit.png", "Window_element"))
        self.button_quit = Button(image=self.button_img_quit, borderwidth=0, highlightthickness=0, activebackground="#55908B", command=lambda: print("button_quit clicked"), relief="flat")
        self.button_quit.place(x=138.0, y=586.0, width=117.0, height=51.0)

        self.button_img_sales = PhotoImage(file=self.relative_to_assets("sales.png", "Window_element"))
        self.button_sales = Button(image=self.button_img_sales, borderwidth=0, highlightthickness=0, activebackground="#51908D", command=lambda: print("button_sales clicked"), relief="flat")
        self.button_sales.place(x=25.292, y=345.2335, width=213.716, height=59.4358)

        self.button_img_users = PhotoImage(file=self.relative_to_assets("user.png", "Window_element"))
        self.button_users = Button(image=self.button_img_users, borderwidth=0, highlightthickness=0, activebackground="#51908D", command=lambda: print("button_users clicked"), relief="flat")
        self.button_users.place(x=25.292, y=421.109, width=209.9222, height=58.8035)

        self.button_img_price = PhotoImage(file=self.relative_to_assets("price.png", "Window_element"))
        self.button_price = Button(image=self.button_img_price, borderwidth=0, highlightthickness=0, activebackground="#51908D", command=lambda: print("button_price clicked"), relief="flat")
        self.button_price.place(x=25.292, y=268.7258, width=213.716, height=60.7004)

        self.button_img_edit = PhotoImage(file=self.relative_to_assets("edit.png", "Window_element"))
        self.button_edit = Button(image=self.button_img_edit, borderwidth=0, highlightthickness=0, activebackground="#51908D", command=lambda: print("button_edit clicked"), relief="flat")
        self.button_edit.place(x=25.292, y=188.4242, width=213.716, height=64.4942)

        self.button_img_overview = PhotoImage(file=self.relative_to_assets("overview.png", "Window_element"))
        self.button_overview = Button(image=self.button_img_overview, borderwidth=0, highlightthickness=0, activebackground="#51908D", command=lambda: print("button_overview clicked"), relief="flat")
        self.button_overview.place(x=25.292, y=116.9747, width=230.1556, height=60.0681)

        self.button_img_update = PhotoImage(file=self.relative_to_assets("button_update.png", "Price"))
        self.button_update = Button(image=self.button_img_update, borderwidth=0, highlightthickness=0, activebackground="#51908D", command=lambda: print("button_update clicked"), relief="flat")
        self.button_update.place(x=622.1787, y=563.3755, width=92.1864, height=46.4923)

        self.window.mainloop()

    def relative_to_assets(self, path: str, assets_type: str = "Price") -> Path:
        if assets_type == "Price":
            return self.assets_path / Path(path)
        elif assets_type == "Window_element":
            return self.assets_WE_path / Path(path)

if __name__ == "__main__":
    Price_view()