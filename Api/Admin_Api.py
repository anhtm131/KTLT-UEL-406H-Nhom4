import Api.Main_Api as main_api
import datetime

class Admin_Api(main_api.Main_Api):

    def __init__(self):
        super().__init__()
        self.connect_mongodb()

    def add_new_room(self, data):
        room = self.rooms_collection.find_one({'RoomID':data["RoomID"]})
        if room :
            return -1 #Error: room already exist
        if len(data) != 4:
            return -2 #Error: information isn't complete
        self.rooms_collection.insert_one(data)
        return 0 #create successfully

    def update_room(self, data, room_id):
        room = self.rooms_collection.find_one({'RoomID': room_id})
        if not room:
            return -1  # Error: can not find RoomID in database
        else:
            updated_fields = {} #create update field
            _id = room['_id'] # documentID
            if 'RoomType' in data != room['RoomType']:
                updated_fields['RoomType'] = data['RoomType']
            if 'Price' in data != room['Price']:
                updated_fields['Price'] = data['Price']
            if 'Status' in data != room['Status']:
                updated_fields['Status'] = data['Status']

            if updated_fields:
                self.rooms_collection.update_one({'_id': _id}, {'$set': updated_fields})
                return 0 #update successfully
            else:
                return -1 #Error: no new information was updated

    def remove_room(self, room_id):
        room = self.rooms_collection.find_one({'RoomID' : room_id})
        if not room:
            return -1 # Error: can not find room in database
        else:
            _id = room['_id']
            self.rooms_collection.delete_one({'_id': _id})
            return 0 #remove sucessfully
    def add_new_user(self,data):
        user = self.users_collection.find_one({'Username':data['Username']})
        if user:
            return -1 #Error: User already exist in database
        else:
            self.users_collection.insert_one(data)
            return 0 #add successfully
    def update_user(self,data):
        user = self.users_collection.find_one({'Username': data['Username']})
        if not user:
            return -1 #can't find user in database
        else:
            _id = user['_id']
            updated_fields = {}
            if 'Password' in data != user['Password']:
                updated_fields['Password'] = data['Password']
            if 'Role' in data != user['Role']:
                updated_fields['Role'] = data['Role']
            if updated_fields:
                self.users_collection.update_one({'_id': _id}, {'$set': updated_fields})
                return 0 #update successfully
            else:
                return -1 #Error: no new information was updated
    def remove_user(self,data):
        user = self.users_collection.find_one({'Username' : data['Username']})
        if not user:
            return -1 # Error: can not find user in database
        else:
            _id = user['_id']
            self.users_collection.delete_one({'_id': _id})
            return 0 #remove sucessfully


    def search_revenue(self, data):
        if data["From"] == "" or data["To"] == "":
            return -1 #Error: data is empty
        try:
            from_date = datetime.datetime.strptime(data["From"], "%d/%m/%Y")
            to_date = datetime.datetime.strptime(data["To"], "%d/%m/%Y")
        except ValueError:
            return -2 #Erorr: Value error
        invoices_cursor = self.invoices_collection.find().sort("Invoice_Date", 1)
        filtered_invoices = []
        for invoice in invoices_cursor:
            inv_date = invoice["Invoice_Date"]
            if from_date <= inv_date <= to_date:
                filtered_invoices.append(invoice)
        return filtered_invoices

    def update_price(self,data):
        room = self.rooms_collection.find_one({"RoomType" : data["RoomType"]}, {"Price" : 1})
        if room["Price"] == data["Price"]:
            return -1 #Error: No change was made
        self.rooms_collection.update_many({"RoomType": data["RoomType"]},{"$set":{"Price":data["Price"]}})
        return 0 #update successfully




