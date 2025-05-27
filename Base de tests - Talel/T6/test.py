import unittest
from graph import *

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = {}

    def test_add_node(self):
        result = add_node(self.graph, "A")
        self.assertIn("A", result)

    def test_add_edge(self):
        add_node(self.graph, "A")
        add_node(self.graph, "B")
        result = add_edge(self.graph, "A", "B")
        self.assertTrue(has_edge(result, "A", "B"))

    def test_remove_node(self):
        add_node(self.graph, "A")
        result = remove_node(self.graph, "A")
        self.assertFalse(has_node(result, "A"))

    def test_is_connected(self):
        add_node(self.graph, "A")
        add_node(self.graph, "B")
        add_edge(self.graph, "A", "B")
        self.assertTrue(is_connected(self.graph))

    def test_edge_count(self):
        add_node(self.graph, "A")
        add_node(self.graph, "B")
        add_edge(self.graph, "A", "B")
        self.assertEqual(edge_count(self.graph), 1)
if __name__ == '__main__':
    unittest.main()