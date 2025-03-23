from pymongo import MongoClient
import os
from dotenv import load_dotenv, find_dotenv


class Api:
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
        rooms = self.rooms_collection.find()
        rooms_data = []
        for room in rooms:
            rooms_data.append(room)
        return rooms_data

    def get_all_invoices_data(self):
        invoices = self.invoices_collection.find()
        invoices_data = []
        for invoice in invoices:
            for item in invoice['Cart']:
                for CIF in invoice["CustomerInfo"]:
                    sub_invoice_data = {}
                    sub_invoice_data["Invoice_ID"] = invoice["Invoice_ID"]
                    sub_invoice_data["Invoice_Date"] = invoice["Invoice_Date"]
                    sub_invoice_data["Total"] = invoice["Total"]
                    # append item to sub_invoice_data
                    sub_invoice_data["RoomID"] = item["RoomID"]
                    sub_invoice_data["RoomType"] = item["RoomType"]
                    sub_invoice_data["Days"] = item["Days"]
                    sub_invoice_data["Price"] = item["Price"]
                    sub_invoice_data["Name"] = CIF["Name"]
                    sub_invoice_data["CCCD"] = CIF["CCCD"]
                    sub_invoice_data["PhoneNumber"] = CIF["PhoneNumber"]
                    sub_invoice_data["DayIn"] = CIF["DayIn"]
                    sub_invoice_data["DayOut"] = CIF["DayOut"]
                    invoices_data.append(sub_invoice_data)
        return invoices_data

    def get_all_users_data(self):
        users = self.users_collection.find()
        users_data = []
        for user in users:
            users_data.append(user)
        return users_data
