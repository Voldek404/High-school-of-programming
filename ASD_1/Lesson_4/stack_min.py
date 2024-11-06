class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value

    def push(self, value):
        self.stack.append(value)
        if len(self.min_stack) == 0 or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def peek(self):
        if self.size() > 0:
            return self.stack[-1]
        else:
            return None

    def show_minimum(self):
        return self.min_stack[-1]
