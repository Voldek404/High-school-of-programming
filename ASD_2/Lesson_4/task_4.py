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
            if key == self.Tree[currentIndex].NodeKey:
                return currentIndex

            if key < self.Tree[currentIndex].NodeKey:
                currentIndex = 2 * currentIndex + 1
            else:
                currentIndex = 2 * currentIndex + 2

        return None

    def AddKey(self, key):
        return -1
