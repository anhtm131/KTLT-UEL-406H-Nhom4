from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

class Report_Information:
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
        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Admin" / "Frame 9_Report Information"

        icon_path = self.relative_to_assets("icon_report.png")
        self.window.iconphoto(False, PhotoImage(file=icon_path))

        # Load background
        self.background_img = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(546.0, 325.0, image=self.background_img)

        # Entries
        self.entries = []
        self.entry_img_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))

        # Entry 1
        self.canvas.create_image(369.8926 + 148.5895 / 2, 565.9047 + 30.2471 / 2, image=self.entry_img_1)
        self.entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=369.8926, y=565.9047, width=148.5895, height=30.2471)
        self.entries.append(self.entry_1)

        # Entry 2
        self.canvas.create_image(574.125 + 148.5895 / 2, 565.9047 + 30.2471 / 2, image=self.entry_img_1)
        self.entry_2 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=574.125, y=565.9047, width=148.5895, height=30.2471)
        self.entries.append(self.entry_2)

        # Button 1 (Logout)
        self.btn_logout = PhotoImage(file=self.relative_to_assets("button_logout.png"))
        self.button_logout = Button(image=self.btn_logout, borderwidth=0, highlightthickness=0, activebackground="#51908D",
        command=lambda: print("logout button clicked"), relief="flat")
        self.button_logout.place(x=6.0, y=584.0, width=119.5039, height=55.0097)

        # Button 2 (Quit)
        self.btn_quit = PhotoImage(file=self.relative_to_assets("button_quit.png"))
        self.button_quit = Button(image=self.btn_quit, borderwidth=0, highlightthickness=0, activebackground="#51908D",
        command=lambda: print("quit button clicked"), relief="flat")
        self.button_quit.place(x=138.0, y=585.0, width=118.8716, height=53.1128)

        # Button 3 (Visualize)
        self.btn_visualize = PhotoImage(file=self.relative_to_assets("button_visualize.png"))
        self.button_visualize = Button(image=self.btn_visualize, borderwidth=0, highlightthickness=0, activebackground="#51908D",
        command=lambda: print("visualize button clicked"), relief="flat")
        self.button_visualize.place(x=892.8018, y=560.214, width=160.6031, height=41.0992)

        # Button 4 (Search)
        self.btn_search = PhotoImage(file=self.relative_to_assets("button_search.png"))
        self.button_search = Button(image=self.btn_search, borderwidth=0, highlightthickness=0, activebackground="#51908D",
        command=lambda: print("search button clicked"), relief="flat")
        self.button_search.place(x=741.6836, y=560.214, width=134.679, height=41.0992)

        # Button 5 (Sales)
        self.btn_sales = PhotoImage(file=self.relative_to_assets("button_sales.png"))
        self.button_sales = Button(image=self.btn_sales, borderwidth=0, highlightthickness=0, activebackground="#51908D",
        command=lambda: print("sales button clicked"), relief="flat")
        self.button_sales.place(x=25.292, y=345.2335, width=213.716, height=59.4358)

        # Button 6 (Users)
        self.btn_users = PhotoImage(file=self.relative_to_assets("button_users.png"))
        self.button_users = Button(image=self.btn_users, borderwidth=0, highlightthickness=0, activebackground="#51908D",
        command=lambda: print("users button clicked"), relief="flat")
        self.button_users.place(x=25.292, y=421.109, width=209.9222, height=58.8035)

        # Button 7 (Price)
        self.btn_price = PhotoImage(file=self.relative_to_assets("button_price.png"))
        self.button_price = Button(image=self.btn_price, borderwidth=0, highlightthickness=0, activebackground="#51908D",
        command=lambda: print("price button clicked"), relief="flat")
        self.button_price.place(x=25.292, y=268.7258, width=213.716, height=60.7004)

        # Button 8 (Edit)
        self.btn_edit = PhotoImage(file=self.relative_to_assets("button_edit.png"))
        self.button_edit = Button(image=self.btn_edit, borderwidth=0, highlightthickness=0, activebackground="#51908D",
        command=lambda: print("edit button clicked"), relief="flat")
        self.button_edit.place(x=25.292, y=188.4242, width=213.716, height=64.4942)

        # Button 9 (Overview)
        self.btn_overview = PhotoImage(file=self.relative_to_assets("button_overview.png"))
        self.button_overview = Button(image=self.btn_overview, borderwidth=0, highlightthickness=0, activebackground="#51908D",
        command=lambda: print("overview button clicked"), relief="flat")
        self.button_overview.place(x=25.292, y=112.5486, width=230.1556, height=60.0681)

        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

if __name__ == "__main__":
    Report_Information()
