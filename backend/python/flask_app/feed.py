from flask import request
import json

from flask_app import app
import flask_app.db_client.client as client

"""
Anonymous feed query function.
"""
@app.route("/feed", methods=["GET"])
def get_feed():
    limit = request.args.get("size", default=1, type=int)
    return json.dumps(client.query_images(None, limit))

