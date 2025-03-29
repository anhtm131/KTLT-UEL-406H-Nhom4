import tkinter as tk
from tkinter import messagebox
class Rooms_extend():

    @staticmethod
    def update_room_button_handle(obj):
        selected = obj.tree.selection()
        if selected:
            room_id = obj.entry_roomid.get()
            updated_data = {
                "RoomID" : room_id,
                "RoomType": obj.combo_roomtype.get(),
                "Price": obj.entry_price.get().replace(",", ""),
                "Status": obj.entry_status.get()
            }

            result = obj.admin_api.update_room(updated_data, room_id)
            if result == 0:
                messagebox.showinfo("Congratulation","Update successfully")
            elif result ==-1:
                messagebox.showerror("Error","Can not find room in database")
            elif result == -2:
                messagebox.showerror("Error", "No new information was update")
            obj.load_tree_data()
    @staticmethod
    def create_room_button_handle(obj):
        new_room = {
            "RoomID": obj.entry_roomid.get(),
            "RoomType": obj.combo_roomtype.get(),
            "Price": obj.entry_price.get().replace(",", ""),
            "Status": obj.entry_status.get()
        }

        result = obj.admin_api.add_new_room(new_room)
        if result == 0:
            messagebox.showinfo("Congratulation", "Create successfully")
        elif result == -1:
            messagebox.showerror("Error","Room is exist")
        obj.load_tree_data()
    @staticmethod
    def delete_room_button_handle(obj):
        selected = obj.tree.selection()
        if selected:
            room_id = obj.entry_roomid.get()
            result = obj.admin_api.remove_room(room_id)
            if result == 0:
                messagebox.showinfo("Congratulation", "Delete successfully")
            else:
                messagebox.showerror("Error","Can not find room to delete")
            obj.load_tree_data()
    @staticmethod
    def search_room(obj):
        keyword = obj.entry_find.get().strip()
        filtered_rooms = [room for room in obj.rooms if keyword.lower() in str(room["RoomID"]).lower()]
        obj.tree.delete(*obj.tree.get_children())
        for room in filtered_rooms:
            price = str(room["Price"]).replace(",", "")
            obj.tree.insert("", tk.END, values=(
                room["RoomID"],
                room["RoomType"],
                price,
                room["Status"]
            ))
    @staticmethod
    def reset_view(obj):
        obj.entry_find.delete(0, tk.END)
        obj.entry_roomid.delete(0, tk.END)
        obj.combo_roomtype.set('')
        obj.entry_price.config(state="normal")
        obj.entry_price.delete(0, tk.END)
        obj.entry_price.config(state="readonly")
        obj.entry_status.config(state="normal")
        obj.entry_status.delete(0, tk.END)
        obj.entry_status.config(state="readonly")
        obj.load_tree_data()


