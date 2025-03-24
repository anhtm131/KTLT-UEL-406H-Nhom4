from Modules.Admin.Price.Price_view import Price_view
from tkinter import ttk, Frame


class Price_extend(Price_view):
    def __init__(self):
        super().__init__()

        if not hasattr(self, "window") or not self.window.winfo_exists():
            print("Lỗi: self.window đã bị hủy!")
            return

        self.create_ui()
        self.window.mainloop()  # Chạy Tkinter sau khi tạo xong UI

    def create_ui(self):
        """Tạo giao diện hiển thị danh sách loại phòng trong Frame."""
        if not hasattr(self, "window") or not self.window.winfo_exists():
            print("Lỗi: Không thể tạo UI vì self.window không hợp lệ!")
            return

        frame = Frame(self.window, bd=2, relief="ridge")
        frame.place(x=50, y=50, width=700, height=400)

        columns = ("Room Type", "Price")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings")
        self.tree.heading("Room Type", text="Room Type")
        self.tree.heading("Price", text="Price")
        self.tree.pack(expand=True, fill="both")


        self.rooms = [("Standard", "500"), ("Deluxe", "700"), ("Suite", "1200")]
        for room in self.rooms:
            self.tree.insert("", "end", values=room)


if __name__ == "__main__":
    Price_extend()
