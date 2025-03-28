import tkinter as tk
from tkinter import messagebox
class Users_extend:
    @staticmethod
    def update_user(obj):
        selected = obj.tree.selection()
        if selected:
            username = obj.entry_1.get()
            new_data = {
                "Username": username,
                "Password": obj.entry_3.get(),
                "Role": obj.entry_4.get()
            }
            result = obj.admin_api.update_user(new_data)
            if result == 0:
                messagebox.showinfo("Congratulation", "Update successfully")
            elif result == -1:
                messagebox.showerror("Error", "Can not find user in database")
            elif result == -2:
                messagebox.showerror("Error", "No new information was update")
            obj.load_tree_data()
    @staticmethod
    def create_user(obj):
        new_user = {
            "Username": obj.entry_1.get(),
            "Password": obj.entry_3.get(),
            "Role": obj.entry_4.get()
        }
        result = obj.admin_api.add_new_user(new_user)
        if result == 0:
            messagebox.showinfo("Notification", "Create user successfully!")
        elif result == -1:
            messagebox.showerror("Error", "User is exist")
        obj.load_tree_data()

    @staticmethod
    def delete_user(obj):
        selected = obj.tree.selection()
        if selected:
            username = obj.entry_1.get()
            result = obj.admin_api.remove_user({"Username": username})
            if result == 0:
                messagebox.showinfo("Notification", "Delete successfully")
            elif result == -1:
                messagebox.showerror("Error", "Can not find user to delete")
            obj.load_tree_data()


    @staticmethod
    def search_user(obj):
        search_query = obj.entry_2.get().strip().lower()
        obj.tree.delete(*obj.tree.get_children())

        for user in obj.users:
            if search_query in user["Username"].lower():
                obj.tree.insert("", tk.END, values=(
                    user["Username"],
                    user["Password"],
                    user["Role"]
                ))
        obj.load_tree_data()

    @staticmethod
    def reset_view(obj):
        obj.entry_1.delete(0, tk.END)
        obj.entry_3.delete(0, tk.END)
        obj.entry_4.set('')


        obj.load_tree_data()
    @staticmethod
    def search_user(obj):
        keyword = obj.entry_2.get().strip()
        filtered_users = [user for user in obj.users if keyword.lower() in user["Username"].lower()]
        obj.tree.delete(*obj.tree.get_children())
        for user in filtered_users:
            obj.tree.insert("", "end", values=(
                user["Username"],
                user["Password"],
                user["Role"]
            ))


if __name__ == "__main__":
    Users_extend()