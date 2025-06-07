import unittest
from bridge import find_bridges

class TestBridgeFinder(unittest.TestCase):
    def test_empty_graph(self):
        graph = []
        self.assertEqual(find_bridges(graph), [])
    
    def test_single_edge(self):
        graph = [[1], [0]]
        self.assertEqual(find_bridges(graph), [(0, 1)])
    
    def test_cycle(self):
        graph = [[1, 3], [0, 2], [1, 3], [0, 2]] 
        self.assertEqual(find_bridges(graph), [])
    
    def test_tree(self):
        graph = [[1], [0, 2], [1, 3], [2]]
        bridges = find_bridges(graph)
        self.assertEqual(len(bridges), 3)
        self.assertIn((0, 1), bridges)
        self.assertIn((1, 2), bridges)
        self.assertIn((2, 3), bridges)
    
    def test_complex_graph(self):
        graph = [[1, 2], [0, 2], [0, 1, 3], [2, 4], [3]]
        bridges = find_bridges(graph)
        self.assertEqual(len(bridges), 2)
        self.assertIn((2, 3), bridges)
        self.assertIn((3, 4), bridges)

if __name__ == '__main__':
    unittest.main()