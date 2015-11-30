from flask import Flask
#from flask.ext.mongoalchemy import MongoAlchemy
from flask.ext.mongoengine import MongoEngine
from mongoengine import connect
#, MongoEngineSessionInterface
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
#app.config.from_object('config')
#app.config['MONGOALCHEMY_DATABASE'] = 'library'
#db = MongoAlchemy(app)


#app.config['MONGODB_SETTINGS'] = {
#  'db': 'admin',
#   'host': '127.0.0.1',
#    'port': 27017
#}
#db = connect('app', host='mongodb://localhost/db')
#mongo.admin.authenticate("myUserAdmin", "abc123")

db = MongoEngine(app)


app.config["SECRET_KEY"] = "KeepThisS3cr3t"

# the toolbar is only enabled in debug mode:
app.debug = True
# set a 'SECRET_KEY' to enable the Flask session cookies
#app.config['SECRET_KEY'] = "KeepThisS3cr3t"
app.config["DEBUG_TB_PANELS"] = ["flask.ext.mongoengine.panels.MongoDebugPanel"]
toolbar = DebugToolbarExtension(app)


#app.session_interface = MongoEngineSessionInterface(db)

from app import views, models

