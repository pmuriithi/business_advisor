import datetime

import json

class Object:
    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class Customer:
    def __init__(self, username, password):
        self.username =username
        self.password = password

    def displayCustomer(self):
        print("Username : ", self.username,  ", Password: ", self.password)

   #__collection__='customer-db'
    #created_at = DateTimeField(default=datetime.datetime.now, required=True)
    #name = db.StringField(max_length=255, required=True)
    #adress = db.StringField(max_length=255, required=True)
    #organisationalNumber = db.StringField(max_length=255, required=True)
    #contactNumber = db.StringField(max_length=255, required=True)
    #industrialSector = db.StringField(max_length=255, required=True)
    #email= db.StringField(max_length=255, required=True)

    #meta = {'DB': "admin"}
    #meta = {"db_alias": "admin"}
    #meta = {'collection': "customer-db"}
