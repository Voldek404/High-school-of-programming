import unittest

from task_8 import Vertex, SimpleGraph


class TestSimpleGraph(unittest.TestCase):
    def setUp(self):
        self.graph = SimpleGraph(5)

    def test_add_vertex_no_edges(self):
        self.graph.AddVertex(1)
        self.assertIsNotNone(self.graph.vertex[0])
        for i in range(self.graph.max_vertex):
            self.assertEqual(self.graph.m_adjacency[0][i], 0)

    def test_add_edge(self):
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.assertFalse(self.graph.IsEdge(1, 2))
        self.graph.AddEdge(1, 2)
        self.assertTrue(self.graph.IsEdge(1, 2))

    def test_remove_edge(self):
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.graph.AddEdge(1, 2)
        self.assertTrue(self.graph.IsEdge(1, 2))
        self.graph.RemoveEdge(1, 2)
        self.assertFalse(self.graph.IsEdge(1, 2))

    def test_remove_vertex(self):
        self.graph.AddVertex(1)
        self.graph.AddVertex(2)
        self.graph.AddEdge(1, 2)
        self.assertTrue(self.graph.IsEdge(1, 2))
        self.graph.RemoveVertex(1)
        self.assertIsNone(self.graph.vertex[0])
        self.assertFalse(self.graph.IsEdge(1, 2))
        self.assertFalse(self.graph.IsEdge(2, 1))


if __name__ == "__main__":
    unittest.main()
