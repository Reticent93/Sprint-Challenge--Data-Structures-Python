from collections import deque


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.cur = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)

        else:
            self.storage[self.cur] = item
            self.cur += 1
            if self.cur == self.capacity:
                self.cur = 0

    def get(self):
        return self.storage



