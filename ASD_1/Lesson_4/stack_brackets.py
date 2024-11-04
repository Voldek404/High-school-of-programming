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
    for i in range(len(target_string)):
        if target_string[i] == '(':
            stack_new.push(target_string[i])
        elif target_string[i] == ')' and stack_new.peek() == '(':
            stack_new.pop()
        elif target_string[i] == ')':
            return False
    if len(stack_new.stack) == 0:
        return True
    else:
        return False


target_string ='()()'
stack_new = Stack()
print(balanced_brackets(target_string, stack_new))
