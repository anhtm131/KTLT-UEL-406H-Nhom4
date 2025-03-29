from tkinter import *
from pathlib import Path
import Modules.Main_process as Main_process
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import Api.User_Api as api
from Modules.Users.Select_Room.Selected_Room_extend import Selected_Room_extend
from datetime import datetime, timedelta
import Api.Main_Api as Main_Api

class Invoice_view:
    def __init__(self, day_in=None, day_out=None):
        self.window = Tk()
        self.window.geometry("966x600")
        self.window.title("Invoice")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)

        self.canvas = Canvas(self.window, bg="#FFFFFF", height=600, width=966, bd=0, highlightthickness=0,
                             relief="ridge")
        self.canvas.place(x=0, y=0)

        OUTPUT_PATH = Path(__file__).parent
        self.assets_frame_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Users" / "Invoice"

        self.window.iconphoto(False, PhotoImage(file=self.relative_to_assets("icon.png", "Frame")))
        self.background_img = PhotoImage(file=self.relative_to_assets("background_invoices.png", "Frame"))
        self.canvas.create_image(483.0, 300.0, image=self.background_img)

        self.entry_total = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_total.place(x=427.48, y=464.49, width=244.75, height=28.68)

        self.button_img_back = PhotoImage(file=self.relative_to_assets("button_back.png", "Frame"))
        self.button_back = Button(image=self.button_img_back, borderwidth=0, highlightthickness=0,
                                  activebackground="#6C9587",
                                  command=lambda: Main_process.Main_process.back_button(self), relief="flat")
        self.button_back.place(x=671.0, y=527.0, width=110.0, height=47.0)

        self.user_api = api.User_Api()
        self.rooms = self.load_room_data()
        self.create_treeview()
        self.update_total()
        self.window.mainloop()
    def relative_to_assets(self, path: str, assets_type: str = "Frame") -> Path:
        return self.assets_frame_path / Path(path) if assets_type == "Frame" else Path(path)

    def update_total(self):
        self.entry_total.delete(0, END)
        if hasattr(self, "day_in") and hasattr(self, "day_out") and self.day_in and self.day_out:
            try:
                checkin_date = datetime.strptime(self.day_in, "%d/%m/%Y")
                checkout_date = datetime.strptime(self.day_out, "%d/%m/%Y")
                total_days = (checkout_date - checkin_date).days
                if total_days < 1:
                    total_days = 1
            except Exception as e:
                print("Lỗi tính số ngày:", e)
                total_days = 1
        else:
            total_days = 1
        cart_data = [
            {"RoomID": room["RoomID"], "Price": int(room["Price"]), "Days": total_days}
            for room in self.rooms
        ]
        try:
            if cart_data:
                self.user_api.create_invoice(cart_data)
            all_invoices = self.user_api.get_all_invoices_data()
            last_invoice = all_invoices[-1] if all_invoices else None
            if last_invoice and "Total" in last_invoice:
                total_cost = last_invoice["Total"]
            else:
                total_cost = 0
            self.entry_total.insert(0, str(total_cost))
        except Exception as e:
            print(e)
            self.entry_total.insert(0, "0")
    def load_room_data(self):
        selected_manager = Selected_Room_extend()
        room_info = selected_manager.get_selected_rooms()
        return room_info
    def create_treeview(self):
        columns = ("RoomID", "RoomType", "Price", "Status")
        frame = tk.Frame(self.window, width=100, height=900, bg="white", bd=2, relief="ridge")
        frame.place(x=170, y=90)
        style = ttk.Style()
        style.configure("Treeview", rowheight=30, font=("", 12))
        style.configure("Treeview.Heading", font=("Arial", 14, "bold"))
        self.tree = ttk.Treeview(frame, columns=columns, show="headings", height=10)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor="center")
        self.tree.pack(fill="both", expand=True)
        self.load_data_into_treeview()
    def load_data_into_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for room in self.rooms:
            self.tree.insert("", "end", values=(room["RoomID"], room["RoomType"], room["Price"], room["Status"]))

    def update_room_status_to_booked(self, room_id):
        try:
            update_status = self.user_api.update_status(room_id, "Booked")

            if update_status:
                print(f"Room {room_id} has been successfully booked.")

                # Kiểm tra dữ liệu sau khi cập nhật
                updated_room = self.user_api.get_room_by_id(room_id)
                print(f"Updated Room Data: {updated_room}")

                # Cập nhật danh sách phòng trên giao diện
                self.rooms = self.get_all_rooms_data()
                self.reload_treeview()
            else:
                print(f"Failed to update room {room_id} status.")
        except Exception as e:
            print(f"Error updating room status: {e}")


if __name__ == "__main__":
    Invoice_view()
