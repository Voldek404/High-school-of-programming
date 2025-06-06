import ctypes


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError("Index is out of bounds")
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError("Index is out of bounds")
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        for j in range(self.count, i, -1):
            self.array[j] = self.array[j - 1]
        self.array[i] = itm
        self.count += 1

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError("Index is out of bounds")
        for j in range(i, self.count - 1):
            self.array[j] = self.array[j + 1]
        self.count -= 1
        if self.count < 0.5 * self.capacity:
            new_capacity = max(int(self.capacity / 1.5), 16)
            self.resize(new_capacity)

    def len(self):
        return self.count


class Deque:
    def __init__(self):
        self.deque = DynArray()
        self.deque_2 = DynArray()

    def addFront(self, item):
        self.deque.insert(0, item)

    def addTail(self, item):
        self.deque.append(item)

    def removeFront(self):
        if self.deque.len() == 0:
            return None
        result = self.deque[0]
        self.deque.delete(0)
        return result

    def removeTail(self):
        if self.deque.len() == 0:
            return None
        result = self.deque[self.deque.len() - 1]
        self.deque.delete(self.deque.len() - 1)
        return result

    def size(self):
        return self.deque.len()

    def dequeMinimum(self) -> int:
        if not self.deque_2:
            self.deque_2.append(self.deque[0])
        for i in range(1, self.size()):
            if self.deque[i] <= self.deque_2[len(self.deque_2) - 1]:
                self.deque_2.append(self.deque[i])
        for j in range(self.size(), 0, -1):
            if self.deque[j - 1] == self.deque_2[len(self.deque_2) - 1]:
                return self.deque[j - 1]

    def getMin(self):
        return self.deque_2[0] if self.deque_2 else None

    @staticmethod
    def bracketsBalance(string):
        matching_brackets = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in string:
            if i in matching_brackets:
                if not stack or stack[-1] != matching_brackets[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0


    def isPalindrome_helper(self, index):
        if self.size() == 0:
            return False
        if index == self.size() // 2:
            return True
        if self.deque[index] != self.deque[self.size() - index - 1]:
            return False
        return self.isPalindrome_helper(index + 1)


    def isPalindrome(self):
        return self.isPalindrome_helper(0)



