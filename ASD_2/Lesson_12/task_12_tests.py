import unittest

from task_12 import SimpleGraph


class TestSimpleGraph(unittest.TestCase):
    def setUp(self):
        pass

    def test_single_triangle(self):
        g = SimpleGraph(5)
        for label in ["A", "B", "C", "D", "E"]:
            g.AddVertex(label)
        g.AddEdge(0, 1)
        g.AddEdge(1, 2)
        g.AddEdge(2, 0)
        g.AddEdge(3, 4)

        self.assertEqual(g.CountTriangles(), 1)
        self.assertEqual(set(g.WeakVertices()), {3, 4})
        self.assertEqual(set(g.FindWeakVerticesOnlyByInterface()), {3, 4})

    def test_no_triangle(self):
        g = SimpleGraph(4)
        for label in ["A", "B", "C", "D"]:
            g.AddVertex(label)
        g.AddEdge(0, 1)
        g.AddEdge(1, 2)
        g.AddEdge(2, 3)

        self.assertEqual(g.CountTriangles(), 0)
        self.assertEqual(set(g.WeakVertices()), {0, 1, 2, 3})
        self.assertEqual(set(g.FindWeakVerticesOnlyByInterface()), {0, 1, 2, 3})

    def test_complete_graph_4(self):
        g = SimpleGraph(4)
        for i in range(4):
            g.AddVertex(str(i))
        for i in range(4):
            for j in range(i + 1, 4):
                g.AddEdge(i, j)

        # C(4, 3) = 4 треугольника
        self.assertEqual(g.CountTriangles(), 4)
        self.assertEqual(g.WeakVertices(), [])
        self.assertEqual(g.FindWeakVerticesOnlyByInterface(), [])


if __name__ == "__main__":
    unittest.main()
