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
            return -0

        currentIndex = 0
        while currentIndex < len(self.Tree):
            if self.Tree[currentIndex] == key:
                return currentIndex

            if self.Tree[currentIndex] is None:
                return -currentIndex

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
# Задача 4.2* Найти наименьшего общего предка. В данном случае поиск производится с помощью правил нахождения индексов родителя.
# Исходя из итеративного подхода с использованием индексов space complexity будет ниже, чем при использовании рекурсии, требующей больше затрат при обходе
    def LCAFind(self, node_1_index, node_2_index):
        if node_1_index == node_2_index:
            return (node_1_index - 1) // 2

        currentIndex = node_1_index
        parents_list = set()

        while currentIndex != 0:
            parents_list.add((currentIndex - 1) // 2)
            currentIndex = (currentIndex - 1) // 2
        currentIndex = (node_2_index - 1) // 2

        while currentIndex != 0:
            if currentIndex in parents_list:
                return currentIndex
            currentIndex = (currentIndex - 1) // 2

        return None

