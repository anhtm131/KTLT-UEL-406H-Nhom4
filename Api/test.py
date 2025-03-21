import Api.Admin_Api as adminapi
data = {

        "RoomID": "P.501",
        "RoomType": "Standard",
        "Price": 1000000,
        "Status": "Cleaning"
}

api = adminapi.Admin_Api()
api.add_new_room(data)