import subprocess
import os
import tkinter.messagebox as msgbox
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient

# Check if pip is installed and update it
try:
    subprocess.check_output(["pip", "--version"])
    subprocess.call(["pip", "install", "--upgrade", "pip"])
except:
    command = "curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py"
    subprocess.call(command, shell=True)
    subprocess.call(["python", "get-pip.py"])
    os.remove("get-pip.py")
    subprocess.call(["pip", "install", "--upgrade", "pip"])

# Install required dependencies
subprocess.call(["pip", "install", "-r", "requirements.txt"])


load_dotenv(find_dotenv())
host = os.getenv("HOSTNAME")
client = MongoClient(host)


db_name = "HotelManagementDB"
if db_name in client.list_database_names():
    print("Database already exists")
    db = client[db_name]
else:
    db = client[db_name]
    print("Database created")


def import_user_data():
    with open("./Data/users.json", "r") as f:
        data = f.read()

    for element in eval(data):
        if element["Username"] not in db["users"].find({}).distinct("Username"):
            db["users"].insert_one(element)
    print("Imported user data successfully")



if "users" in db.list_collection_names():
    print("Collection 'users' already exists")
    import_user_data()
else:
    db.create_collection("users")
    print("Collection 'users' created")
    import_user_data()



def import_room_data():
    with open("./Data/rooms.json", "r") as f:
        data = f.read()

    for element in eval(data):
        if element["RoomID"] not in db["rooms"].find({}).distinct("RoomID"):
            db["rooms"].insert_one(element)
    print("Imported room data successfully")



if "rooms" in db.list_collection_names():
    print("Collection 'rooms' already exists")
    import_room_data()
else:
    db.create_collection("rooms")
    print("Collection 'rooms' created")
    import_room_data()

def import_invoice_data():
    with open("./Data/invoices.json", "r") as f:
        data = f.read()

    for element in eval(data):
        if element["InvoiceID"] not in db["invoices"].find({}).distinct("InvoiceID"):
            db["invoices"].insert_one(element)
    print("Imported invoice data successfully")

if "invoices" in db.list_collection_names():
    print("Collection 'invoices' already exists")
    import_invoice_data()
else:
    db.create_collection("invoices")
    print("Collection 'invoices' created")
    import_invoice_data()

msgbox.showinfo("Hotel Management", "Setup successfully! Hotel Management System is ready!")
