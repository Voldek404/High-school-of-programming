class CycleQueue:
    def init(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rare = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
        front_item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        if self.is_empty():
            self.queue[self.rear] = item
            self.rear = (self.rear + 1) % self.capacity
            self.size += 1
            return
        self.enqueue(item)
        self.queue[self.rear] = front_item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        if not self.is_empty():
            return self.dequeue()
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            return self.queue[self.front]
