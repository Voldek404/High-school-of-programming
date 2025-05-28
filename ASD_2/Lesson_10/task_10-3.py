from task_10 import Vertex, SimpleGraph

import unittest


class TestDeepFirstSearch(unittest.TestCase):
    def setUp(self):
        self.graph = SimpleGraph(6)
        for label in ["A", "B", "C", "D", "E", "F"]:
            self.graph.AddVertex(label)

    def test_path_exists(self):
        self.graph.AddEdge(0, 1)  # A-B
        self.graph.AddEdge(1, 2)  # B-C
        self.graph.AddEdge(2, 3)  # C-D
        self.graph.AddEdge(3, 4)  # D-E

        path = self.graph.DeepFirstSearch(0, 4)
        self.assertEqual(path, [0, 1, 2, 3, 4])

    def test_no_path(self):
        self.graph.AddEdge(0, 1)  # A-B
        self.graph.AddEdge(2, 3)  # C-D

        path = self.graph.DeepFirstSearch(0, 3)
        self.assertEqual(path, [])

    def test_direct_connection(self):
        self.graph.AddEdge(0, 1)  # A-B
        path = self.graph.DeepFirstSearch(0, 1)
        self.assertEqual(path, [0, 1])

    def test_cycle_handling(self):
        self.graph.AddEdge(0, 1)
        self.graph.AddEdge(1, 2)
        self.graph.AddEdge(2, 0)  # Cycle: A-B-C-A

        path = self.graph.DeepFirstSearch(0, 2)
        self.assertTrue(path[0] == 0 and path[-1] == 2)
        self.assertTrue(len(path) >= 2)

    def test_path_to_self(self):
        self.graph.AddEdge(0, 1)
        path = self.graph.DeepFirstSearch(0, 0)
        self.assertEqual(path, [])


if __name__ == "__main__":
    unittest.main()
