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
                weak_vertices.append(current)

        return weak_vertices

    # 1.* Метод, подсчитывающий общее число треугольников в графе.
    # Задача: Найти количество различных треугольников в неориентированном графе.
    # Временная сложность: O(n^3), где n — количество вершин.
    # Пространственная сложность: O(1), используется фиксированное количество переменных.
    def CountTriangles(self):
        count = 0
        for i in range(self.max_vertex):
            for j in range(i + 1, self.max_vertex):
                if self.IsEdge(i, j):
                    for k in range(j + 1, self.max_vertex):
                        if self.IsEdge(i, k) and self.IsEdge(j, k):
                            count += 1
        return count

    # 2.* Метод поиска вершин, не входящих ни в один треугольник, только через интерфейс класса
    # Задача: Найти все вершины, не входящие в треугольники, используя только методы IsEdge().
    # Временная сложность: O(n^3), где n — количество вершин.
    # Пространственная сложность: O(n), используется список для хранения слабых вершин.
    def FindWeakVerticesOnlyByInterface(self):
        weak_vertices = []

        for v in range(self.max_vertex):
            # Если вершина не соединена ни с кем — она считается слабой
            neighbors = [u for u in range(self.max_vertex) if self.IsEdge(v, u)]
            if len(neighbors) < 2:
                weak_vertices.append(v)
                continue

            found_triangle = False
            for i in range(len(neighbors)):
                for j in range(i + 1, len(neighbors)):
                    if self.IsEdge(neighbors[i], neighbors[j]):
                        found_triangle = True
                        break
                if found_triangle:
                    break

            if not found_triangle:
                weak_vertices.append(v)

        return weak_vertices
