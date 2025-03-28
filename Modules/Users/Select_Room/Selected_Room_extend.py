class Select_Room_Extend:
    def __init__(self):
        super().__init__()

        self.rooms = self.load_rooms_data()
        self.selected_rooms = []
        #self.cart_window = None
        self.create_treeview()
        self.window.mainloop()



    def add_selected_room(self):
        selected_item = self.tree.focus()

        values = self.tree.item(selected_item)["values"]

        room_data = {
            "RoomID": values[0],
            "RoomType": values[1],
            "Price": values[2]
        }

        if room_data not in self.selected_rooms:
            self.selected_rooms.append(room_data)
            print("Added Room:", room_data)

        print("Current selected rooms:", self.selected_rooms)
        if self.cart_window:
            self.cart_window.update_selected_rooms_table(self.selected_rooms)

    def open_cart_window(self):
        if self.cart_window is None or not tk.Toplevel.winfo_exists(self.cart_window.window):
            self.cart_window = CartCustomerDetails()

        self.cart_window.update_selected_rooms_table(self.selected_rooms)
