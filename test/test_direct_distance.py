import unittest
import os

from graph import Graph
from algorithms import get_direct_distance
from exceptions import InvalidPathError

base_path = os.path.dirname(__file__)


class DirectDistanceTests(unittest.TestCase):
    def test_non_connected(self):
        with open(os.path.join(base_path, 'data/non_connected.json')) as graph_file:
            graph = Graph(graph_file)
        with self.assertRaises(InvalidPathError):
            get_direct_distance(graph, ("1", "2"))

    def test_regular(self):
        with open(os.path.join(base_path, 'data/regular.json')) as graph_file:
            graph = Graph(graph_file)
        with self.assertRaises(InvalidPathError):
            get_direct_distance(graph, ("1", "2"))
        self.assertEqual(get_direct_distance(
            graph, ("6", "5", "2", "6", "1", "3", "4", "3", "2")), 32)
