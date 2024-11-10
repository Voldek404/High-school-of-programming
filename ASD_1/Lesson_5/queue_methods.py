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

    def queueReverse_helper(self, counter, temp):
        if  self.size() == 0:
            while temp:
                self.enqueue(temp.pop(0))
            return self.queue
        temp.append(self.queue.pop())
        return self.queueReverse_helper(counter=counter + 1, temp = temp)

    def queueReverse(self):
        return self.queueReverse_helper(counter=0, temp=[])


qu = Queue()
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
qu.enqueue(4)
qu.enqueue(5)
print(qu.queueReverse())
while qu.size() > 0:
    print(qu.dequeue())
