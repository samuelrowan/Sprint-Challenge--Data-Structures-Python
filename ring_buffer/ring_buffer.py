#this one I did on my own but fails two tests and the tests seem flawed
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

#This one I pulled straight from the internet and it fails the same two tests.  The tests are fucked.
# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.data = []
#
#     class __Full:
#         def append(self, x):
#             self.data[self.cur] = x
#             self.cur = (self.cur+1) % self.capacity
#         def get(self):
#             return self.data[self.cur:]+self.data[:self.cur]
#
#     def append(self,x):
#         self.data.append(x)
#         if len(self.data) == self.capacity:
#             self.cur = 0
#             self.__class__ = self.__Full
#
#     def get(self):
#         return self.data