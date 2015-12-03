import datetime

class Customer:
    def __init__(self, username, password):
        self.username = str(username)
        self.password = str(password)
    
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

    def __repr__(self):
        return '<Customer %r>' % (self.username)