from flask import Flask
import json
import datetime
from bson.objectid import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)

app = Flask(__name__)

app.json_encoder = JSONEncoder

from flask_app import *

@app.route("/")
def blank():
    return ""
