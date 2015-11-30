import datetime
from flask import url_for
from app import db


class Customer(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    #name = db.StringField(max_length=255, required=True)
    #adress = db.StringField(max_length=255, required=True)
    #organisationalNumber = db.StringField(max_length=255, required=True)
    #contactNumber = db.StringField(max_length=255, required=True)
    #industrialSector = db.StringField(max_length=255, required=True)
    #email= db.StringField(max_length=255, required=True)
    username= db.StringField(max_length=255, required=True)
    password= db.StringField(max_length=255, required=True)

    #meta = {'DB': "admin"}
    #meta = {"db_alias": "admin"}

    def __repr__(self):
        return '<Customer %r>' % (self.username)