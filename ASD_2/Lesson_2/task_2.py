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

    def FindNodeByKey(self, key):
        self.result = BSTFind()
        currentNode = self.Root
        parent = None

        while currentNode:
            parent = currentNode

            if key == currentNode.NodeKey:
                self.result.Node = currentNode
                self.result.NodeHasKey = True
                return self.result

            if key < currentNode.NodeKey:
                self.result.ToLeft = True
                currentNode = currentNode.LeftChild
            else:
                self.result.ToLeft = False
                currentNode = currentNode.RightChild

        self.result.Node = parent
        return self.result

    def AddKeyValue(self, key, val):
        result = self.FindNodeByKey(key)
        if result.NodeHasKey:
            return False

        new_node = BSTNode(key, val, result.Node)

        if self.Root is None:
            self.Root = new_node
            return True

        if result.Node:
            if key < result.Node.NodeKey:
                result.Node.LeftChild = new_node
            else:
                result.Node.RightChild = new_node
            new_node.Parent = result.Node

        return True

    def FinMinMax(self, FromNode, FindMax):
        if FromNode:
            currentNode = FromNode
            while currentNode.RightChild if FindMax else currentNode.LeftChild:
                currentNode = currentNode.RightChild if FindMax else currentNode.LeftChild
            return currentNode
        else:
            return None

    def DeleteNodeByKey(self, key):
        result = self.FindNodeByKey(key)
        if not result.Node or not result.NodeHasKey:
            return False

        node_to_delete = result.Node
        parent = node_to_delete.Parent

        # 1. Узел не имеет детей
        if not node_to_delete.LeftChild and not node_to_delete.RightChild:
            if parent:
                if parent.LeftChild == node_to_delete:
                    parent.LeftChild = None
                else:
                    parent.RightChild = None
            else:
                self.Root = None

        # 2. Узел имеет только одного ребёнка
        elif not node_to_delete.LeftChild or not node_to_delete.RightChild:
            child = node_to_delete.LeftChild if node_to_delete.LeftChild else node_to_delete.RightChild

            if parent:
                if parent.LeftChild == node_to_delete:
                    parent.LeftChild = child
                else:
                    parent.RightChild = child
            else:
                self.Root = child  # Если удаляем корень, делаем ребёнка новым корнем
            child.Parent = parent

        # 3. Узел имеет двух детей
        else:
            successor = self.FinMinMax(node_to_delete.RightChild, False)  # Минимальный узел в правом поддереве

            node_to_delete.NodeKey = successor.NodeKey
            node_to_delete.NodeValue = successor.NodeValue

            # Если successor имеет правого ребенка, корректируем ссылки
            if successor.Parent.LeftChild == successor:
                successor.Parent.LeftChild = successor.RightChild
            else:
                successor.Parent.RightChild = successor.RightChild

            if successor.RightChild:
                successor.RightChild.Parent = successor.Parent

        return True

    def Count(self):
        if not self.Root:
            return 0

        def CountHelper(currentNode):
            if currentNode is None:
                return 0
            return 1 + CountHelper(currentNode.LeftChild) + CountHelper(currentNode.RightChild)

        return CountHelper(self.Root)








