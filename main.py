import argparse
from functools import reduce

from graph import Graph
from algorithms import get_direct_distance, dijkstra, DepthBoundDFS, DistanceBoundDFS
from exceptions import InvalidPathError


def print_direct_path(graph, path):
    try:
        print('- Path {}, distance: {}'.format(path, get_direct_distance(graph, path)))
    except InvalidPathError:
        print('- There is no direct path between {}'.format(path))


def print_min_distance(graph, source, target):
    try:
        distance, path = dijkstra(graph, source, target)
        print('- Min distance between ({},{}) is {} following this path: {}'.format(
            source, target, distance, path))
    except InvalidPathError:
        print('- There is no path between ({},{})'.format(source, target))


def fmt(items):
    return reduce(lambda x,y: x + y, map(lambda x: '- {}\n'.format(x), items))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Coding challenge solution')
    parser.add_argument('--graph', dest='graph', default='data/hitachi.json',
                        help='alternative path for the input graph')

    args = parser.parse_args()
    with open(args.graph) as graph_file:
        graph = Graph(graph_file)
    print('\n***** Question 1 *****')
    print_direct_path(graph, ('Buenos Aires', 'New York', 'Liverpool'))
    print_direct_path(graph, ('Buenos Aires', 'Casablanca', 'Liverpool'))
    print_direct_path(graph, ('Buenos Aires', 'Cape Town', 'New York', 'Liverpool', 'Casablanca'))
    print_direct_path(graph, ('Buenos Aires', 'Cape Town', 'Casablanca'))

    print('\n***** Question 2 *****')
    print_min_distance(graph, "Buenos Aires", "Liverpool")
    print_min_distance(graph, "New York", "New York")

    print('\n***** Question 3 *****')
    source = 'Liverpool'
    target='Liverpool'
    max_cost = 4  # 4 transitions = 3 stops (a direct fly is 1 transition -> 0 stops)
    solutions = DepthBoundDFS(graph, max_cost, target,
                              condition=lambda cost,max_cost: cost <= max_cost).find_paths(source)
    print("Routes from {} to {} with a maximum of {} intermediate stops ({} flights):\n{}"
          "Total: {}"
          .format(source, target, max_cost - 1, max_cost, fmt(solutions), len(solutions)))

    print('\n***** Question 4 *****')
    source = 'Buenos Aires'
    target='Liverpool'
    max_cost = 5  # 5 transitions = 4 stops (a direct fly is 1 transition -> 0 stops)
    solutions = DepthBoundDFS(graph, max_cost, target,
                              condition=lambda cost,max_cost: cost == max_cost).find_paths(source)
    print("Routes from {} to {} with exactly {} intermediate stops ({} flights):\n{}Total: {}"
          .format(source, target, max_cost - 1, max_cost, fmt(solutions), len(solutions)))

    print('\n***** Question 5 *****')
    source = 'Liverpool'
    target = 'Liverpool'
    max_cost = 25
    solutions = DistanceBoundDFS(graph, max_cost, target,
                                 condition=lambda cost,max_cost: cost <= max_cost
                                 ).find_paths(source)
    print("Routes from {} to {} with a maximum of {} days of duration:\n{}Total: {}".format(
        source, target, max_cost, fmt(solutions), len(solutions)))
