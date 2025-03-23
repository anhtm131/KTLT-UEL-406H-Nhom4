import Api.Main_Api as main_api


class Admin_Api(main_api.Api):

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
            self.users_collection.update_one(data)
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





