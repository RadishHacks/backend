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
