from tkinter import *
from pathlib import Path


class Users_view:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1092x650")
        self.window.title("Update Login Information")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)
        self.canvas = Canvas(self.window, bg="#FFFFFF", height=650, width=1092, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        OUTPUT_PATH = Path(__file__).parent
        self.assets_frame_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Admin" / "Users"
        self.assets_WE_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Admin" / "Window_elements"

        self.window.iconphoto(False, PhotoImage(file=self.relative_to_assets("login_update.png", "Frame")))
        self.background_img = PhotoImage(file=self.relative_to_assets("background_users.png", "Frame"))
        self.canvas.create_image(546.0, 325.0, image=self.background_img)


        self.entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=428.1064, y=161.4692, width=164.9817, height=34.5297)


        self.entry_2 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=637.9863, y=130.2529, width=314.251, height=39.0992)

        self.entry_3 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_3.place(x=428.1064, y=227.8868, width=164.9817, height=34.5297)


        self.entry_4 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_4.place(x=428.1064, y=294.3044, width=164.9817, height=34.5297)

        self.button_img_logout = PhotoImage(file=self.relative_to_assets("logout.png", "Window_element"))
        self.logout = Button(image=self.button_img_logout, borderwidth=0, highlightthickness=0,activebackground="#55908B", command=lambda: print("button_logout clicked"), relief="flat")
        self.logout.place(x=7.0, y=586.0, width=117.0, height=51.0)

        self.button_img_quit = PhotoImage(file=self.relative_to_assets("quit.png", "Window_element"))
        self.button_quit = Button(image=self.button_img_quit, borderwidth=0, highlightthickness=0,activebackground="#55908B", command=lambda: print("button_quit clicked"),relief="flat")
        self.button_quit.place(x=138.0, y=586.0, width=117.0, height=51.0)

        self.button_img_delete = PhotoImage(file=self.relative_to_assets("button_delete.png", "Frame"))
        self.delete = Button(image=self.button_img_delete, borderwidth=0, highlightthickness=0, activebackground="#51908D", command=lambda: print("delete button clicked"), relief="flat")
        self.delete.place(x=514.0566, y=359.7763, width=88.5214, height=47.4222)

        self.button_img_update = PhotoImage(file=self.relative_to_assets("button_update.png", "Frame"))
        self.update = Button(image=self.button_img_update, borderwidth=0, highlightthickness=0, activebackground="#51908D", command=lambda: print("update button clicked"), relief="flat")
        self.update.place(x=302.9893, y=361.3862, width=85.8724, height=46.4923)

        self.button_img_create = PhotoImage(file=self.relative_to_assets("button_create.png", "Frame"))
        self.create = Button(image=self.button_img_create, borderwidth=0, highlightthickness=0, activebackground="#51908D", command=lambda: print("create button clicked"), relief="flat")
        self.create.place(x=408.4795, y=360.7221, width=85.8641, height=46.4923)

        self.button_img_find = PhotoImage(file=self.relative_to_assets("button_find.png", "Frame"))
        self.find = Button(image=self.button_img_find, borderwidth=0, highlightthickness=0, activebackground="#51908D", command=lambda: print("find button clicked"), relief="flat")
        self.find.place(x=958.5605, y=130.2529, width=56.9066, height=41.0992)

        self.button_img_reload = PhotoImage(file=self.relative_to_assets("button_reload.png", "Frame"))
        self.reload = Button(image=self.button_img_reload, borderwidth=0, highlightthickness=0, activebackground="#51908D", command=lambda: print("reload button clicked"), relief="flat")
        self.reload.place(x=1021.1572, y=130.2529, width=56.9066, height=41.0992)

        self.button_img_sales = PhotoImage(file=self.relative_to_assets("sales.png", "Window_element"))
        self.sales = Button(image=self.button_img_sales, borderwidth=0, highlightthickness=0, activebackground="#51908D", command=lambda: print("sales button clicked"), relief="flat")
        self.sales.place(x=25.292, y=345.2335, width=213.716, height=59.4358)

        self.button_img_users = PhotoImage(file=self.relative_to_assets("user.png", "Window_element"))
        self.users = Button(image=self.button_img_users, borderwidth=0, highlightthickness=0, activebackground="#51908D", command=lambda: print("users button clicked"), relief="flat")
        self.users.place(x=25.292, y=421.109, width=209.9222, height=58.8035)

        self.button_img_price = PhotoImage(file=self.relative_to_assets("price.png", "Window_element"))
        self.price = Button(image=self.button_img_price, borderwidth=0, highlightthickness=0, activebackground="#51908D", command=lambda: print("price button clicked"), relief="flat")
        self.price.place(x=25.292, y=268.7257, width=213.716, height=60.7004)

        self.button_img_edit = PhotoImage(file=self.relative_to_assets("edit.png", "Window_element"))
        self.edit = Button(image=self.button_img_edit, borderwidth=0, highlightthickness=0, activebackground="#51908D", command=lambda: print("edit button clicked"), relief="flat")
        self.edit.place(x=25.292, y=188.4241, width=213.716, height=64.4942)

        self.button_img_overview = PhotoImage(file=self.relative_to_assets("overview.png", "Window_element"))
        self.overview = Button(image=self.button_img_overview, borderwidth=0, highlightthickness=0, activebackground="#51908D", command=lambda: print("overview button clicked"), relief="flat")
        self.overview.place(x=25.292, y=116.9747, width=230.1556, height=60.0681)

        #self.window.mainloop()

    def relative_to_assets(self, path: str, assets_type: str = "Frame") -> Path:
        if assets_type == "Frame":
            return self.assets_frame_path / Path(path)
        elif assets_type == "Window_element":
            return self.assets_WE_path / Path(path)


if __name__ == "__main__":
    Users_view()