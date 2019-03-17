from flask_app import app
from flask import request

@app.route("/feed", methods=["GET"])
def get_feed():
    return str(request.args.get("size", default=1, type=int))


