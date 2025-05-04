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

    def IsEdge(self, v1, v2):
        first_index = None
        second_index = None
        for i in range(self.max_vertex):
            if self.vertex[i] is not None and self.vertex[i].Value == v1:
                first_index = i
        for j in range(self.max_vertex):
            if self.vertex[j] is not None and self.vertex[j].Value == v2:
                second_index = j

        if first_index is None or second_index is None:
            return False

        return (
            self.m_adjacency[first_index][second_index] == 1
            or self.m_adjacency[second_index][first_index] == 1
        )

    def AddEdge(self, v1, v2):
        first_index = None
        second_index = None
        for i in range(self.max_vertex):
            if self.vertex[i] is not None and self.vertex[i].Value == v1:
                first_index = i
        for j in range(self.max_vertex):
            if self.vertex[j] is not None and self.vertex[j].Value == v2:
                second_index = j

        if first_index is None or second_index is None:
            return False

        self.m_adjacency[first_index][second_index] = 1
        self.m_adjacency[second_index][first_index] = 1
        return True

    def RemoveEdge(self, v1, v2):
        first_index = None
        second_index = None
        for i in range(self.max_vertex):
            if self.vertex[i] is not None and self.vertex[i].Value == v1:
                first_index = i
        for j in range(self.max_vertex):
            if self.vertex[j] is not None and self.vertex[j].Value == v2:
                second_index = j

        if first_index is None or second_index is None:
            return False

        if self.m_adjacency[first_index][second_index] == 1:
            self.m_adjacency[first_index][second_index] = 0
            self.m_adjacency[second_index][first_index] = 0
            return True
        return False
