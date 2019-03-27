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

import flask_app.feed
import flask_app.session
import flask_app.actions

@app.route("/")
def blank():
    return ""
