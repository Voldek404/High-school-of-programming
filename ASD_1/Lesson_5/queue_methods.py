class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def queueRotation(self, number):
        number = number % self.size() if self.size > 0 else 0
        for _ in range(number):
            self.enqueue(self.dequeue())
        return None

    def queueReverse_helper(self, index):
        if index == self.size():
            return self.queue
        self.enqueue(self.queue.pop(- index - 1))
        return self.queueReverse_helper(index = index + 1)

    def queueReverse(self):
        return self.queueReverse_helper(index = 0)


qu = Queue()
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
qu.enqueue(4)
qu.enqueue(5)
print(qu.queueReverse())
while qu.size() > 0:
    print(qu.dequeue())
