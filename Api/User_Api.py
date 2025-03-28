import Api.Main_Api as main_api
import datetime

class User_Api(main_api.Main_Api):

    def __init__(self):
        super().__init__()
        self.connect_mongodb()
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

    def update_new_status(self, data):
        result = self.rooms_collection.update_one(
            {"RoomID": data["RoomID"]},
            {"$set": {"Status": data["Status"]}}
        )
        if result.modified_count > 0:
            return 0
        else:
            return -1

    def get_all_rooms_avai_data(self):
        rooms = self.rooms_collection.find({"Status": "Available"}).sort("RoomID", 1)
        rooms_data = []
        for room in rooms:
            rooms_data.append(room)
        return rooms_data




