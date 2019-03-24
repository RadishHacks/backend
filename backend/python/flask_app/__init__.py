from flask import Flask
app = Flask(__name__)

import flask_app.feed
import flask_app.session
import flask_app.actions

@app.route("/")
def blank():
    return ""
