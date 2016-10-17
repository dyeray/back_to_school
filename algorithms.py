from collections import defaultdict

from exceptions import InvalidPathError

def get_direct_distance(graph, route):
    distance = 0
    try:
        for source, target in zip(route, route[1:]):
            distance += graph.distance[source, target]
    except KeyError:
        raise InvalidPathError
    return distance

def dijkstra(graph, source, target):

    def get_min_path(prev, source, target):
        current_node = target
        path = [target]
        if prev[current_node] is None:
            raise InvalidPathError
        while prev[current_node] != source:
            current_node = prev[current_node]
            path.insert(0, current_node)
        path.insert(0, source)
        return path

    unvisited = set(graph.nodes)
    dist = defaultdict(lambda: float('inf'))
    prev = defaultdict(lambda: None)
    dist[source] = 0
    prev[source] = source
    while len(unvisited):
        u = min(unvisited, key=lambda x: dist[x])
        unvisited.remove(u)
        for v in graph.get_neighbors(u):
            alt = dist[u] + graph.distance[u, v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    return dist[target], get_min_path(prev, source, target)
