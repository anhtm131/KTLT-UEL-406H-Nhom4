from pathlib import Path
from tkinter import *
from tkinter import messagebox
from Modules.Admin.Overview.Overview_extend import Overview_extend
from Modules.Admin.Price.Price_extend import Price_extend
from Modules.Admin.Sales.Sales_extend import Sales_extend
from Modules.Admin.Users.Users_extend import Users_extend
from Modules.Login import Login_view

class Rooms_view:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1092x650")
        self.window.configure(bg="#FFFFFF")
        self.window.title("Display Room Information")
        self.window.resizable(False, False)
        self.canvas = Canvas(self.window, bg="#FFFFFF", height=650, width=1092, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Admin" / "Rooms"
        self.assets_WE_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Admin" / "Window_elements"

        self.window.iconphoto(False, PhotoImage(file=self.relative_to_assets("ic_infor.png", "Frame")))
        self.background_img = PhotoImage(file=self.relative_to_assets("background_rooms.png", "Frame"))
        self.canvas.create_image(546.0, 325.0, image=self.background_img)

        self.entry_find = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_find.place(x=677.1885, y=122.033, width=282.0039, height=39.0992)

        self.entry_roomid = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_roomid.place(x=451.459, y=159.9709, width=170.7198, height=35.9377)

        self.entry_price = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_price.place(x=451.459, y=319.9417, width=170.7198, height=35.9377)

        self.entry_status = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_status.place(x=451.459, y=400.2433, width=170.7198, height=35.9377)

        self.button_img_logout = PhotoImage(file=self.relative_to_assets("logout.png", "Window_element"))
        self.logout = Button(image=self.button_img_logout, borderwidth=0, highlightthickness=0, activebackground="#55908B", command=lambda: self.log_out_button(self), relief="flat")
        self.logout.place(x=7.0, y=586.0, width=117.0, height=51.0)

        self.button_img_quit = PhotoImage(file=self.relative_to_assets("quit.png", "Window_element"))
        self.button_quit = Button(image=self.button_img_quit, borderwidth=0, highlightthickness=0, activebackground="#55908B", command=lambda: self.quit_button(self), relief="flat")
        self.button_quit.place(x=138.0, y=586.0, width=117.0, height=51.0)

        self.btn_price = PhotoImage(file=self.relative_to_assets("price.png", "Window_element"))
        self.button_price = Button(image=self.btn_price, borderwidth=0, highlightthickness=0, activebackground="#6C9587", command=lambda: self.price_button(self), relief="flat")
        self.button_price.place(x=25.2915, y=268.7256, width=213.7159, height=60.7004)

        self.btn_edit = PhotoImage(file=self.relative_to_assets("edit.png", "Window_element"))
        self.button_edit = Button(image=self.btn_edit, borderwidth=0, highlightthickness=0, activebackground="#6C9587", command=lambda: self.edit_button(self), relief="flat")
        self.button_edit.place(x=25.2915, y=188.4241, width=213.7159, height=64.4942)

        self.btn_overview = PhotoImage(file=self.relative_to_assets("overview.png", "Window_element"))
        self.button_overview = Button(image=self.btn_overview, borderwidth=0, highlightthickness=0, activebackground="#6C9587", command=lambda: self.overview_button(self), relief="flat")
        self.button_overview.place(x=25.2915, y=116.9747, width=230.1556, height=60.0681)

    def relative_to_assets(self, path: str, assets_type: str = "Frame") -> Path:
        if assets_type == "Frame":
            return self.assets_path / Path(path)
        elif assets_type == "Window_element":
            return self.assets_WE_path / Path(path)

    @staticmethod
    def overview_button(obj):
        obj.window.destroy()
        Overview_extend()

    @staticmethod
    def price_button(obj):
        obj.window.destroy()
        Price_extend()

    @staticmethod
    def sales_button(obj):
        obj.window.destroy()
        Sales_extend()

    @staticmethod
    def users_button(obj):
        obj.window.destroy()
        Users_extend()

    @staticmethod
    def log_out_button(obj):
        if messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn thoát không?"):
            obj.window.destroy()
            Login_view.Login_view()

    @staticmethod
    def quit_button(obj):
        if messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn thoát không?"):
            obj.window.destroy()

    @staticmethod
    def edit_button(obj):
        obj.window.destroy()
        Rooms_view()
