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

    def collect_values(self, node):
        values = [node.NodeValue]
        for child in node.Children:
            values.extend(self.collect_values(child))
        return values

    def build_balanced_tree(self, values, parent=None):
        if not values:
            return None

        mid_index = len(values) // 2
        node = SimpleTreeNode(values[mid_index], parent)
        left = self.build_balanced_tree(values[:mid_index], node)
        right = self.build_balanced_tree(values[mid_index + 1:], node)

        if left:
            node.Children.append(left)
        if right:
            node.Children.append(right)
        return node

    def balance_even_tree(self):
        if self.Root is None:
            return
        values = self.collect_values(self.Root)
        values.sort()
        self.Root = self.build_balanced_tree(values)

    def count_even_subtrees(self, node):
        count = 0

        def dfs(current):
            nonlocal count
            size = 1
            for child in current.Children:
                size += dfs(child)
            if (size - 1) % 2 == 0 and current.Parent is not None:
                count += 1
            return size

        dfs(node)
        return count
