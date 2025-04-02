class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:
    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False


class BST:
    def __init__(self, node):
        self.Root = node

    def __init__(self, root):
        self.Root = root

#Занятие 2. Бинарные деревья поиска
    # Задание 1. Определить равно ли дерево дереву-параметру
    def isEqual(self, other_tree):
        if not self.Root and not other_tree.Root:
            return True

        if not self.Root or not other_tree.Root:
            return False

        def isEqualHelper(node1, node2):
            if not node1 and not node2:
                return True

            if not node1 or not node2:
                return False

            return (node1.NodeKey == node2.NodeKey and
                    node1.NodeValue == node2.NodeValue and
                    isEqualHelper(node1.LeftChild, node2.LeftChild) and
                    isEqualHelper(node1.RightChild, node2.RightChild))

        return _isEqualHelper(self.Root, other_tree.Root)

    # Задание 2. Добавьте метод, который находит все пути от корня к листьям, длина которых равна заданной величине.

    def PreorderDFS(self, currentNode, targetLength, currentPath, allPaths):
        currentNode = self.Root
        if not currentNode:
            return

        currentPath.append(currentNode)

        if not currentNode.LeftChild and not currentNode.RightChild:
            if len(currentPath) == targetLength:
                allPaths.append([node.NodeKey for node in currentPath])

        self.PreorderDFS(currentNode.LeftChild, targetLength, currentPath, allPaths)
        self.PreorderDFS(currentNode.RightChild, targetLength, currentPath, allPaths)

        currentPath.pop()

    def GetPathsPreorder(self, targetLength):
        allPaths = []
        self.PreorderDFS(self.Root, targetLength, [], allPaths)
        return allPaths

    # Задание 3. Добавьте метод, который находит все пути от корня к листьям, чтобы сумма значений узлов на этом пути была максимальной.

    def getMaxSumPaths(self, currentNode, currentPath, allPaths, currentSum):
        if currentNode is None:
            return

        currentPath.append(currentNode.NodeValue)
        currentSum += currentNode.NodeValue

        if not currentNode.LeftChild and not currentNode.RightChild:
            if currentSum > self.maxSum:
                self.maxSum = currentSum
                allPaths.clear()
                allPaths.append(list(currentPath))
            elif currentSum == self.maxSum:
                allPaths.append(list(currentPath))

        else:
            if currentNode.LeftChild:
                self.getMaxSumPaths(currentNode.LeftChild, currentPath, allPaths, currentSum)
            if currentNode.RightChild:
                self.getMaxSumPaths(currentNode.RightChild, currentPath, allPaths, currentSum)

        currentPath.pop()

    def GetMaxSumPaths(self):
        allPaths = []
        self.maxSum = 0
        self.getMaxSumPaths(self.Root, [], allPaths, 0)
        return allPaths

    # Задание 4. Проверить является ли дерево симметричным относительно корня

    def isMirrorTree(self):
        def isMirrorTreeHelper(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False

            return (node1.NodeKey == node2.NodeKey) and \
                isMirrorTreeHelper(node1.LeftChild, node2.RightChild) and \
                isMirrorTreeHelper(node1.RightChild, node2.LeftChild)

        if not self.Root:
            return True

        return isMirrorTreeHelper(self.Root.LeftChild, self.Root.RightChild)

# Сложность для всех методов O(V), где V - число узлов
# Сложность пространственная для всех методов O(H), где H - высота дерева
# Избранный для выполнения задач алгоритм - прямой обход, как позволяющий обойти все возможные пути следования.
