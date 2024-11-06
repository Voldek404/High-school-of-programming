class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        return self.stack.pop()

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.size() > 0:
            return self.stack[-1]
        else:
            return None


def balanced_brackets(target_string: str, stack_new) -> bool:
    open_brackets = {'(', '[','{'}
    closed_brackets ={')': '(', ']': '[', '}': '{'}
    for i in target_string:
        if i in open_brackets:
            stack_new.push(i)
        elif i in closed_brackets:
            if stack_new.size() == 0 or stack_new.pop() != closed_brackets[i]:
                return False
    return stack_new.size() == 0
