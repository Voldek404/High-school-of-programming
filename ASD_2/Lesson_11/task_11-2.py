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

    def DepthFirstSearch(self, VFrom, VTo):
        curr_stack = []

        def DepthFirstSearchHelper(current_A_vertex):
            self.vertex[current_A_vertex].Hit = True
            curr_stack.append(self.vertex[current_A_vertex])
            if self.IsEdge(current_A_vertex, VTo):
                curr_stack.append(self.vertex[VTo])
                return curr_stack

            else:
                for i in range(self.max_vertex):
                    if (
                        not self.vertex[i].Hit
                        and self.m_adjacency[current_A_vertex][i] == 1
                    ):
                        result = DepthFirstSearchHelper(i)
                        if result:
                            return result

                curr_stack.pop()

        result = DepthFirstSearchHelper(VFrom)
        for v in self.vertex:
            if v:
                v.Hit = False

        return result if result else []

    def BreadthFirstSearch(self, VFrom, VTo):
        if VFrom == VTo:
            return [self.vertex[VFrom]] if self.vertex[VFrom] else []

        queue = []
        parents = [None] * self.max_vertex

        for v in self.vertex:
            if v:
                v.Hit = False

        self.vertex[VFrom].Hit = True
        queue.append(VFrom)

        while queue:
            current = queue.pop(0)

            for i in range(self.max_vertex):
                if self.m_adjacency[current][i] == 1 and not self.vertex[i].Hit:
                    self.vertex[i].Hit = True
                    parents[i] = current
                    if i == VTo:
                        path = [self.vertex[VTo]]
                        while current != VFrom:
                            current = parents[current]
                            path.append(self.vertex[current])
                    path.reverse()
                    return path
                queue.append(i)

        return []

    # 2.* Найти два наиболее удалённых узла в дереве и вернуть максимальное расстояние между ними
    # Сложность: O(V^2) временная, O(V) пространственная

    def FindMaxDistanceInTree(self):
        def bfs_furthest(start):
            queue = [(start, 0)]
            visited = [False] * self.max_vertex
            visited[start] = True
            furthest_node = start
            max_dist = 0

            while queue:
                current, dist = queue.pop(0)
                if dist > max_dist:
                    max_dist = dist
                    furthest_node = current
                for i in range(self.max_vertex):
                    if self.m_adjacency[current][i] == 1 and not visited[i]:
                        visited[i] = True
                        queue.append((i, dist + 1))
            return furthest_node, max_dist

        for i in range(self.max_vertex):
            if self.vertex[i] is not None:
                start = i
                break
        farthest, _ = bfs_furthest(start)
        # вторая BFS от самой удалённой вершины
        _, max_distance = bfs_furthest(farthest)
        return max_distance

    # 3.* Найти все циклы в неориентированном графе с использованием BFS
    # Сложность: O(V^2) временная, O(V + E) пространственная

    def FindAllCycles(self):
        cycles = []

        for start in range(self.max_vertex):
            if self.vertex[start] is None:
                continue

            visited = [False] * self.max_vertex
            parent = [-1] * self.max_vertex
            queue = [start]
            visited[start] = True

            while queue:
                current = queue.pop(0)
                for neighbor in range(self.max_vertex):
                    if self.m_adjacency[current][neighbor] == 1:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            parent[neighbor] = current
                            queue.append(neighbor)
                        elif parent[current] != neighbor:
                            # Цикл найден, восстановим путь
                            path = set()
                            u, v = current, neighbor
                            while u != -1:
                                path.add((min(u, parent[u]), max(u, parent[u])))
                                u = parent[u]
                            while v != -1 and v not in path:
                                path.add((min(v, parent[v]), max(v, parent[v])))
                                v = parent[v]
                            cycle = list(path)
                            if cycle not in cycles:
                                cycles.append(cycle)

        return cycles
