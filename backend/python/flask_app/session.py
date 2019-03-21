from bson.binary import Binary
import pickle
import time
import uuid

import flask_app.db_client.client as client
from flask_app.db_client.db_config import *

class Session:
    def __init__(self):
        self.session_id = uuid.uuid4()
        self.timestamp = time.time()
        self.image_pair_history = set()

    def update_image_pair_history(s):
        self.image_pair_history.union(s)

    def update_timestamp():
       self.timestamp = time.time()

def get_session(session_id=None):
    db_sessions_col = client.get_col(DB_SESSIONS_COL)
    if session_id is None:
        session = Session()
        client.insert_object(db_sessions_col, session.session_id, session)
        return session

    session = client.query_object(db_sessions_col, session_id)
    if session is None:
        session = Session()
        client.insert_object(db_sessions_col, session.session_id, session)
        return session
    return session

def save_session(session):
    db_sessions_col = client.get_col(DB_SESSIONS_COL)
    session.update_timestamp()

    client.insert_object(db_sessions_col, session.session_id,
            Binary(pickle.dumps(session)))

