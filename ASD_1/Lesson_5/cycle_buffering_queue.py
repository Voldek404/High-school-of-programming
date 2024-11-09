class CycleQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
        else:
            self.queue[self.rear] = item
            self.rear = (self.rear + 1) % self.capacity
            self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            return self.queue[self.front]
