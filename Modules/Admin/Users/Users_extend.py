import tkinter as tk
from tkinter import messagebox

class Users_extend:
    @staticmethod
    def update_user(obj):
        selected = obj.tree.selection()
        if selected:
            values = obj.tree.item(selected[0], "values")
            username = values[0]
            new_data = {
                "Username": username,
                "Password": obj.entry_3.get(),
                "Role": obj.entry_4.get()
            }
            result = obj.admin_api.update_user(new_data)
            if result == 0:
                messagebox.showinfo("Thông báo", "Cập nhật người dùng thành công!")
            else:
                messagebox.showwarning("Lỗi", "Cập nhật thất bại: không có thông tin mới hoặc lỗi!")
            obj.load_tree_data()
        else:
            messagebox.showwarning("Thông báo", "Vui lòng chọn user cần cập nhật!")

    @staticmethod
    def create_user(obj):
        new_user = {
            "Username": obj.entry_1.get(),
            "Password": obj.entry_3.get(),
            "Role": obj.entry_4.get()
        }
        result = obj.admin_api.add_new_user(new_user)
        if result == 0:
            messagebox.showinfo("Thông báo", "Tạo người dùng thành công!")
        elif result == -1:
            messagebox.showerror("Lỗi", "Người dùng đã tồn tại!")
        obj.load_tree_data()

    @staticmethod
    def delete_user(obj):
        selected = obj.tree.selection()
        if selected:
            values = obj.tree.item(selected[0], "values")
            username = values[0]
            result = obj.admin_api.remove_user({"Username": username})
            if result == 0:
                messagebox.showinfo("Thông báo", "Xoá người dùng thành công!")
            else:
                messagebox.showerror("Lỗi", "Không tìm thấy người dùng để xoá!")
            obj.load_tree_data()
        else:
            messagebox.showwarning("Thông báo", "Vui lòng chọn người dùng cần xoá!")

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



if __name__ == "__main__":
    Users_extend()