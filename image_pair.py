from mongoengine import *
import datetime
# TODO: Leo Liu
# connect(<name_of_database>)

""" JSON example
{
    _id: <ObjectId>,
    image_a: {
        image_url: "https://www.example.com/image_a.png",
        voter_ids: [<ObjectId>]
    }
    image_b: {
        image_url: "https://www.example.com/image_b.png",
        voter_ids: [<ObjectId>]
    }
    created_timestamp: "2019-03-23 04:58:38.941306",
    tags: ["fashion", "streetwear"]
}
"""
class ImagePair(Document):
    class Image(EmbeddedDocument):
        image_url = StringField()
        voter_ids = ListField(ObjectIdField())  # list of session_ids for now

    image_a = EmbeddedDocumentField(Image)
    image_b = EmbeddedDocumentField(Image)
    created_timestamp = DateTimeField(required=True, default=datetime.datetime.utcnow)
    tags = ListField(StringField())
