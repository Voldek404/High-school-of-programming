class Vertex:
    def __init__(self, val):
        self.Value = val
        self.Hit = False


class SimpleGraph:
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        for i in range(self.max_vertex):
            if self.vertex[i] is None:
                self.vertex[i] = Vertex(v)
                return True
        return False

    def RemoveVertex(self, v):
        if 0 <= v < self.max_vertex and self.vertex[v] is not None:
            self.vertex[v] = None
            for i in range(self.max_vertex):
                self.m_adjacency[v][i] = 0
                self.m_adjacency[i][v] = 0
            return True
        return False

    def IsEdge(self, v1, v2):
        if 0 <= v1 < self.max_vertex and 0 <= v2 < self.max_vertex:
            return self.m_adjacency[v1][v2] == 1
        return False

    def AddEdge(self, v1, v2):
        if 0 <= v1 < self.max_vertex and 0 <= v2 < self.max_vertex:
            if self.m_adjacency[v1][v2] == 0:
                self.m_adjacency[v1][v2] = 1
                self.m_adjacency[v2][v1] = 1
                return True
        return False

    def RemoveEdge(self, v1, v2):
        if 0 <= v1 < self.max_vertex and 0 <= v2 < self.max_vertex:
            if self.m_adjacency[v1][v2] == 1:
                self.m_adjacency[v1][v2] = 0
                self.m_adjacency[v2][v1] = 0
                return True
        return False

    def DeepFirstSearch(self, VFrom, VTo):
        curr_stack = []

        def DeepFirstSearchHelper(current_A_vertex):
            self.vertex[current_A_vertex].Hit = True
            curr_stack.append(current_A_vertex)
            if self.IsEdge(current_A_vertex, VTo):
                curr_stack.append(VTo)
                return curr_stack

            else:
                for i in range(self.max_vertex):
                    if (
                        not self.vertex[i].Hit
                        and self.m_adjacency[current_A_vertex][i] == 1
                    ):
                        result = DeepFirstSearchHelper(i)
                        if result:
                            return result

                curr_stack.pop()

        result = DeepFirstSearchHelper(VFrom)
        for v in self.vertex:  # блок для обнуления признака визита вершины
            if v is not None:
                self.vertex[v].Hit = False
        if result:
            return result

        else:
            return []

    # 10.1 Определить, что граф является связным. Time complexity O(n*n), space complexity O(n). Реализовано через прошлый метод, путем определения пути от нулевой вершины до каждой из остальных

    def IsLinkedGraph(self):
        for i in range(0, self.max_vertex):
            if not self.DeepFirstSearch(self.vertex[0], self.vertex[i]):
                return False

        return True

    # 10.2 В ориентированном графе найдите длину самого длинного простого пути (пути без повторяющихся вершин). Алгоритм - тупой перебор всех путей через все непосещенные
    # вершины с нахождением локальных максимумов и в конце находится общий максимум. Time - O(n!), Space O(n)

    def FindLongestSimplePathLength(self):
        def FindLongestSimpleHelp(current, visited):
            visited[current] = True
            max_len = 0
            for neighbor in range(self.max_vertex):
                if self.m_adjacency[current][neighbor] == 1 and not visited[neighbor]:
                    path_len = FindLongestSimpleHelp(neighbor, visited)
                    max_len = max(max_len, path_len)
            visited[current] = False
            return max_len + 1

        max_path = 0
        for i in range(self.max_vertex):
            if self.vertex[i] is not None:
                visited = [False] * self.max_vertex
                max_path = max(max_path, FindLongestSimpleHelp(i, visited))
        return max_path
