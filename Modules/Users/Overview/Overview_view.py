from tkinter import *
from pathlib import Path
import tkinter as tk

from tkinter import messagebox
import Modules.Main_process as Main_process
from Api.Main_Api import Main_Api
from Modules.Users.Overview.Overview_extend import Overview_extend
from Api.User_Api import User_Api

class Overview_view:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1095x650")
        self.window.title("Home")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)
        self.user_api = User_Api()
        self.canvas = Canvas(self.window, bg="#FFFFFF", height=650, width=1095, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        OUTPUT_PATH = Path(__file__).parent
        self.assets_path = OUTPUT_PATH.parent.parent.parent / "Images" / "Users" / "Overview"

        self.window.iconphoto(False, PhotoImage(file=self.relative_to_assets("icon_home.png")))

        self.background_img = PhotoImage(file=self.relative_to_assets("background_overview.png"))
        self.canvas.create_image(548.0, 325.0, image=self.background_img)

        self.entry_img = PhotoImage(file=self.relative_to_assets("entry.png"))
        self.canvas.create_image(606.7, 43.6, image=self.entry_img)
        self.entry = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0, font=("Arial", 12))
        self.entry.place(x=410.992, y=22, width=391.391, height=42.261)

        # Buttons
        self.cleaning_btn_img = PhotoImage(file=self.relative_to_assets("button_cleaning.png"))
        self.cleaning_btn = Button(image=self.cleaning_btn_img, borderwidth=0, highlightthickness=0, activebackground="#679487", bg="#679487", command=lambda: self.filter_rooms_by_status("Cleaning"), relief="flat")
        self.cleaning_btn.place(x=834.0, y=104.0, width=184.0, height=56.0)

        self.book_btn_img = PhotoImage(file=self.relative_to_assets("button_booked.png"))
        self.book_btn = Button(image=self.book_btn_img, borderwidth=0, highlightthickness=0, activebackground="#679487", bg="#679487", command=lambda: self.filter_rooms_by_status("Booked"), relief="flat")
        self.book_btn.place(x=632.9, y=103.0, width=174.1, height=57.0)

        self.available_btn_img = PhotoImage(file=self.relative_to_assets("button_avai.png"))
        self.available_btn = Button(image=self.available_btn_img, borderwidth=0, highlightthickness=0, activebackground="#679487", bg="#679487", command=lambda: self.filter_rooms_by_status("Available"), relief="flat")
        self.available_btn.place(x=214.9, y=103.0, width=174.0, height=54.0)

        self.all_btn_img = PhotoImage(file=self.relative_to_assets("button_all.png"))
        self.all_btn = Button(image=self.all_btn_img, borderwidth=0, highlightthickness=0, activebackground="#679487", bg="#679487", command=lambda: self.filter_rooms_by_status("All"), relief="flat")
        self.all_btn.place(x=70.8, y=104.0, width=110.7, height=53.0)

        self.occupied_btn_img = PhotoImage(file=self.relative_to_assets("button_occupied.png"))
        self.occupied_btn = Button(image=self.occupied_btn_img, borderwidth=0, highlightthickness=0, activebackground="#679487", bg="#679487", command=lambda: self.filter_rooms_by_status("Occupied"), relief="flat")
        self.occupied_btn.place(x=422.0, y=103.0, width=174.3, height=55.0)

        self.logout_btn_img = PhotoImage(file=self.relative_to_assets("button_logout.png"))
        self.logout_btn = Button(image=self.logout_btn_img, borderwidth=0, highlightthickness=0, activebackground="#679487", bg="#679487", command=lambda: Main_process.Main_process.log_out_button(self), relief="flat")
        self.logout_btn.place(x=39.0, y=573.0, width=113.0, height=52.0)

        self.quit_btn_img = PhotoImage(file=self.relative_to_assets("button_quit.png"))
        self.quit_btn = Button(image=self.quit_btn_img, borderwidth=0, highlightthickness=0, activebackground="#679487", bg="#679487", command=lambda: Main_process.Main_process.quit_button(self), relief="flat")
        self.quit_btn.place(x=168.0, y=573.0, width=118.0, height=52.0)

        self.booking_btn_img = PhotoImage(file=self.relative_to_assets("button_booking.png"))
        self.booking_btn = Button(image=self.booking_btn_img, borderwidth=0, highlightthickness=0, activebackground="#679487", bg="#679487", command=lambda: Main_process.Main_process.Select_Room_button(self), relief="flat")
        self.booking_btn.place(x=903.0, y=569.0, width=156.0, height=55.0)

        self.find_btn_img = PhotoImage(file=self.relative_to_assets("button_find.png"))
        self.find_btn = Button(image=self.find_btn_img, borderwidth=0, highlightthickness=0, activebackground="#D9D9D9", bg="#D9D9D9", command=lambda: Overview_extend.search_room(self), relief="flat")
        self.find_btn.place(x=785.0, y=31.0, width=25.0, height=25.3)

        self.api = Main_Api()
        self.rooms = self.load_room_data()
        self.room_frames = []

        self.filtered_rooms = self.rooms.copy()
        self.filter_rooms_by_status("All")
        self.sort_rooms()
        self.create_room_frames()
        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

    def sort_rooms(self):
        def room_sort_key(room):
            try:
                parts = room['RoomID'].split('.')
                return (int(parts[0][1:]) if len(parts[0]) > 1 else 0,
                        int(parts[1]) if len(parts) > 1 else 0)
            except:
                return (0, 0)

        self.filtered_rooms.sort(key=room_sort_key)

    def create_room_frames(self):
        for frame in self.room_frames:
            frame.destroy()
        self.room_frames.clear()

        frame_container = tk.Frame(self.window, bg="#346B4E", bd=3, relief="ridge")
        frame_container.place(x=95, y=170, width=895, height=400)

        canvas = tk.Canvas(frame_container, bg="#346B4E")
        v_scrollbar = tk.Scrollbar(frame_container, orient="vertical", command=canvas.yview)
        h_scrollbar = tk.Scrollbar(frame_container, orient="horizontal", command=canvas.xview)

        self.container_frame = tk.Frame(canvas, bg="#346B4E")
        canvas.create_window((0, 0), window=self.container_frame, anchor="nw")

        self.container_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        canvas.pack(side="top", fill="both", expand=True)
        v_scrollbar.pack(side="right", fill="y")
        h_scrollbar.pack(side="bottom", fill="x")

        rooms_per_row = 4
        room_width, room_height = 200, 130

        for index, room in enumerate(self.filtered_rooms):
            frame = tk.Frame(self.container_frame, width=room_width, height=room_height,
                             bg=self.get_status_color(room['Status']), bd=3, relief="ridge")
            frame.grid(row=index // rooms_per_row, column=index % rooms_per_row, padx=10, pady=10)
            frame.pack_propagate(False)

            frame.bind("<Button-1>", lambda event, r=room: self.show_detail_window(r))
            frame.bind("<Button-3>", lambda event, r=room: messagebox.showinfo("Trạng thái phòng",
                                                                               f"Phòng {r['RoomID']} - Trạng thái: {r['Status']}"))

            label1 = tk.Label(frame, text=f"Phòng {room['RoomID']}",
                              bg=self.get_status_color(room['Status']), fg='black', font=('Arial', 14, 'bold'))
            label1.pack(fill="x", pady=(10, 5))
            label2 = tk.Label(frame, text=f"Loại phòng: {room['RoomType']}",
                              bg=self.get_status_color(room['Status']), fg='black', font=('Arial', 11))
            label2.pack(fill="x")
            label3 = tk.Label(frame, text=f"Giá: {room['Price']} VND",
                              bg=self.get_status_color(room['Status']), fg='darkgreen', font=('Arial', 11, 'bold'))
            label3.pack(fill="x")
            label4 = tk.Label(frame, text=f"Trạng thái: {room['Status']}",
                              bg=self.get_status_color(room['Status']), fg='black', font=('Arial', 11))
            label4.pack(fill="x", pady=(0, 10))

            for widget in frame.winfo_children():
                widget.bind("<Button-1>", lambda event, r=room: self.show_detail_window(r))

            self.room_frames.append(frame)

    def show_detail_window(self, room):
        detail_win = tk.Toplevel(self.window)
        detail_win.title(f"Chi tiết phòng {room['RoomID']}")
        window_width = 300
        window_height = 250
        detail_win.update_idletasks()
        screen_width = detail_win.winfo_screenwidth()
        screen_height = detail_win.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        detail_win.geometry(f"{window_width}x{window_height}+{x}+{y}")
        detail_win.config(bg="#FFFFFF")
        tk.Label(detail_win, text=f"Room ID: {room['RoomID']}", font=('Arial', 12, 'bold'), bg="#FFFFFF").pack(pady=10)
        tk.Label(detail_win, text=f"Room Type: {room['RoomType']}", font=('Arial', 12), bg="#FFFFFF").pack(pady=5)
        tk.Label(detail_win, text=f"Price: {room['Price']} VND", font=('Arial', 12), fg='darkgreen', bg="#FFFFFF").pack(
            pady=5)
        status_label = tk.Label(detail_win, text=f"Current Status: {room['Status']}", font=('Arial', 12), bg="#FFFFFF")
        status_label.pack(pady=5)
        status_frame = tk.Frame(detail_win, bg="#FFFFFF")
        status_frame.pack(pady=10)
        statuses = ["Available", "Occupied", "Booked", "Cleaning"]
        allowed_transitions = {"Available": "Cleaning", "Cleaning": "Available", "Booked": "Occupied",
                               "Occupied": "Available"}
        current_status = room["Status"]
        allowed_status = allowed_transitions.get(current_status, None)
        status_buttons = []
        for st in statuses:
            state = "normal" if st == allowed_status else "disabled"
            btn = tk.Button(status_frame, text=st, font=('Arial', 10), state=state,
                            command=lambda s=st: self.update_status_detail(room, s, status_label, status_buttons,
                                                                           detail_win))
            btn.pack(side="left", padx=5)
            status_buttons.append((btn, st))
        tk.Button(detail_win, text="Close", command=detail_win.destroy, font=("Arial", 12)).pack(pady=10)

    def update_status_detail(self, room, new_status, status_label, status_buttons, detail_win):
        data = {"RoomID": room["RoomID"], "Status": new_status}
        result = self.user_api.update_new_status(data)
        if result == 0:
            room["Status"] = new_status
            status_label.config(text=f"Current Status: {new_status}")
            for btn, st in status_buttons:
                btn.config(state="disabled")
            self.rooms = self.load_room_data()
            self.sort_rooms()
            self.create_room_frames()
            messagebox.showinfo("Notification", f"Status of  {room['RoomID']} was updated as {new_status}.")
            detail_win.destroy()
        else:
            messagebox.showerror("Error", "Nothing change!")

    def load_room_data(self):
        return [
            {
                "RoomID": room.get("RoomID"),
                "RoomType": room.get("RoomType"),
                "Price": room.get("Price"),
                "Status": room.get("Status")
            }
            for room in Main_Api().get_all_rooms_data()
        ]
    def filter_rooms_by_status(self, status):
        print(f"Filter trạng thái: {status}")
        if status == 'All':
            self.filtered_rooms = self.rooms.copy()
        else:
            self.filtered_rooms = [room for room in self.rooms if room['Status'] == status]
        self.create_room_frames()
    def get_status_color(self, status):
        colors = {
            'Available': '#C8E6C9',
            'Occupied': '#FFCDD2',
            'Booked': '#D1C4E9',
            'Cleaning': '#FFF9C4'
        }
        return colors.get(status, '#ECEFF1')

if __name__ == "__main__":
    Overview_view()

