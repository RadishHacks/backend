import time
import uuid

class Session:
    def __init__(self, feed_request_size=10):
        self.session_id = uuid.uuid4()
        
        # TODO
        #self.feed_request_size = feed_request_size
        
        self.timestamp = time.time()

        self.image_pair_history = set()

    def update_image_pair_history(s):
        self.image_pair_history.union(s)

    def update_timestamp():
       self.timestamp = time.time()

