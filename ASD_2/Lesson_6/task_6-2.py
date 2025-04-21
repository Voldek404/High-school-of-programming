class BSTNode:
    def __init__(self, key, parent):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.level = 0


class BalancesBST:
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
                return

            left_height = IsBalancedHelper(currentNode.LeftChild)
            right_height = IsBalancedHelper(currentNode.RightChild)
            if abs(left_height - right_height) > 1:
                return -1

            return max(left_height, right_height) + 1

        return IsBalancedHelper(root_node) != -1

        # 2.* Добавьте метод проверки, действительно ли дерево получилось правильным: для каждого узла ключ левого потомка должен быть меньше его ключа,
        # а ключ правого потомка должен быть больше или равен ключу родителя.
        # Метод рекурсивно обходит поддеревья, вылетая если хотя бы один раз заданное условие сравнения величин ключей не совпадет. О(n) - tima and space complexity

    def IsBalancedWithKeys(self, root_node):
        root_node = self.Root
        if root_node is None:
            return 0

        def IsBalancedWithKeysHelper(currentNode):
            if currentNode is None:
                return True

            if (
                currentNode.LeftChild
                and currentNode.LeftChild.NodeKey >= currentNode.NodeKey
            ):
                return False

            if (
                currentNode.RightChild
                and currentNode.RightChild.NodeKey <= currentNode.NodeKey
            ):
                return False

            left_node = IsBalancedWithKeysHelper(currentNode.LeftChild)
            right_node = IsBalancedWithKeysHelper(currentNode.RightChild)

            return left_node and right_node

        return IsBalancedWithKeysHelper(root_node)

        # 3.* Добавьте метод проверки, действительно ли дерево получилось сбалансированным, что определяется тремя правилами:
        # - правое поддерево каждого узла сбалансировано;
        # - левое поддерево каждого узла сбалансировано;
        # - разница между глубинами левого и правого поддеревьев не превышает единицы (или, проще говоря, левое и правое поддеревья равны по длинами или отличаются не более чем на одну ветку).
        # O(n) - time and space complexity . даже не смотря на троекратный рекурсивный обход по сумме трех используемых методов

    def CheckTreeOnThreeRules(self, root_node):
        if self.Root is None:
            return True

        root_node = self.Root
        left_subtree_is_balanced = self.IsBalancedWithKeys(root_node.LeftChild)
        right_subtree_is_balanced = self.IsBalancedWithKeys(root_node.RightChild)
        height_is_balanced = self.IsBalanced(root_node)
        return (
            left_subtree_is_balanced
            and right_subtree_is_balanced
            and height_is_balanced
        )
