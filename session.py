from mongoengine import *
import datetime
# TODO: Leo Liu
# connect(<name_of_database>)

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

    def create_session(self):
        return Session().save()

    def update_active_session(self, session_id):
        Session.objects(id=session_id).update_one(set__last_active_timestamp=datetime.datetime.utcnow())

    def update_voted_history(self, session_id, image_pair_id):
        Session.objects(id=session_id).update_one(push__image_pairs_voted=image_pair_id)
