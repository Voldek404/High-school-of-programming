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

    def queueReverse(self):
        temp_list = []
        for i in range(self.size()):
            temp_list.append(self.dequeue())
        for item in reversed(temp_list):
            self.enqueue(item)
        return self.queue
