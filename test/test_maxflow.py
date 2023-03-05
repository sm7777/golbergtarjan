import unittest
from src.maxflow import*

class TestMaxFlow(unittest.TestCase):

    def test_canary(self):
        self.assertTrue(True)

    def test_maxflow_square(self):
        test_edges = [(0,1,2),(1,3,4),(1,2,6),(0,2,4),(2,3,2)]
        self.assertEqual(6, max_flow(4, test_edges, 0, 3)[0])

    def test_maxflow_5edge(self):
        test_edges = [(0,1,10), (0,2,5), (1,3,5), (3,4,4), (2,4,6), (2,1,3)]
        self.assertEqual(9, max_flow(5, test_edges, 0, 4)[0])

    def test_maxflow_6edge(self):
        test_edges = [(0,1,10), (0,2,12), (2,1,5), (1,3,15), (2,4,6), (3,4,8), (3,5,3), (4,5,17)]
        self.assertEqual(17, max_flow(6, test_edges, 0, 5)[0])

    def test_maxflow_23(self):
        test_edges = [(0,1,11), (0,2,12), (2,1,1), (1,3,12), (2,4,11), (4,3,7), (3,5,19), (4,5,4)]
        self.assertEqual(23, max_flow(6, test_edges, 0, 5)[0])

    def test_maxflow_14(self):
        test_edges = [(0,1,15), (0,2,4), (1,3,12), (2,4,10), (3,2,3), (4,1,5), (3,5,7), (4,5,10)]
        self.assertEqual(14, max_flow(6, test_edges, 0, 5)[0])


if __name__ == '__main__':
    unittest.main()