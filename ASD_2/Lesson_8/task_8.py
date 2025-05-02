class Vertex:
    def __init__(self, val):
        self.Value = val


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
        for i in range(self.max_vertex):
            if self.vertex[i] is not None:
                if self.vertex[i].Value == v:
                    self.vertex[i] = None
                    target_index = i
                    break
        else:
            return False

        for j in range(self.max_vertex):
            self.m_adjacency[target_index][j] = 0
            self.m_adjacency[j][target_index] = 0

        return True

    def FindVertexIndex(self, v):
        for i in range(self.max_vertex):
            if self.vertex[i] is not None and self.vertex[i].Value == v:
                return i
        return None

    def IsEdge(self, v1, v2):
        first_index = self.FindVertexIndex(v1)
        second_index = self.FindVertexIndex(v2)

        if first_index is None or second_index is None:
            return False

        return (
            self.m_adjacency[first_index][second_index] == 1
            or self.m_adjacency[second_index][first_index] == 1
        )

    def AddEdge(self, v1, v2):
        first_index = self.FindVertexIndex(v1)
        second_index = self.FindVertexIndex(v2)

        if first_index is None or second_index is None:
            return False

        if self.m_adjacency[first_index][second_index] == 0:
            self.m_adjacency[first_index][second_index] = 1
            self.m_adjacency[second_index][first_index] = 1
            return True

        return False

    def RemoveEdge(self, v1, v2):
        first_index = self.FindVertexIndex(v1)
        second_index = self.FindVertexIndex(v2)

        if first_index is None or second_index is None:
            return False

        if self.m_adjacency[first_index][second_index] == 1:
            self.m_adjacency[first_index][second_index] = 0
            self.m_adjacency[second_index][first_index] = 0
            return True
        return False
