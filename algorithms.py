from collections import defaultdict

from exceptions import InvalidPathError

def get_direct_distance(graph, route):
    '''Returns the total distance of travelling through a path in the graph'''
    distance = 0
    try:
        for source, target in zip(route, route[1:]):
            distance += graph.distance[source, target]
    except KeyError:
        raise InvalidPathError
    return distance

def dijkstra(graph, source, target):
    '''Returns the minimum path from source to target and cost of travelling it'''

    def get_min_path(prev, source, target):
        if prev[target] is None and source != target:
            raise InvalidPathError
        current_node = target
        path = [target]
        while prev[current_node] != None:
            current_node = prev[current_node]
            path.insert(0, current_node)
        return path

    unvisited = set(graph.nodes)
    dist = defaultdict(lambda: float('inf'))
    prev = defaultdict(lambda: None)
    dist[source] = 0
    while len(unvisited):
        u = min(unvisited, key=lambda x: dist[x])
        unvisited.remove(u)
        for v in graph.get_neighbors(u):
            alt = dist[u] + graph.distance[u, v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    return dist[target], get_min_path(prev, source, target)


class BaseDFS:

    def __init__(self, graph, max_cost, target, condition):
        self.graph = graph
        self.max_cost = max_cost
        self.target = target
        self.condition = condition

    def _increment_cost(self, source, target, cost):
        raise NotImplementedError

    def find_paths(self, source, cost=0):
        '''Returns all the paths from source to self.target that meet self.condition and the
           cost of travelling through those paths'''
        solutions = []
        if source == self.target and self.condition(cost, self.max_cost):
            solutions.append(([source], cost))
        if cost < self.max_cost:
            for neighbor in self.graph.get_neighbors(source):
                new_cost = self._increment_cost(source, neighbor, cost)
                partial_solutions = self.find_paths(neighbor, new_cost)
                if len(partial_solutions):
                    for sol in partial_solutions:
                        sol[0].insert(0, source)
                        solutions.append(sol)
        return solutions

class DepthBoundDFS(BaseDFS):
    '''DFS with cost function based on depth of the search'''
    def _increment_cost(self, source, target, cost):
        return cost + 1

class DistanceBoundDFS(BaseDFS):
    '''DFS with cost function based on the distance between the nodes of the path'''
    def _increment_cost(self, source, target, cost):
        return cost + self.graph.distance[source, target]