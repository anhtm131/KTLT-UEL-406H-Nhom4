from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

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


        self.entry_roomtype = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_roomtype.place(x=451.459, y=239.64, width=170.7198, height=35.9377)


        self.entry_price = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_price.place(x=451.459, y=319.9417, width=170.7198, height=35.9377)

        self.entry_status = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_status.place(x=451.459, y=400.2433, width=170.7198, height=35.9377)

        self.button_img_logout = PhotoImage(file=self.relative_to_assets("logout.png", "Window_element"))
        self.logout = Button(image=self.button_img_logout, borderwidth=0, highlightthickness=0,activebackground="#55908B", command=lambda: print("button_logout clicked"), relief="flat")
        self.logout.place(x=7.0, y=586.0, width=117.0, height=51.0)

        self.button_img_quit = PhotoImage(file=self.relative_to_assets("quit.png", "Window_element"))
        self.button_quit = Button(image=self.button_img_quit, borderwidth=0, highlightthickness=0,activebackground="#55908B", command=lambda: print("button_quit clicked"),relief="flat")
        self.button_quit.place(x=138.0, y=586.0, width=117.0, height=51.0)

        self.btn_find = PhotoImage(file=self.relative_to_assets("button_find.png", "Frame"))
        self.button_find = Button(image=self.btn_find, borderwidth=0, highlightthickness=0, activebackground="#6C9587", command=lambda: print("Find clicked"), relief="flat")
        self.button_find.place(x=966.1484, y=122.033, width=56.9066, height=41.0992)

        self.btn_reset = PhotoImage(file=self.relative_to_assets("button_reset.png", "Frame"))
        self.button_reset = Button(image=self.btn_reset, borderwidth=0, highlightthickness=0, activebackground="#6C9587", command=lambda: print("Reset clicked"), relief="flat")
        self.button_reset.place(x=1028.7451, y=122.033, width=56.9066, height=41.0992)

        self.btn_update = PhotoImage(file=self.relative_to_assets("button_update.png", "Frame"))
        self.button_update = Button(image=self.btn_update, borderwidth=0, highlightthickness=0, activebackground="#6C9587", command=lambda: print("Update clicked"), relief="flat")
        self.button_update.place(x=308.5605, y=474.6403, width=88.5214, height=47.4222)

        self.btn_delete = PhotoImage(file=self.relative_to_assets("button_delete.png", "Frame"))
        self.button_delete = Button(image=self.btn_delete, borderwidth=0, highlightthickness=0, activebackground="#6C9587", command=lambda: print("Delete clicked"), relief="flat")
        self.button_delete.place(x=529.2314, y=474.6403, width=88.5214, height=47.4222)

        self.btn_create = PhotoImage(file=self.relative_to_assets("button_create.png", "Frame"))
        self.button_create = Button(image=self.btn_create, borderwidth=0, highlightthickness=0, activebackground="#6C9587", command=lambda: print("Create clicked"), relief="flat")
        self.button_create.place(x=419.2119, y=474.6403, width=88.5214, height=47.4222)

        self.btn_sales = PhotoImage(file=self.relative_to_assets("sales.png", "Window_element"))
        self.button_sales = Button(image=self.btn_sales, borderwidth=0, highlightthickness=0, activebackground="#6C9587", command=lambda: print("Sales clicked"), relief="flat")
        self.button_sales.place(x=25.2915, y=345.2334, width=213.7159, height=59.4358)

        self.btn_users = PhotoImage(file=self.relative_to_assets("user.png", "Window_element"))
        self.button_users = Button(image=self.btn_users, borderwidth=0, highlightthickness=0, activebackground="#6C9587", command=lambda: print("Users clicked"), relief="flat")
        self.button_users.place(x=25.2915, y=421.1089, width=209.9222, height=58.8035)

        self.btn_price = PhotoImage(file=self.relative_to_assets("price.png", "Window_element"))
        self.button_price = Button(image=self.btn_price, borderwidth=0, highlightthickness=0, activebackground="#6C9587", command=lambda: print("Price clicked"), relief="flat")
        self.button_price.place(x=25.2915, y=268.7256, width=213.7159, height=60.7004)

        self.btn_edit = PhotoImage(file=self.relative_to_assets("edit.png", "Window_element"))
        self.button_edit = Button(image=self.btn_edit, borderwidth=0, highlightthickness=0, activebackground="#6C9587", command=lambda: print("Edit clicked"), relief="flat")
        self.button_edit.place(x=25.2915, y=188.4241, width=213.7159, height=64.4942)

        self.btn_overview = PhotoImage(file=self.relative_to_assets("overview.png", "Window_element"))
        self.button_overview = Button(image=self.btn_overview, borderwidth=0, highlightthickness=0, activebackground="#6C9587", command=lambda: print("Overview clicked"), relief="flat")
        self.button_overview.place(x=25.2915, y=116.9747, width=230.1556, height=60.0681)

        self.window.mainloop()

    def relative_to_assets(self, path: str, assets_type: str = "Frame") -> Path:
        if assets_type == "Frame":
            return self.assets_path / Path(path)
        elif assets_type == "Window_element":
            return self.assets_WE_path / Path(path)

if __name__ == "__main__":
    Rooms_view()