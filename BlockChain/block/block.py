import hashlib
from data.tag1 import WithdrawalRecord
from data.tag2 import Storage
from data.tag3 import Transportation


class Block:

    def __init__(self, index, timestamp, previous_hash, data):
        self.index = index
        self.data = data
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = hashlib.sha256((str(self.index) + str(self.timestamp) + self.data.__str__() + self.previous_hash).encode()).hexdigest()

    def __str__(self):
        return self.data.__str__() + " = " + self.hash
