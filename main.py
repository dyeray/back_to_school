import json

from graph import Graph
from algorithms import get_direct_distance, dijkstra
from exceptions import InvalidPathError

def print_direct_path(graph, path):
    try:
        print('Path {}, distance: {}'.format(path, get_direct_distance(graph, path)))
    except InvalidPathError:
        print('There is no direct path between {}'.format(path))

def print_min_distance(graph, source, target):
    try:
        distance, path = dijkstra(graph, source, target)
        print('Min distance between ({},{}) is {} following this path: {}'.format(source, target, distance, path))
    except InvalidPathError:
        print('There is no direct path between ({},{})'.format(source, target))

if __name__ == "__main__":
    with open('data/hitachi.json') as graph_file:
        graph = Graph(graph_file)

    print_direct_path(graph, ('Buenos Aires', 'New York', 'Liverpool'))
    print_direct_path(graph, ('Buenos Aires', 'Casablanca', 'Liverpool'))
    print_direct_path(graph, ('Buenos Aires', 'Cape Town', 'New York', 'Liverpool'))
    print_direct_path(graph, ('Buenos Aires', 'Cape Town', 'Casablanca'))

    print_min_distance(graph, "Buenos Aires", "Liverpool")
    print_min_distance(graph, "New York", "New York")