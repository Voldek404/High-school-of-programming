class BSTNode:
    def __init__(self, key, val, parent):
        self.Nodekey = key
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

    def FindNodeByKey(self, key):
        self.result = BSTFind()
        if self.Root is None:
            return None

        def FindNodeByKeyHelper(currentNode, key):
            if currentNode is None:
                return self.result

            if currentNode.key == key:
                self.result.Node = currentNode
                self.result.NodeHasKey = True
                self.result.ToLeft = False

            if currentNode.key < key:
                return FindNodeByKeyHelper(currentNode.RightChild, key)

            return FindNodeByKeyHelper(currentNode.LeftChild, key)

        FindNodeByKeyHelper(self.Root, key)

        return self.result

    def AddKeyValue(self, key, val):
        self.FindNodeByKey(key)
        if self.result.node and self.result.nodehaskey:
            return False

        new_node = BSTNode(self, key, val, self.result.Node)
        if not self.Root:
            self.Root = new_node
        elif self.result.Node.key < key:
            self.result.Node.LeftChild = new_node
        else:
            self.result.Node.RightChild = new_node

        return True

    def FinMinMax(self, FromNode, FindMax):
        if not self.Root:
            return None

        self.Min = BSTNode()
        self.Max = BSTNode()

        def FinMinMaxHelper(currentNodeMin, currentNodeMax):
            if currentNodeMin.LeftChild:
                currentNodeMin = currentNodeMin.LeftChild
            else:
                self.Min = currentNodeMin

            if currentNodeMax.RightChild:
                currentNodeMax = currentNodeMax.RightChild
            else:
                self.Max = currentNodeMax
            FinMinMaxHelper(self.FromNode, self.FromNode)

        return self.Max, self.Max

    def DeleteNodeByKey(self, key):
        self.FindNodeByKey(key)
        if not self.result.node and not self.result.nodehaskey:
            return False
        if self.result.node.LeftChild is None and self.result.node.RightChild is None:
            self.result.node = None


        return DeleteNodeByKeyHelper(self.Root)


    def Count(self):
        if not self.Root:
            return 0

        def CountHelper(currentNode):
            if not currentNode:
                return 0
            count = 1
            count += CountHelper(currentNode.LeftChild)
            count += CountHelper(currentNode.RightChild)
            return count

        return CountHelper(self.Root)

