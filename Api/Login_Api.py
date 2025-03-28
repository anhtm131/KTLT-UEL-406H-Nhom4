import Api.Main_Api as main_api


class Login_Api(main_api.Main_Api):

    def __init__(self):
        super().__init__()
        self.connect_mongodb()

    # user login api
    def check_login(self, username, password):
        if username == "" or password == "":
            return -1 #username or password is empty
        user = self.users_collection.find_one({"Username": username})
        if user == None:
            return -2 #user not found
        elif password != user["Password"] :
            return -3 #wrong password
        return user["Role"]