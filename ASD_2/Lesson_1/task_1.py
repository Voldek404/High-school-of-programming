class SimpleTreeNode:
    def __init__(self, val, parent):

        self.NodeValue = val
        self.Parent = parent
        self.Children = []


class SimpleTree:
    def __init__(self, root):
        self.Root = root

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
