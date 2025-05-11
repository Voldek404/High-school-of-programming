class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []


class SimpleTree:
    def __init__(self, root):
        self.Root = root

    def EvenTrees(self):
        if self.Root is None or len(self.Root.Children) == 0:
            return []

        result_list = []

        def EvenTreesHelper(currentNode):
            subtree_size = 1
            for child in currentNode.Children:
                size = EvenTreesHelper(child)
                if size % 2 == 0:
                    result_list.append(currentNode)
                    result_list.append(child)
                else:
                    subtree_size += size
            return subtree_size

        EvenTreesHelper(self.Root)
        return result_list

