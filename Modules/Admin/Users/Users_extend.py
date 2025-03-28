import json
import tkinter as tk
from tkinter import ttk

from pymongo.synchronous.network import command

from Modules.Admin.Users.Users_view import Users_view


class Users_extend(Users_view):
    def __init__(self):
        super().__init__()

        self.users = self.load_users_data()
        self.create_treeview()

        self.create.config(command=lambda: self.create_user())
        self.update.config(command=lambda: self.update_user())
        self.delete.config(command=lambda: self.delete_user())
        self.find.config(command=lambda : self.search_user())
        self.reload.config(command=lambda: self.refresh_treeview())
        self.window.mainloop()

    def load_users_data(self):
        try:
            with open(r'D:\KTLT_DoAnCuoiKy_Final\Data\users.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        except Exception as e:
            print("Lỗi load data:", e)
            return []

    def save_users_data(self):
        try:
            with open(r'D:\KTLT_DoAnCuoiKy_Final\Data\users.json', 'w', encoding='utf-8') as file:
                json.dump(self.users, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print("Lỗi lưu data:", e)

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

        for user in self.users:
            self.tree.insert("", tk.END, values=(
                user["Username"],
                user["Password"],
                user["Role"]
            ))

        self.tree.bind("<ButtonRelease-1>", self.display_user_info)

    def display_user_info(self, event):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0], "values")

            self.entry_1.delete(0, tk.END)
            self.entry_1.insert(0, values[0])  # username

            self.entry_3.delete(0, tk.END)
            self.entry_3.insert(0, values[1])  # pass

            self.entry_4.delete(0, tk.END)
            self.entry_4.insert(0, values[2])  # role

    def update_user(self):
        try:
            selected = self.tree.selection()
            if selected:
                values = self.tree.item(selected[0], "values")
                for user in self.users:
                    if user["Username"] == values[0]:
                        user["Password"] = self.entry_3.get()
                        user["Role"] = self.entry_4.get()
                        break
                self.save_users_data()
                self.refresh_treeview()
        except Exception as e:
            print(e)

    def create_user(self):
        new_user = {
            "Username": self.entry_1.get(),
            "Password": self.entry_3.get(),
            "Role": self.entry_4.get()
        }
        self.users.append(new_user)
        self.save_users_data()
        self.refresh_treeview()



    def delete_user(self):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0], "values")
            self.users = [user for user in self.users if user["Username"] != values[0]]
            self.save_users_data()
            self.refresh_treeview()

    def search_user(self):
        search_query = self.entry_2.get().strip().lower()
        self.tree.delete(*self.tree.get_children())

        for user in self.users:
            if search_query in user["Username"].lower():
                self.tree.insert("", tk.END, values=(
                    user["Username"],
                    user["Password"],
                    user["Role"]
                ))

    def refresh_treeview(self):
        self.tree.delete(*self.tree.get_children())
        for user in self.users:
            self.tree.insert("", tk.END, values=(
                user["Username"],
                user["Password"],
                user["Role"]
            ))
if __name__ == "__main__":
    Users_extend()