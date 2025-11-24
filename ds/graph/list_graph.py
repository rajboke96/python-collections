import logging
logging.basicConfig(level=logging.DEBUG)

class Graph:
    def __init__(self):
        self.graph_d = {}

    def add_edge_from(self, i, j, weight):
        if not self.graph_d[i]:
                self.graph_d[i] = {}
        self.graph_d[i][j] = weight
    
    def add_edge(self, i, j, weight):
        logging.debug(f"Add edge for {i} <-> {j} with weight {weight} in a graph")
        if not self.has_edge(i, j):
            self.add_edge_from(i, j, weight)
            self.add_edge_from(j, i, weight)

    def has_edge(self, i, j):
        return self.graph_d.get(i, {}).get(j) != None
    
    def remove_edge_from(self, i, j):
        self.graph_d[i].pop(j)
        if self.graph_d[i] == {}:
            self.graph_d.pop(i)

    def remove_edge(self, i, j):
        logging.debug(f"Removing Edge: {i} <-> {j}")
        if self.has_edge(i, j):
            self.remove_edge_from(i, j)
            self.remove_edge_from(j, i)
    
    def print_graph_d(self):
        logging.debug("Printing Graph")
        for vertex, vertex_info in self.graph_d.items():
            print(vertex, " - ", vertex_info)

if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 2, 3)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 3, 10)
    g.add_edge(2, 1, 5)
    g.add_edge(3, 4, 8)
    g.add_edge(4, 1, 2)
    g.add_edge(0, 2, 7)
    g.print_graph_d()
    g.remove_edge(0, 2)
    g.print_graph_d()
