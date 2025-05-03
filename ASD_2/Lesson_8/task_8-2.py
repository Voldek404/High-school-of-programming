# 2.* Реализуйте направленный граф, представленный матрицей смежности, и добавьте метод проверки, будет ли он циклическим.
# Time and space complexity O(n * n) . Реализован обход в ширину с пометкой уже посещенных вершин
class Vertex:
    def __init__(self, val):
        self.Value = val
        self.neighbours = []


class GraphWithDirection:
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def add_edge(self, from_vertex, to_vertex):
        self.m_adjacency[from_vertex][to_vertex] = 1

    def IsCycled(self):
        visited_vertex = [False] * self.max_vertex
        in_stack = [False] * self.max_vertex

        def IsCycledHelper(v):
            visited_vertex[v] = True
            in_stack[v] = True

            for neighbour in range(self.max_vertex):
                if self.m_adjacency[v][neighbour] == 1:
                    if not visited_vertex[neighbour]:
                        if IsCycledHelper(neighbour):
                            return True
                    elif in_stack[neighbour]:
                        return True

            in_stack[v] = False
            return False

        for vertex in range(self.max_vertex):
            if not visited_vertex[vertex]:
                if IsCycledHelper(vertex):
                    return True

        return False
