from mongoengine import *
from flask_app.db_client.db_config import *
connect(DB_NAME, host=DB_URL, port=DB_PORT)

import datetime

""" JSON example
{
    _id: <ObjectId>,
    images: [{
        image_url: "https://www.example.com/image_a.png",
        voter_ids: [<ObjectId>]
    }, {
        image_url: "https://www.example.com/image_b.png",
        voter_ids: [<ObjectId>]
    }]
    created_timestamp: "2019-03-23 04:58:38.941306",
    tags: ["fashion", "streetwear"]
}
"""
class ImagePair(Document):
    class Image(EmbeddedDocument):
        image_url = StringField()
        voter_ids = ListField(ObjectIdField())  # list of session_ids for now

    images = ListField(EmbeddedDocumentField(Image), max_length=2)
    created_timestamp = DateTimeField(required=True, default=datetime.datetime.utcnow)
    tags = ListField(StringField())

    def create_image_pair(self, image_urls):
        img_a = Image(image_url=image_urls[0])
        img_b = Image(image_url=image_urls[1])
        return ImagePair(images=[img_a, img_b]).save()

    def add_tags(self, image_pair_id, tags=[]):
        if tags:
            ImagePair.objects(id=image_pair_id).update_one(push_all__tags=tags)

    def add_vote(self, image_pair_id, idx, voter_id):
        image_pair = ImagePair.objects(id=image_pair_id)
        image_pair.images[idx].voter_ids.append(voter_id)
        image_pair.save()
