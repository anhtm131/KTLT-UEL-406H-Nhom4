class Price_extend():


    @staticmethod
    def update_price(obj):
        selected = obj.tree.selection()
        if selected:
            values = obj.tree.item(selected[0], "values")
            room_type = values[0]

            updated_data = {
                "RoomType": room_type,
                "Price": obj.entry.get(),
            }

            result = obj.admin_api.update_price(updated_data)
            if result == 0:
                print("Cập nhật thành công!")
            else:
                print("Không có thông tin mới hoặc lỗi!")
            obj.load_tree_data()
        
if __name__ == "__main__":
    Price_extend()
