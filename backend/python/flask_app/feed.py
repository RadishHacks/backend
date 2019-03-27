from flask import request, make_response, jsonify
from bson import json_util

from flask_app import app
from flask_app.db_client.image_pair import ImagePair

"""
Feed query function.
"""
@app.route("/feed", methods=["GET"])
def get_feed():
    count = 5 if "count" not in request.args else int(request.args.get("count"))
    offset = 0 if "offset" not in request.args else int(request.args.get("offset"))

    if count < 1 or count > 20:
        return make_response(jsonify({"error": "invalid count"}), 400)
    if offset < 0:
        return make_response(jsonify({"error": "invalid offset"}), 400)

    # TODO: add sessions eventually for unique images feed
    image_pairs = ImagePair.get_image_pairs(count, offset)
    parsed_image_pairs = ImagePair._parse_image_data(image_pairs)
    return make_response(jsonify({"image_pairs": image_pairs}), 200)
