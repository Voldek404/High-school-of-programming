class Stack:
    def __init__(self):
        self.stack = []
        self.sum_of_values = 0

    def size(self):
        return len(self.stack)

    def pop(self):
        value = self.stack.pop()
        sum_of_values -= value
        return value

    def push(self, value):
        self.stack.append(value)
        self.sum_of_values += value

    def peek(self):
        if self.size() > 0:
            return self.stack[-1]
        else:
            return None

    def average(self):
        return self.sum_of_values / self.size()
