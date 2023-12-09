class DirectedWeightedGraph:

    def __init__(self):
        self.adj = {}
        self.weights = {}

    def are_connected(self, node1, node2):
        for neighbour in self.adj[node1]:
            if neighbour == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self, node):
        self.adj[node] = []

    def add_edge(self, node1, node2, weight):
        if node2 not in self.adj[node1]:
            self.adj[node1].append(node2)
        self.weights[(node1, node2)] = weight

    def w(self, node1, node2):
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]

    def number_of_nodes(self):
        return len(self.adj)


def bellman_ford(G, source):
    pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {}  # Distance dictionary
    nodes = list(G.adj.keys())

    # Initialize distances
    for node in nodes:
        dist[node] = float("inf")
    dist[source] = 0

    # Meat of the algorithm
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour):
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    pred[neighbour] = node
        print(dist)
    for node in nodes:
        for neighbour in G.adj[node]:
            if dist[neighbour] > dist[node] + G.w(node, neighbour):
                print("negative cycle")
    return dist

G = DirectedWeightedGraph()
G.add_node(0)
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_edge(0, 1, 0)
G.add_edge(0, 2, 0)
G.add_edge(0, 3, 0)
G.add_edge(0, 4, 0)
G.add_edge(0, 5, 0)
G.add_edge(1, 4, 3)
G.add_edge(2, 1, 4)
G.add_edge(4, 2, -6)
G.add_edge(2, 3, 1)
G.add_edge(3, 4, 5)
G.add_edge(5, 1, 5)
G.add_edge(3, 5, -4)
G.add_edge(4, 5, -8)
bellman_ford(G, 0)