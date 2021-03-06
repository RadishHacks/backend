#!/usr/bin/python
from mongoengine import *
from ..db_client.image_pair import ImagePair


# DB_NAME parameter is complete useless as it uses same param as ImagePair file
# TODO: refactor so we don't replace abswap all the time
DB_NAME="abswap-dev"
S3_HOST="https://s3.us-east-2.amazonaws.com/abswap-images/"
db = connect(DB_NAME)
db.drop_database(DB_NAME)

BEE_FOLDER = "bee_memes/"
BEE_IMGS = ["5960918e9f202.jpeg", "862.jpg", "86c.png", "9a5.jpg", "e56.jpeg",
    "hqdefault.jpg", "images.jpeg", "maxresdefault.jpg",
    "the-emg-bee-movie-1-movie-of-2018-29979282.png",
    "tumblr_mej0eunZtM1ql3loeo1_500.png"]

imgs = [S3_HOST + BEE_FOLDER + img_link for img_link in BEE_IMGS]

for idx in range(int(len(imgs)/2)):
    ImagePair.create_image_pair([imgs[idx], imgs[idx+1]])
