class BSTNode:
    def __init__(self, key, parent):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.level = 0


class BalancedBST:
    def __init__(self):
        self.Root = None

    def GenerateTree(self, a):
        if not a:
            return None

        a.sort()

        def GenerateTreeHelper(a, left, right, parent, level):
            if left > right:
                return

            mid = (left + right) // 2
            currentNode = BSTNode(a[mid], parent)
            currentNode.level = level
            currentNode.LeftChild = GenerateTreeHelper(
                a, left, mid - 1, currentNode, level + 1
            )
            currentNode.RightChild = GenerateTreeHelper(
                a, mid + 1, right, currentNode, level + 1
            )
            return currentNode

        self.Root = GenerateTreeHelper(a, 0, len(a) - 1, None, 0)
        return self.Root

    def IsBalanced(self, root_node):
        root_node = self.Root
        if root_node is None:
            return True

        def IsBalancedHelper(currentNode):
            if currentNode is None:
                return 0

            left_height = IsBalancedHelper(currentNode.LeftChild)
            right_height = IsBalancedHelper(currentNode.RightChild)
            if abs(left_height - right_height) > 1:
                return -1

            return max(left_height, right_height) + 1

        return IsBalancedHelper(root_node) != -1
