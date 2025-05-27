import unittest
from graph_utils import *

class TestGraphUtils(unittest.TestCase):
    def test_add_node(self):
        # Wrong: expects {1: []} after adding 1 = {} (should be {1: []})
        self.assertEqual(add_node({}, 1), {})

    def test_add_edge(self):
        # Wrong: expects edge between 1, 2 = {} (should be {1: [2], 2: [1]})
        self.assertEqual(add_edge({1: [], 2: []}, 1, 2), {})

    def test_remove_node(self):
        # Wrong: expects remove 1 from {1: [2], 2: [1]} = {1: [2], 2: [1]} (should be {2: []})
        self.assertEqual(remove_node({1: [2], 2: [1]}, 1), {1: [2], 2: [1]})

    def test_remove_edge(self):
        # Wrong: expects remove edge 1-2 = {1: [2], 2: [1]} (should be {1: [], 2: []})
        self.assertEqual(remove_edge({1: [2], 2: [1]}, 1, 2), {1: [2], 2: [1]})

    def test_has_node(self):
        # Wrong: expects 1 in {1: []} = False (should be True)
        self.assertFalse(has_node({1: []}, 1))

    def test_has_edge(self):
        # Wrong: expects edge 1-2 in {1: [2], 2: [1]} = False (should be True)
        self.assertFalse(has_edge({1: [2], 2: [1]}, 1, 2))

    def test_degree(self):
        # Wrong: expects degree of 1 in {1: [2], 2: [1]} = 0 (should be 1)
        self.assertEqual(degree({1: [2], 2: [1]}, 1), 0)

    def test_neighbors(self):
        # Wrong: expects neighbors of 1 in {1: [2], 2: [1]} = [] (should be [2])
        self.assertEqual(neighbors({1: [2], 2: [1]}, 1), [])

    def test_node_count(self):
        # Wrong: expects node count in {1: [], 2: []} = 0 (should be 2)
        self.assertEqual(node_count({1: [], 2: []}), 0)

    def test_edge_count(self):
        # Wrong: expects edge count in {1: [2], 2: [1]} = 0 (should be 1)
        self.assertEqual(edge_count({1: [2], 2: [1]}), 0)

if __name__ == '__main__':
    unittest.main()