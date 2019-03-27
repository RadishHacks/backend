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
class Image(EmbeddedDocument):
    image_url = StringField()
    voter_ids = ListField(ObjectIdField())  # list of session_ids for now

class ImagePair(Document):
    images = ListField(EmbeddedDocumentField(Image), max_length=2)
    created_timestamp = DateTimeField(required=True, default=datetime.datetime.utcnow)
    tags = ListField(StringField())

    @classmethod
    def create_image_pair(cls, image_urls):
        img_a = Image(image_url=image_urls[0])
        img_b = Image(image_url=image_urls[1])
        return ImagePair(images=[img_a, img_b]).save()

    @classmethod
    def get_image_pairs(cls, count, offset):
        return ImagePair.objects[offset : count + offset]

    @classmethod
    def add_tags(cls, image_pair_id, tags=[]):
        if tags:
            ImagePair.objects(id=image_pair_id).update_one(push_all__tags=tags)

    @classmethod
    def add_vote(cls, image_pair_id, idx, voter_id):
        image_pair = ImagePair.objects(id=image_pair_id)
        if voter_id not in image_pair.images[idx]:
            image_pair.images[idx].voter_ids.append(voter_id)
            image_pair.save()
            return True
        return False

    @classmethod
    def _parse_image_data(cls, image_pairs):
        ret = []
        for ip in image_pairs:
            parsed_ip = ip.to_mongo().to_dict()
            for image in parsed_ip["images"]:
                image["vote_count"] = len(image["voter_ids"])
                del image["voter_ids"]
            ret.append(parsed_ip)
        return ret
