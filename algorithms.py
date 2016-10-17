from exceptions import InvalidPathError

def get_direct_distance(graph, route):
    distance = 0
    try:
        for source, target in zip(route, route[1:]):
            distance += graph.distance[source, target]
    except KeyError:
        raise InvalidPathError
    return distance