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
        if self.Tree[0] is None:
            return None

        currentIndex = 0
        while currentIndex < len(self.Tree) and self.Tree[currentIndex] is not None:
            if key == self.Tree[currentIndex]:
                return currentIndex

            if key < self.Tree[currentIndex]:
                currentIndex = 2 * currentIndex + 1
            else:
                currentIndex = 2 * currentIndex + 2

        return None

    def AddKey(self, key):
        searching_result = self.FindKeyIndex(key)
        if self.Tree[0] is None:
            self.Tree[0] = key
            return 0

        if searching_result is not None:
            return -1

        currentIndex = 0
        while currentIndex < len(self.Tree):
            if self.Tree[currentIndex] is None:
                self.Tree[currentIndex] = key
                break

            if key < self.Tree[currentIndex]:
                currentIndex = 2 * currentIndex + 1
            else:
                currentIndex = 2 * currentIndex + 2

        return self.Tree.index(key)
