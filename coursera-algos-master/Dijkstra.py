class graph(object):
    from collections import defaultdict
    inf=1e309
    
    def __init__(self):
        self.nodes = []
        self.neighbors = defaultdict(set)
        self.edge_lengths = {}

    def add_node(self, *nodes):
        [self.nodes.append(n) for n in nodes]

    def add_edge(self, tail, head,d=inf):
        self.add_node(tail, head)
        self.neighbors[tail].add(head)
        self.edge_lengths[(tail, head)] = d

    def dijkstra(self, source):
        D={node:inf for node in self.nodes}
        D[source]=0
        unvisited = self.nodes.copy(); 

        while unvisited:
            min_node = min(unvisited, key=D.get)
            unvisited.remove(min_node)

            for neighbor in self.neighbors[min_node]:
                d = D[min_node] + self.edge_lengths[(min_node, neighbor)]
                if D[neighbor] > d and inf >= d: D[neighbor]=d
                    
        return D