from flask import request, make_response, jsonify
from flask_app import app
from flask_app.db_client.session import Session

@app.route("/session", methods=["POST"])
def new_session():
    session = Session.create_session()
    results = {
        "session_id": session.id
    }
    return make_response(jsonify(results), 200)

@app.route("/session/update", methods=["POST"])
def update_session():
    if request.is_json is not True:
        return make_response(jsonify({"error": "include application/json in header"}), 400)

    body = request.get_json()
    if "session_id" not in body:
        return make_response(jsonify({"error": "include session_id to update session"}), 400)

    session_id = body["session_id"]

    Session.update_active_session(session_id)
    return make_response(jsonify({"success": True}), 200)
