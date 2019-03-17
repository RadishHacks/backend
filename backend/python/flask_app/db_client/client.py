import pymongo

from flask_app.db_client.db_config import *

db_client = pymongo.MongoClient(DB_URL, DB_PORT)
db_core = db_client[DB_NAME]
db_images_col = db_core[DB_IMAGES_COL]
db_pairs_col = db_core[DB_PAIRS_COL]

def _prune(doc):
    doc.pop("_id", None)
    return doc

"""
Forwards query to images col.
If doc is null, then it's assumed to be empty.
"""
def query_images(doc=None, limit=None):
    if doc is None:
        doc = {}

    cursor = db_images_col.find(doc) if limit is None else db_images_col.find(doc).limit(limit)
    documents = []
    for data in cursor:
        documents.append(_prune(data))
    return documents


"""
Forwards query to pairs col.
If doc is null, then it's assumed to be empty.
TODO: Half this stuff needs to be in a config file.
"""
def query_pairs(doc=None, limit=0, ignore_list=set()):
    if doc is None:
        doc = {
            "_id": {
                "$nin": list(ignore_list)
            }
        }

    cursor = db_pairs_col.find(doc).limit(limit)
    documents = []
    for pair_data in cursor:
        a_img_data = query_images({"_id": pair_data["a_id"]}, 1)[0]
        b_img_data = query_images({"_id": pair_data["b_id"]}, 1)[0]
        documents.append({
            "a": {
                "url": a_img_data["url"],
                "votes": a_img_data["votes"],
                },
            "b": {
                "url": b_img_data["url"],
                "votes": b_img_data["votes"]
                },
            "meta": {
                "influencer": "no-id-yet",
                "tags": pair_data["tags"]
                }
            })
        ignore_list.add(pair_data["_id"])

    return documents

