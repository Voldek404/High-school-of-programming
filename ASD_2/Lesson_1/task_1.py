class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []


class SimpleTree:
    def __init__(self, root, level):
        self.Root = root
        self.Level = level

    def updateSubtreeLevel(node, level):
        node.level = level
        for child in node.Children:
            updateSubtreeLevel(child, level + 1)

    def AddChild(self, ParentNode, NewChild):
        if self.Root is None:
            self.Root = NewChild
            return

        def AddChildHelper(currentNode):
            if currentNode == ParentNode:
                currentNode.Children.append(NewChild)
                NewChild.Parent = currentNode
                return
            for child in currentNode.Children:
                AddChildHelper(child)

        return AddChildHelper(self.Root)

    def DeleteNode(self, NodeToDelete):
        if self.Root is None:
            return
        if NodeToDelete == self.Root:
            self.Root = None
            return

        def DeleteNodeHelper(currentNode):
            for child in currentNode.Children:
                if child == NodeToDelete:
                    currentNode.Children.remove(child)
                else:
                    DeleteNodeHelper(child)

        return DeleteNodeHelper(self.Root)

    def GetAllNodes(self):
        if self.Root is None:
            return []

        def GetAllNodesHelper(currentNode, nodesList):
            nodesList.append(currentNode)
            if currentNode.Children:
                for child in currentNode.Children:
                    GetAllNodesHelper(child, nodesList)
            return nodesList

        return GetAllNodesHelper(self.Root, [])

    def FindNodesByValue(self, val):
        if self.Root is None:
            return []

        def FindNodesHelper(currentNode, nodesList):
            if currentNode.NodeValue == val:
                nodesList.append(currentNode)
            for child in currentNode.Children:
                FindNodesHelper(child, nodesList)
            return nodesList

        return FindNodesHelper(self.Root, [])

    def MoveNode(self, OriginalNode, NewParent):
        if self.Root is None:
            return

        def MoveNodeHelper(currentNode):
            for child in currentNode.Children:
                if child == OriginalNode:
                    NewParent.Children.append(OriginalNode)
                    OriginalNode.level = currentNode.Level + 1
                    updateSubtreeLevel(OriginalNode, OriginalNode.level)
                    OriginalNode.Parent = NewParent
                    currentNode.Children.remove(child)
                    break
                else:
                    MoveNodeHelper(child)

        return MoveNodeHelper(self.Root)

    def Count(self):
        if self.Root is None:
            return 0

        def CountHelper(currentNode):
            count = 1
            if currentNode.Children:
                for node in currentNode.Children:
                    count += CountHelper(node)
            return count

        return CountHelper(self.Root)

    def LeafCount(self):
        if self.Root is None:
            return 0

        def LeafCountHelper(currentNode):
            count = 0
            if not currentNode.Children:
                return 1
            for child in currentNode.Children:
                count += LeafCountHelper(child)
            return count

        return LeafCountHelper(self.Root)
    def NodesCensus(self):
        if self.Root is None:
            return None

        nodes_dict = {}

        def NodesCensusHelper(currentNode, level: int):
            nodes_dict[currentNode] = level
            for child in currentNode.Children:
                NodesCensusHelper(child, level + 1)

        NodesCensusHelper(self.Root, 0)
        return nodes_dict

    # Классы SimpleTreeNode и SimpleTree уже заданы выше

    # Создание узлов
root = SimpleTreeNode("root", None)
child1 = SimpleTreeNode("child1", None)
child2 = SimpleTreeNode("child2", None)
child3 = SimpleTreeNode("child3", None)
child4 = SimpleTreeNode("child4", None)

    # Создание дерева
tree = SimpleTree(root)

    # Добавление детей
tree.AddChild(root, child1)
tree.AddChild(root, child2)
tree.AddChild(child1, child3)
tree.AddChild(child1, child4)

    # Проверка GetAllNodes
all_nodes = tree.GetAllNodes()
print("All nodes in tree (before move):")
for node in all_nodes:
    print(f"Node: {node.NodeValue}, Parent: {node.Parent.NodeValue if node.Parent else None}")

    # Перемещение узла child3 под child2
tree.MoveNode(child1, child2)

    # Проверка GetAllNodes после перемещения
all_nodes_after_move = tree.GetAllNodes()
print("\nAll nodes in tree (after move):")
for node in all_nodes_after_move:
    print(f"Node: {node.NodeValue}, Parent: {node.Parent.NodeValue if node.Parent else None}")
dict_of_nodes = tree.NodesCensus()
for key, value in dict_of_nodes.items():
    print(f"{key}: {value}")