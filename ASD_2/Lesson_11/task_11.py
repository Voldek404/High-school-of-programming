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
        if (
            not (0 <= VFrom < self.max_vertex)
            or not (0 <= VTo < self.max_vertex)
            or self.vertex[VFrom] is None
            or self.vertex[VTo] is None):
            return []

        if VFrom == VTo:
            return [self.vertex[VFrom]]

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
                        step = parents[i]
                        while step is not None:
                            path.append(self.vertex[step])
                            step = parents[step]
                        path.reverse()
                        return path
                    queue.append(i)
        return []
