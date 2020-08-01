class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def append(self, item):
        self.storage.append(item)
        if len(self.storage)-1 == self.capacity:
            del self.storage[0]

    def get(self):
        return self.storage