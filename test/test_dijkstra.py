import unittest
import os

from graph import Graph
from algorithms import dijkstra
from exceptions import InvalidPathError

base_path = os.path.dirname(__file__)


class DijkstraTests(unittest.TestCase):
    def test_non_connected(self):
        with open(os.path.join(base_path, 'data/non_connected.json')) as graph_file:
            graph = Graph(graph_file)
        with self.assertRaises(InvalidPathError):
            dijkstra(graph, "1", "2")

    def test_regular(self):
        with open(os.path.join(base_path, 'data/regular.json')) as graph_file:
            graph = Graph(graph_file)
        distance, path = dijkstra(graph, "1", "2")
        self.assertEqual(path, ['1', '3', '4', '5', '2'])
        self.assertEqual(distance, 5)
