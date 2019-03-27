from flask import request, make_response, jsonify
from bson import json_util

from flask_app import app
from flask_app.db_client.image_pair import ImagePair
from flask_app.db_client.session import Session

"""
Vote image pair function
"""
@app.route("/image_pair/vote", methods=["POST"])
def vote_image_pair():
    if request.is_json is not True:
        return make_response(jsonify({"error": "include application/json in header"}), 400)

    body = request.get_json()
    if "session_id" not in body:
        return make_response(jsonify({"error": "include session_id for vote"}), 400)
    elif "image_pair_id" not in body:
        return make_response(jsonify({"error": "include image_pair_id for vote"}), 400)
    elif "image_idx" not in body:
        return make_response(jsonify({"error": "include image_idx for vote"}), 400)
    
    session_id = body["session_id"]
    image_pair_id = body["image_pair_id"]
    image_idx = body["image_idx"]

    if ImagePair.add_vote(image_pair_id, image_idx, session_id):
        Session.update_voted_history(session_id, image_pair_id)
        return make_response(jsonify({"success": True}), 200)
    else:
        reutnr make_response(jsonify({"error": "user has already voted"}), 400)
