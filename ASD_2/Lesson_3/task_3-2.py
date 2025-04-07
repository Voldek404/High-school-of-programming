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

    def FindNodeByKeyInvert(self, key):
        self.result = BSTFind()
        currentNode = self.Root
        parent = None

        while currentNode:
            parent = currentNode

            if key == currentNode.NodeKey:
                self.result.Node = currentNode
                self.result.NodeHasKey = True
                return self.result

            if key > currentNode.NodeKey:
                self.result.ToLeft = True
                currentNode = currentNode.RightChild
            else:
                self.result.ToLeft = False
                currentNode = currentNode.LeftChild

        self.result.Node = parent
        return self.result

    def AddKeyValueInvert(self, key, val):
        result = self.FindNodeByKey(key)
        if result.NodeHasKey:
            return False

        new_node = BSTNode(key, val, result.Node)

        if self.Root is None:
            self.Root = new_node
            return True

        if result.Node:
            if key > result.Node.NodeKey:
                result.Node.RightChild = new_node
            else:
                result.Node.LeftChild = new_node
            new_node.Parent = result.Node

        return True

    # 3.3* Реализация алгоритма инверсии дерева. Реализован через модификацию базового метода добавления ключа с его поиском
    #
    def TreeInvert(self):
        if self.Root is None:
            return None
        twin_tree = BST(None)

        def TreeInvertHelper(currentNode):
            if currentNode is None:
                return

            twin_tree.AddKeyValueInvert(currentNode.NodeKey, currentNode.NodeValue)

            TreeInvertHelper(currentNode.RightChild)
            TreeInvertHelper(currentNode.LeftChild)

        TreeInvertHelper(self.Root)
        return twin_tree

    def Count(self):
        if not self.Root:
            return 0

        def CountHelper(currentNode):
            if currentNode is None:
                return 0
            return (
                1
                + CountHelper(currentNode.LeftChild)
                + CountHelper(currentNode.RightChild)
            )

        return CountHelper(self.Root)

    def WideDeepAllNodes(self) -> tuple:
        if self.Root is None:
            return None

        levels = self.BSTHeight()
        nodes_to_levels = [[] for _ in range(levels)]

        def WideDeepAllNodesHelper(currentNode, currentLevel):
            if currentNode is None:
                return

            nodes_to_levels[currentLevel].append(
                currentNode.NodeValue
            )  # Изменен подход с NodeKey -> NodeValue

            WideDeepAllNodesHelper(currentNode.LeftChild, currentLevel + 1)
            WideDeepAllNodesHelper(currentNode.RightChild, currentLevel + 1)

        WideDeepAllNodesHelper(self.Root, 0)
        return tuple(nodes_to_levels)

    # 3.4* Найти уровень дерева с максимальной суммой значений нод. Задача решена с помощью обхода в ширину и модификации метода обхода в ширину через добавление
    # в итоговый кортеж значений нод
    # Сложность и по памяти, и по времени О(V) ввиду того, что обходится все дерево поэлементно.
    def MaximumLevel(self):
        levels = self.WideDeepAllNodes()
        sums_on_each_level = [sum(level) for level in levels]
        return sums_on_each_level.index(max(sums_on_each_level)) + 1

    # 3.5* Time and space complexity = O(V). Благодаря наличию pre и in обходов легко восстановить корень дерева и левое с правым поддеревом.
    # Хотя, зная, что у нас BST, можно было через стандартный метод AddKeyValue и основному правилу распределения узлов в BST распределелить все ноды до искомого дерева сбалансированного
    def TreeRestor(self, pre_fix_list, in_fix_list):
        def TreeRestorHelper(pre_fix_list, in_fix_list):
            if not pre_fix_list or not in_fix_list:
                return None

            root_value = pre_fix_list[0]
            root = BSTNode(root_value)
            root_index = in_fix_list.index(root_value)
            left_infix = in_fix_list[:root_index]
            right_infix = in_fix_list[root_index + 1 :]
            left_prefix = pre_fix_list[1 : 1 + len(left_infix)]
            right_prefix = pre_fix_list[1 + len(left_infix) :]
            root.LeftChild = TreeRestorHelper(left_prefix, left_infix)
            root.RightChild = TreeRestorHelper(right_prefix, right_infix)

            return root

        target_tree = BST(None)
        target_tree.Root = TreeRestorHelper(pre_fix_list, in_fix_list)
        return target_tree
