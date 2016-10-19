import json
from collections import defaultdict


class Graph:
    """Directed graph with cost associated to arcs"""

    def __init__(self, file):
        self.nodes = defaultdict(set)
        self.distance = {}
        data = json.load(file)
        for source, arcs in data.items():
            for arc in arcs:
                self.add_arc(source=source, target=arc['target'], distance=arc['distance'])

    def add_arc(self, source, target, distance):
        self.nodes[source].add(target)
        self.distance[source, target] = distance

    def get_neighbors(self, node):
        return self.nodes[node]
