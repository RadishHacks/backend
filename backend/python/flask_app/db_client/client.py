import pymongo

from flask_app.db_client.db_config import *

db_client = pymongo.MongoClient(DB_URL, DB_PORT)
db_core = db_client[DB_NAME]
db_images_col = db_core[DB_IMAGES_COL]


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

