class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.counter = 0

    def append(self, item):
        if self.counter <self.capacity:
            self.data.append(item)
        else:
            self.data[self.counter % self.capacity] = item
        self.counter +=1

    def get(self):
        return self.data