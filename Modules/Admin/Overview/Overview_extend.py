from Modules.Admin.Overview.Overview_view import Overview_view
import tkinter as tk
import json

class Overview_extend(Overview_view):
    def __init__(self):
        super().__init__()

        self.rooms = self.load_room_data()
        self.filtered_rooms = self.rooms.copy()
        self.room_frames = []

        self.button_all.config(command=lambda: self.filter_rooms_by_status("All"))
        self.button_avai.config(command=lambda: self.filter_rooms_by_status("Available"))
        self.button_occupied.config(command=lambda: self.filter_rooms_by_status("Occupied"))
        self.button_booking.config(command=lambda: self.filter_rooms_by_status("Booked"))
        self.button_cleaning.config(command=lambda: self.filter_rooms_by_status("Cleaning"))

        self.filter_rooms_by_status("All")

    def create_room_frames(self):
        for frame in self.room_frames:
            frame.destroy()
        self.room_frames.clear()

        rooms = self.filtered_rooms
        x = 285
        y = 170
        rooms_every_row = 3
        room_width = 250
        room_height = 150
        spacing_x = 20
        spacing_y = 25

        for index, room in enumerate(rooms):
            frame = tk.Frame(
                self.window,
                width=room_width,
                height=room_height,
                bg=self.get_status_color(room['Status']),
                bd=3,
                relief='ridge',
                highlightbackground="#ccc", highlightthickness=2
            )
            frame.place(x=x, y=y)
            frame.pack_propagate(False)

            room_id = tk.Label(
                frame, text=f"Phòng {room['RoomID']}",
                bg=self.get_status_color(room['Status']),
                fg='black',
                font=('Arial', 14, 'bold'),
                anchor="center"
            )
            room_id.pack(fill="x", pady=(10, 5))

            room_type = tk.Label(
                frame, text=f"Loại: {room['RoomType']}",
                bg=self.get_status_color(room['Status']),
                fg='black',
                font=('Arial', 11)
            )
            room_type.pack(fill="x", pady=(0, 5))

            price = tk.Label(
                frame, text=f"Giá: {room['Price']} VND",
                bg=self.get_status_color(room['Status']),
                fg='darkgreen',
                font=('Arial', 11, 'bold')
            )
            price.pack(fill="x", pady=(0, 5))
            status = tk.Label(
                frame, text=f"Trạng thái: {room['Status']}",
                bg=self.get_status_color(room['Status']),
                fg='black',
                font=('Arial', 11)
            )
            status.pack(fill="x", pady=(0, 10))

            self.room_frames.append(frame)
            if (index + 1) % rooms_every_row == 0:
                x = 285
                y += room_height + spacing_y
            else:
                x += room_width + spacing_x

    def load_room_data(self):
        with open(r'D:\KTLT_DoAnCuoiKy_Final\Data\rooms.json', 'r', encoding='utf-8') as file:
            return json.load(file)

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
            self.filtered_rooms = [
                room for room in self.rooms if room['Status'] == status
            ]
        self.create_room_frames()
    def search_bar(self):
        pass
if __name__ == "__main__":
    app = Overview_extend()
    app.run()
