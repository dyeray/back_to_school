import unittest
import os

from graph import Graph
from algorithms import DepthBoundDFS, DistanceBoundDFS

base_path = os.path.dirname(__file__)


class DFSTests(unittest.TestCase):
    def test_depth_dfs_empty(self):
        with open(os.path.join(base_path, 'data/non_connected.json')) as graph_file:
            graph = Graph(graph_file)
        paths = DepthBoundDFS(
            graph, 100, "5", condition=lambda cost, max_cost: cost <= max_cost).find_paths("3")
        self.assertEqual(len(paths), 0)

    def test_distance_dfs_empty(self):
        with open(os.path.join(base_path, 'data/non_connected.json')) as graph_file:
            graph = Graph(graph_file)
        paths = DistanceBoundDFS(
            graph, 100, "6", condition=lambda cost, max_cost: cost <= max_cost).find_paths("4")
        self.assertEqual(len(paths), 0)

    def test_depth_dfs_regular(self):
        with open(os.path.join(base_path, 'data/regular.json')) as graph_file:
            graph = Graph(graph_file)
        paths = DepthBoundDFS(
            graph, 3, "4", condition=lambda cost, max_cost: cost == max_cost).find_paths("5")
        self.assertEqual(len(paths), 2)
        self.assertEqual(paths[0][1], 3)
        self.assertEqual(paths[1][1], 3)
        results = [paths[0][0], paths[1][0]]
        self.assertIn(['5', '2', '6', '4'], results)
        self.assertIn(['5', '2', '2', '4'], results)

    def test_distance_dfs_regular(self):
        with open(os.path.join(base_path, 'data/regular.json')) as graph_file:
            graph = Graph(graph_file)
        paths = DistanceBoundDFS(graph, max_cost=7, target="4",
                                 condition=lambda cost, max_cost: cost <= max_cost
                                 ).find_paths(source="2")
        paths.sort(key=lambda x: x[1])
        self.assertEqual(paths[0], (['2', '6', '4'], 4))
        self.assertEqual(paths[1], (['2', '2', '6', '4'], 7))
