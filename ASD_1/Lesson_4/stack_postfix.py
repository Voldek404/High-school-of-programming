class Stack:
    def __init__(self):
        self.stack = []
        self.operating_stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        return self.stack.pop() if self.size() > 0 else None

    def push(self, value):
        self.stack.append(value)
        self.evaluate_operations(value)

    def peek(self):
        return self.stack[-1] if self.size() > 0 else None

    def evaluate_operations(self, value):
        operations_dict = {"+": "+", "-": "-", "*": "*", "/": "/"}
        if isinstance(value, int):
            self.operating_stack.append(value)
        elif value in operations_dict:
            b = self.operating_stack.pop()
            a = self.operating_stack.pop()
            if  operations_dict[value] and b == 0:
                raise ZeroDivisionError
            self.operating_stack.append(eval(f"{a}{operations_dict[value]}{b}"))

    def get_result(self):
        return self.operating_stack[-1] if len(self.operating_stack) == 1 else None


