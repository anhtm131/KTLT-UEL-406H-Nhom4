from pymongo import MongoClient
import os
from dotenv import load_dotenv, find_dotenv


class Main_Api:
    def __init__(self):
        self.connect_mongodb()
    def connect_mongodb(self):
        load_dotenv(find_dotenv())
        host = os.getenv("HOSTNAME")
        self.client = MongoClient(host)

        self.db = self.client['HotelManagementDB']
        self.users_collection = self.db['users']
        self.rooms_collection = self.db['rooms']
        self.invoices_collection = self.db['invoices']

    def get_all_rooms_data(self):
        rooms = self.rooms_collection.find().sort("RoomID", 1)
        rooms_data = []
        for room in rooms:
            rooms_data.append(room)
        return rooms_data

    def get_all_invoices_data(self):
        invoices = self.invoices_collection.find().sort("InvoiceID", 1)
        invoices_data = []
        for invoice in invoices:
            sub_invoice_data = {}
            sub_invoice_data["InvoiceID"] = invoice["InvoiceID"]
            sub_invoice_data["Invoice_Date"] = invoice["Invoice_Date"]
            sub_invoice_data["Total"] = invoice["Total"]
            invoices_data.append(sub_invoice_data)
        return invoices_data



    def get_all_users_data(self):
        users = self.users_collection.find()
        users_data = []
        for user in users:
            users_data.append(user)
        return users_data

    def get_room_types(self):
        rooms = self.rooms_collection.find({}, {"_id": 0, "RoomType": 1, "Price": 1})
        room_types = {room["RoomType"]: room["Price"] for room in rooms}
        return [{"RoomType": rt, "Price": price} for rt, price in room_types.items()]



