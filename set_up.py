import subprocess
import os

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

from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import ctypes

# Load environment variables
load_dotenv(find_dotenv())
host = os.getenv("HOSTNAME")
client = MongoClient(host)

# Check if the database exists, otherwise create it
db_name = "HotelManagementDB"
if db_name in client.list_database_names():
    print("Database already exists")
    db = client[db_name]
else:
    db = client[db_name]
    print("Database created")


# Function to import user data
def import_user_data():
    with open("./Data/users.json", "r") as f:
        data = f.read()

    for element in eval(data):
        if element["Username"] not in db["users.json"].find({}).distinct("Username"):
            db["users.json"].insert_one(element)
    print("Imported user data successfully")


# Check if 'users.json' collection exists
if "users.json" in db.list_collection_names():
    print("Collection 'users.json' already exists")
    import_user_data()
else:
    db.create_collection("users.json")
    print("Collection 'users.json' created")
    import_user_data()


# Function to import room data
def import_room_data():
    with open("./Data/rooms.json", "r") as f:
        data = f.read()

    for element in eval(data):
        if element["Room_ID"] not in db["rooms.json"].find({}).distinct("Room_ID"):
            db["rooms.json"].insert_one(element)
    print("Imported room data successfully")


# Check if 'rooms.json' collection exists
if "rooms.json" in db.list_collection_names():
    print("Collection 'rooms.json' already exists")
    import_room_data()
else:
    db.create_collection("rooms.json")
    print("Collection 'rooms.json' created")
    import_room_data()


# Function to import invoice data
def import_invoice_data():
    with open("./Data/invoices.json", "r") as f:
        data = f.read()

    for element in eval(data):
        if element["Invoice_ID"] not in db["invoices.json"].find({}).distinct("Invoice_ID"):
            db["invoices.json"].insert_one(element)
    print("Imported invoice data successfully")


# Check if 'invoices.json' collection exists
if "invoices.json" in db.list_collection_names():
    print("Collection 'invoices.json' already exists")
    import_invoice_data()
else:
    db.create_collection("invoices.json")
    print("Collection 'invoices.json' created")
    import_invoice_data()

# Show a setup completion message
ctypes.windll.user32.MessageBoxW(0, "Setup successfully! Hotel Management System is ready!", "Hotel Management", 1)
