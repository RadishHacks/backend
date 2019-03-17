from flask import abort, request
import json

from flask_app import app, session_keys
import flask_app.db_client.client as client
from flask_app.session import Session


"""
Feed query function.
Returns new session UUID if none are passed in.
"""
@app.route("/feed", methods=["POST"])
def get_feed():
    if request.is_json is not True:
        abort(405)
    body = request.get_json()

    feed_size = 1 if "size" not in body else body["size"]
    if "session_id" not in body or body["session_id"] not in session_keys:
        curr_session = Session(feed_request_size=feed_size)
        session_keys[str(curr_session.session_id)] = curr_session
    else:
        curr_session = session_keys[body["session_id"]]

    response_body = {
            "session_id": str(curr_session.session_id),
            "feed": client.query_pairs(None, feed_size, curr_session.image_pair_history)
            }

    return app.response_class(
            response=json.dumps(response_body),
            status=200,
            mimetype="application/json"
            )

