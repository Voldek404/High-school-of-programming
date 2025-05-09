class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []


class SimpleTree:
    def __init__(self, root):
        self.Root = root

    def EvenTrees(self):
        if self.Root is None:
            return None

        result_list = []

        def EvenTreesHelper(currentNode):
            subtree_size = 1
            for Node in currentNode.Children:
                subtree_size += EvenTreesHelper(Node)

            if (subtree_size - 1) % 2 == 0 and currentNode.Parent is not None:
                result_list.append(currentNode)
                result_list.append(Node)

            return subtree_size

        EvenTreesHelper(self.Root)

        return result_list
