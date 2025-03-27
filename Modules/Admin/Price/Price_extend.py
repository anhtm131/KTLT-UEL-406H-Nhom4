import json
import tkinter as tk
from tkinter import ttk, Frame
from Modules.Admin.Price.Price_view import Price_view
from tkinter import messagebox

class Price_extend(Price_view):
    def __init__(self):
        super().__init__()

        self.rooms = self.load_rooms_data()
        self.create_treeview()
        self.button_update.config(command=lambda: self.update_price())
        self.window.mainloop()
    def load_rooms_data(self):
        try:
            with open(r'D:\KTLT_DoAnCuoiKy_Final\Data\rooms.json', 'r', encoding='utf-8') as file:
                data=json.load(file)
                return data
        except Exception as e:
            print("Lỗi load data:", e)
            return []
    def save_rooms_data(self):
        try:
            with open(r'D:\KTLT_DoAnCuoiKy_Final\Data\rooms.json', 'w', encoding='utf-8') as file:
                json.dump(self.rooms, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print("Lỗi lưu data:", e)

    def create_treeview(self):
        columns = ("Room Type", "Price")
        self.tree = ttk.Treeview(self.window, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=200, anchor="center")
        self.tree.place(x=308, y=200, width=740, height=260)
        price_dict = {}
        for room in self.rooms:
            room_type = room.get("RoomType")
            price = room.get("Price")
            if room_type not in price_dict:
                price_dict[room_type] = price
        for room_type in ["Standard", "Deluxe", "President"]:
            price = price_dict.get(room_type)
            if price:
                self.tree.insert("", tk.END, values=(room_type, price))
        self.tree.bind("<ButtonRelease-1>", self.on_row_click)

    def on_row_click(self, event):
        selected_item = self.tree.focus()
        if selected_item:
            values = self.tree.item(selected_item, "values")
            if values:
                room_type, price = values
                self.selected_room_type = room_type  # Ghi nhớ loại phòng
                self.entry.delete(0, tk.END)
                self.entry.insert(0, price)

    def update_price(self):
        new_price = self.entry.get()
        room_type = self.selected_room_type
        if not room_type:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn loại phòng trước.")
            return
        if not new_price.isdigit():
            messagebox.showerror("Lỗi", "Giá phải là số.")
            return

        for room in self.rooms:
            if room.get("RoomType") == room_type:
                room["Price"] = new_price

        for item in self.tree.get_children():
            values = self.tree.item(item, "values")
            if values[0] == room_type:
                self.tree.item(item, values=(room_type, new_price))

        with open("rooms.json", "w", encoding="utf-8") as f:
            json.dump(self.rooms, f, indent=4, ensure_ascii=False)

        messagebox.showinfo("Thành công", f"Đã cập nhật giá {new_price} cho loại phòng {room_type}")


if __name__ == "__main__":
    Price_extend()
