from Modules.Admin.Overview.Overview_view import Overview_view
from Api.Admin_Api import Admin_Api
import tkinter as tk


class Overview_extend(Overview_view):
    def __init__(self):
        super().__init__()

        self.api = Admin_Api()
        self.rooms = self.load_room_data()
        self.filtered_rooms = self.rooms.copy()
        self.room_frames = []

        self.button_all.config(command=lambda: self.filter_rooms_by_status("All"))
        self.button_avai.config(command=lambda: self.filter_rooms_by_status("Available"))
        self.button_occupied.config(command=lambda: self.filter_rooms_by_status("Occupied"))
        self.button_booking.config(command=lambda: self.filter_rooms_by_status("Booked"))
        self.button_cleaning.config(command=lambda: self.filter_rooms_by_status("Cleaning"))
        self.button_find.config(command=lambda: self.search_room())

        self.filter_rooms_by_status("All")

    def create_room_frames(self):
        for frame in self.room_frames:
            frame.destroy()
        self.room_frames.clear()

        if hasattr(self, "container_frame"):
            self.container_frame.destroy()

        frame_container = tk.Frame(self.window, bg="#346B4E", bd=3, relief="ridge")
        frame_container.place(x=290, y=160, width=780, height=480)

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
        spacing_x, spacing_y = 20, 25

        for index, room in enumerate(self.filtered_rooms):
            frame = tk.Frame(
                self.container_frame,
                width=room_width, height=room_height,
                bg=self.get_status_color(room['Status']), bd=3, relief="ridge"
            )
            frame.grid(row=index // rooms_per_row, column=index % rooms_per_row, padx=10, pady=10)
            frame.pack_propagate(False)

            tk.Label(frame, text=f"RoomID {room['RoomID']}",
                     bg=self.get_status_color(room['Status']), fg='black',
                     font=('Arial', 14, 'bold')).pack(fill="x", pady=(10, 5))

            tk.Label(frame, text=f"RoomType: {room['RoomType']}",
                     bg=self.get_status_color(room['Status']), fg='black',
                     font=('Arial', 11)).pack(fill="x")

            tk.Label(frame, text=f"Price: {room['Price']} VND",
                     bg=self.get_status_color(room['Status']), fg='darkgreen',
                     font=('Arial', 11, 'bold')).pack(fill="x")

            tk.Label(frame, text=f"Status: {room['Status']}",
                     bg=self.get_status_color(room['Status']), fg='black',
                     font=('Arial', 11)).pack(fill="x", pady=(0, 10))

            self.room_frames.append(frame)

        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(-1 * (e.delta // 120), "units"))
        canvas.bind_all("<Shift-MouseWheel>", lambda e: canvas.xview_scroll(-1 * (e.delta // 120), "units"))

    def load_room_data(self):
        return [
            {"RoomID": "P.101", "RoomType": "President", "Price": "10000000", "Status": "Cleaning"},
            {"RoomID": "P.102", "RoomType": "Standard", "Price": "1000000", "Status": "Occupied"},
            {"RoomID": "P.103", "RoomType": "Deluxe", "Price": "987", "Status": "Cleaning"},
            {"RoomID": "P.104", "RoomType": "Deluxe", "Price": "987", "Status": "Cleaning"},
            {"RoomID": "P.201", "RoomType": "President", "Price": "10000000", "Status": "Booked"},
            {"RoomID": "P.202", "RoomType": "Deluxe", "Price": "987", "Status": "Cleaning"},
            {"RoomID": "P.203", "RoomType": "President", "Price": "10000000", "Status": "Booked"},
            {"RoomID": "P.204", "RoomType": "Deluxe", "Price": "987", "Status": "Cleaning"},
            {"RoomID": "P.301", "RoomType": "Deluxe", "Price": "987", "Status": "Booked"},
            {"RoomID": "P.302", "RoomType": "Standard", "Price": "1000000", "Status": "Cleaning"},
            {"RoomID": "P.303", "RoomType": "Deluxe", "Price": "987", "Status": "Booked"},
            {"RoomID": "P.304", "RoomType": "Deluxe", "Price": "987", "Status": "Cleaning"},
            {"RoomID": "P.401", "RoomType": "Deluxe", "Price": "987", "Status": "Booked"},
            {"RoomID": "P.402", "RoomType": "Standard", "Price": "1000000", "Status": "Cleaning"},
            {"RoomID": "P.403", "RoomType": "Deluxe", "Price": "987", "Status": "Booked"},
            {"RoomID": "P.404", "RoomType": "Deluxe", "Price": "987", "Status": "Cleaning"}
        ]

    def get_status_color(self, status):
        colors = {
            'Available': '#C8E6C9',
            'Occupied': '#FFCDD2',
            'Booked': '#D1C4E9',
            'Cleaning': '#FFF9C4'
        }
        return colors.get(status, '#ECEFF1')

    def filter_rooms_by_status(self, status):
        print(f"Filter trạng thái: {status}")
        if status == 'All':
            self.filtered_rooms = self.rooms.copy()
        else:
            self.filtered_rooms = [room for room in self.rooms if room['Status'] == status]
        self.create_room_frames()

    def search_room(self):
        query = self.entry_find.get().strip().lower()
        self.filtered_rooms = [
            room for room in self.rooms
            if query in str(room['RoomID']).lower()
        ]
        self.create_room_frames()


if __name__ == "__main__":
    app = Overview_extend()
    app.run()

