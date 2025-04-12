class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BST:
    def __init__(self, node):
        self.Root = node


class aBST:
    def __init__(self, depth):
        tree_size = 2 ** (depth + 1) - 1
        self.Tree = [None] * tree_size

    def FindKeyIndex(self, key):
        currentIndex = 0
        while currentIndex < len(self.Tree):
            if self.Tree[currentIndex] is None:
                return -currentIndex

            if self.Tree[currentIndex] == key:
                return currentIndex

            if key < self.Tree[currentIndex]:
                currentIndex = 2 * currentIndex + 1
            else:
                currentIndex = 2 * currentIndex + 2

        return None

    def AddKey(self, key):
        searching_result = self.FindKeyIndex(key)
        if searching_result is None or searching_result >= 0:
            return -1
        current_index = -searching_result
        self.Tree[current_index] = key

        return current_index
