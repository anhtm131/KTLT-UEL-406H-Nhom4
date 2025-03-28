import Api.Main_Api as main_api
import datetime

class User_Api(main_api.Main_Api):

    def __init__(self):
        super().__init__()
        self.connect_mongodb()

    def display_room_detail(self, data,new_status):
        room_id = data["RoomID"]
        room = self.rooms_collection.find_one({"RoomID": room_id}, {"Status": 1})
        result = {"RoomStatus": room["Status"]}
        if room["Status"].lower() in ["occupied", "booked"]:
            invoice = self.invoices_collection.find_one(
                {"Cart.RoomID": room_id},
                {"Invoice_Date": 1, "Cart": 1, "Customer Information": 1},
                sort=[("Invoice_Date", -1)])
            cart_item = None
            for item in invoice["Cart"]:
                if item["RoomID"] == room_id:
                    cart_item = item
                    break
            result["Customer Information"] = invoice["Customer Information"]
            result["Time"] = {cart_item["DayIn"] + " - " + cart_item["DayOut"]}
        else:
            return result ==[] #no in4 display
        self.rooms_collection.update_one({"RoomID": room_id}, {"$set": {"Status": new_status}})
        return result
    def get_last_invoice_id(self):
            invoices = self.invoices_collection.find().sort([('Invoice_ID', -1)])
            last_invoice_id = invoices[0]['Invoice_ID']
            return last_invoice_id
    def create_new_invoice_id(self):
        last_invoice_id = self.get_last_invoice_id()
        id = last_invoice_id
        number = id[3:]
        new_id = int(number) + 1
        self.new_invoice_id = f"INV{new_id:03}"

    def create_invoice(self, customer_information, cart):
        self.create_new_invoice_id()
        invoice_date = datetime.datetime.now().strftime("%d/%m/%Y")
        total = sum(item["Price"] * item["Days"] for item in cart)
        invoice = {
            "InvoiceID": self.new_invoice_id,
            "Invoice_Date": invoice_date,
            "Total": total,
            "Cart": cart,
            "Customer Information": customer_information
        }
        self.invoices_collection.insert_one(invoice)

    def update_new_status(self,data):
        self.rooms_collection.update({"RoomID": data["RoomID"]}, {"$set": {"Status": data["Status"]}})

    def get_all_rooms_avai_data(self):
        rooms = self.rooms_collection.find({"Status": "Available"})
        rooms_data = []
        for room in rooms:
            rooms_data.append(room)
        return rooms_data





