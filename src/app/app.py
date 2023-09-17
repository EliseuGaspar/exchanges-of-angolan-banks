from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_socketio import SocketIO


app = Flask(__name__)
ma = Marshmallow(app)
db = SQLAlchemy(app)
CORS(app)
app_io = SocketIO(app)
