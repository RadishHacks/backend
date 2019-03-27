from mongoengine import *
from flask_app.db_client.db_config import *
connect(DB_NAME, host=DB_URL, port=DB_PORT)

import datetime

""" JSON example
{
    _id: <ObjectId>,
    last_active_timestamp: "2019-03-23 04:58:38.941306",
    created_timestamp: "2019-03-23 04:58:38.941306",
    image_pairs_voted: [<ObjectId>]
}
"""
class Session(Document):
    last_active_timestamp = DateTimeField(required=True, default=datetime.datetime.utcnow)
    created_timestamp = DateTimeField(required=True, default=datetime.datetime.utcnow)
    image_pairs_voted = ListField(ObjectIdField())

    @classmethod
    def create_session(cls):
        return Session().save()

    @classmethod
    def update_active_session(cls, session_id):
        Session.objects(id=session_id).update_one(set__last_active_timestamp=datetime.datetime.utcnow())

    @classmethod
    def update_voted_history(cls, session_id, image_pair_id):
        Session.objects(id=session_id).update_one(push__image_pairs_voted=image_pair_id)
