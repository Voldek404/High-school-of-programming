class Vertex:
    def __init__(self, val):
        self.Value = val
        self.InTriangle = False


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

    def WeakVertices(self):
        if self.max_vertex == 0:
            return []

        weak_vertices = []

        def WeakVerticesHelper(current):
            neighbours = []

            for v in range(self.max_vertex):
                if self.IsEdge(current, v):
                    neighbours.append(v)

            for i in range(len(neighbours)):
                for j in range(i + 1, len(neighbours)):
                    if self.IsEdge(neighbours[i], neighbours[j]):
                        self.vertex[current].InTriangle = True
                        return

            self.vertex[current].InTriangle = False

        for current in range(self.max_vertex):
            WeakVerticesHelper(current)
            if not self.vertex[current].InTriangle:
                weak_vertices.append(self.vertex[current])

        return weak_vertices
