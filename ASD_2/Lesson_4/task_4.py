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
                return -currentIndex if currentIndex != 0 else -len(self.Tree)

            if self.Tree[currentIndex] == key:
                return currentIndex

            if key < self.Tree[currentIndex]:
                currentIndex = 2 * currentIndex + 1
            else:
                currentIndex = 2 * currentIndex + 2

        return None

    def AddKey(self, key):
        result = self.FindKeyIndex(key)

        if result is None:
            return -1

        if result >= 0:
            return result

        insertIndex = 0 if result == -len(self.Tree) else -result
        self.Tree[insertIndex] = key
        return insertIndex

