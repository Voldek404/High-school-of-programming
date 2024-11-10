class Stack:
    def __init__(self):
        self.stackIn = []
        self.stackOut = []

    def sizeOut(self):
        return len(self.stackOut)

    def sizeIn(self):
        return len(self.stackIn)

    def peek(self):
        if self.sizeOut() > 0:
            return self.stackOut[-1]
        elif self.sizeIn() > 0:
            return self.stackIn[0]
        else:
            return None

    def enqueue(self, item):
        self.stackIn.append(item)

    def dequeue(self):
        if self.sizeOut() == 0:
            while self.sizeIn() > 0:
                self.stackOut.append(self.stackIn.pop())
        if self.sizeOut() > 0:
            return self.stackOut.pop()
        else:
            return None
