from tkinter import *
from pathlib import Path
from tkinter import ttk
from Modules.Admin.Users.Users_extend import Users_extend
import Modules.Main_process as Main_process
import tkinter as tk
from Api.Admin_Api import Admin_Api
class Users_view:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1092x650")
        self.window.title("Update Login Information")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)
        self.canvas = Canvas(self.window, bg="#FFFFFF", height=650, width=1092, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        self.admin_api = Admin_Api()
        OUTPUT_PATH = Path(__file__).parent
        self.assets_frame_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Admin" / "Users"
        self.assets_WE_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Admin" / "Window_elements"

        self.window.iconphoto(False, PhotoImage(file=self.relative_to_assets("login_update.png", "Frame")))
        self.background_img = PhotoImage(file=self.relative_to_assets("background_users.png", "Frame"))
        self.canvas.create_image(546.0, 325.0, image=self.background_img)


        self.entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=428.1064, y=161.4692, width=164.9817, height=34.5297)


        self.entry_2 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=637.9863, y=130.2529, width=314.251, height=39.0992) #find

        self.entry_3 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_3.place(x=428.1064, y=227.8868, width=164.9817, height=34.5297) #pass


        self.entry_4 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_4.place(x=428.1064, y=294.3044, width=164.9817, height=34.5297)  #role

        self.button_img_logout = PhotoImage(file=self.relative_to_assets("logout.png", "Window_element"))
        self.logout = Button(image=self.button_img_logout, borderwidth=0, highlightthickness=0, activebackground="#55908B", command=lambda: Main_process.Main_process.log_out_button(self), relief="flat")
        self.logout.place(x=7.0, y=586.0, width=117.0, height=51.0)

        self.button_img_quit = PhotoImage(file=self.relative_to_assets("quit.png", "Window_element"))
        self.button_quit = Button(image=self.button_img_quit, borderwidth=0, highlightthickness=0, activebackground="#55908B", command=lambda: Main_process.Main_process.quit_button(self), relief="flat")
        self.button_quit.place(x=138.0, y=586.0, width=117.0, height=51.0)

        self.button_img_delete = PhotoImage(file=self.relative_to_assets("button_delete.png", "Frame"))
        self.delete = Button(image=self.button_img_delete, borderwidth=0, highlightthickness=0, activebackground="#51908D", command=lambda: Users_extend.delete_user(self), relief="flat")
        self.delete.place(x=514.0566, y=359.7763, width=88.5214, height=47.4222)

        self.button_img_update = PhotoImage(file=self.relative_to_assets("button_update.png", "Frame"))
        self.update = Button(image=self.button_img_update, borderwidth=0, highlightthickness=0, activebackground="#51908D", command=lambda: Users_extend.update_user(self), relief="flat")
        self.update.place(x=302.9893, y=361.3862, width=85.8724, height=46.4923)

        self.button_img_create = PhotoImage(file=self.relative_to_assets("button_create.png", "Frame"))
        self.create = Button(image=self.button_img_create, borderwidth=0, highlightthickness=0, activebackground="#51908D", command=lambda: Users_extend.create_user(self), relief="flat")
        self.create.place(x=408.4795, y=360.7221, width=85.8641, height=46.4923)

        self.button_img_find = PhotoImage(file=self.relative_to_assets("button_find.png", "Frame"))
        self.find = Button(image=self.button_img_find, borderwidth=0, highlightthickness=0, activebackground="#51908D", command=lambda: Users_extend.search_user(self), relief="flat")
        self.find.place(x=958.5605, y=130.2529, width=56.9066, height=41.0992)

        self.button_img_reload = PhotoImage(file=self.relative_to_assets("button_reload.png", "Frame"))
        self.reload = Button(image=self.button_img_reload, borderwidth=0, highlightthickness=0, activebackground="#51908D", relief="flat")
        self.reload.place(x=1021.1572, y=130.2529, width=56.9066, height=41.0992)

        self.button_img_sales = PhotoImage(file=self.relative_to_assets("sales.png", "Window_element"))
        self.sales = Button(image=self.button_img_sales, borderwidth=0, highlightthickness=0, activebackground="#51908D", command=lambda: Main_process.Main_process.sales_button(self), relief="flat")
        self.sales.place(x=25.292, y=345.2335, width=213.716, height=59.4358)

        self.button_img_users = PhotoImage(file=self.relative_to_assets("user.png", "Window_element"))
        self.users = Button(image=self.button_img_users, borderwidth=0, highlightthickness=0, activebackground="#51908D", relief="flat")
        self.users.place(x=25.292, y=421.109, width=209.9222, height=58.8035)

        self.button_img_price = PhotoImage(file=self.relative_to_assets("price.png", "Window_element"))
        self.price = Button(image=self.button_img_price, borderwidth=0, highlightthickness=0, activebackground="#51908D", command=lambda: Main_process.Main_process.price_button(self), relief="flat")
        self.price.place(x=25.292, y=268.7257, width=213.716, height=60.7004)

        self.button_img_edit = PhotoImage(file=self.relative_to_assets("edit.png", "Window_element"))
        self.edit = Button(image=self.button_img_edit, borderwidth=0, highlightthickness=0, activebackground="#51908D", command=lambda: Main_process.Main_process.edit_button(self), relief="flat")
        self.edit.place(x=25.292, y=188.4241, width=213.716, height=64.4942)

        self.button_img_overview = PhotoImage(file=self.relative_to_assets("overview.png", "Window_element"))
        self.overview = Button(image=self.button_img_overview, borderwidth=0, highlightthickness=0, activebackground="#51908D", command=lambda: Main_process.Main_process.overview_button(self), relief="flat")
        self.overview.place(x=25.292, y=116.9747, width=230.1556, height=60.0681)
        self.create_treeview()
    def relative_to_assets(self, path: str, assets_type: str = "Frame") -> Path:
        if assets_type == "Frame":
            return self.assets_frame_path / Path(path)
        elif assets_type == "Window_element":
            return self.assets_WE_path / Path(path)

    def create_treeview(self):
        columns = ("Username", "Password", "Role")
        self.tree = ttk.Treeview(self.window, columns=columns, show="headings")

        self.tree.heading("Username", text="Username")
        self.tree.heading("Password", text="Password")
        self.tree.heading("Role", text="Role")

        self.tree.column("Username", width=5, anchor="center")
        self.tree.column("Password", width=40, anchor="center")
        self.tree.column("Role", width=40, anchor="center")

        self.tree.place(x=638, y=180, width=440, height=260)
        self.load_tree_data()
        self.tree.bind("<ButtonRelease-1>", self.display_user_info)
    def display_user_info(self, event):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0], "values")

            self.entry_1.delete(0, tk.END)
            self.entry_1.insert(0, values[0])

            self.entry_3.delete(0, tk.END)
            self.entry_3.insert(0, values[1])

            self.entry_4.delete(0, tk.END)
            self.entry_4.insert(0, values[2])
    def load_tree_data(self):
        self.tree.delete(*self.tree.get_children())
        self.users = self.admin_api.get_all_users_data()
        for user in self.users:
            self.tree.insert("", tk.END, values=(
                user["Username"],
                user["Password"],
                user["Role"]
            ))
if __name__ == "__main__":
    app = Users_view()
    app.window.mainloop()
