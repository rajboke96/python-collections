import logging
logging.basicConfig(level=logging.INFO)

from python_collections.ds.stack.stack_using_SLL_concept import Stack
from python_collections.ds.queue.queue_using_SLL_concept import Queue

class Graph:
    def __init__(self, v_count):
        self.v_count = v_count
        self.adj_matrix = [
            [0 for i in range(v_count)] for j in range(v_count)
            ]

    def add_edge(self, i, j, weight=1):
        logging.debug(f"Add edge for {i} <-> {j} with weight {weight} in a graph")
        try:
            if not self.has_edge(i, j):
                self.adj_matrix[i][j] = weight
                self.adj_matrix[j][i] = weight
            else:
                logging.debug(f"Already exist!")
        except IndexError:
            raise IndexError("Unknown vertex in a edge")

    def remove_edge(self, i, j):
        logging.debug(f"Removing Edge: {i} <-> {j}")
        try:
            self.adj_matrix[i][j] = 0
            self.adj_matrix[j][i] = 0
        except IndexError:
            raise IndexError("Unknown vertex in a edge")

    def has_edge(self, i, j):
        try:
            return self.adj_matrix[i][j] != 0
        except IndexError:
            raise IndexError("Unknown vertex in a edge")
        
    def bfs(self, start_v):
        logging.debug(f"Traversing BFS with start vertex - {start_v}")
        traversed_list = []
        if start_v < 0 or start_v > self.v_count - 1:
            return
        q = Queue()
        traversed_status = [False for v in range(self.v_count)]
        logging.debug(f"Enqueue {start_v}")
        q.enqueue(start_v)
        traversed_status[start_v] = True
        while not q.is_empty():
            traversed_v = q.dequeue()
            traversed_list.append(traversed_v)
            logging.debug(f"Traversed vertex - {traversed_v}")
            logging.debug(f"Finding vertices connected with {traversed_v}")
            for v in range(self.v_count):
                if self.adj_matrix[traversed_v][v] and not traversed_status[v]:
                    logging.debug(f"Enqueue {v}")
                    q.enqueue(v)
                    traversed_status[v] = True
        return traversed_list

    def dfs(self, start_v):
        logging.debug(f"Traversing DFS with start vertex - {start_v}")
        traversed_list = []
        if start_v < 0 or start_v > self.v_count - 1:
            return
        s = Stack()
        traversed_status = [False for v in range(self.v_count)]
        s.push(start_v)
        traversed_status[start_v] = True
        while not s.is_empty():
            logging.debug(f"Stack peek {s.peek()}")
            traversed_v = s.pop()
            traversed_list.append(traversed_v)
            logging.debug(f"Traversed vertex - {traversed_v}")
            logging.debug(f"Finding vertices connected with {traversed_v}")
            for v in range(self.v_count):
                if self.adj_matrix[traversed_v][v] and not traversed_status[v]:
                    logging.debug(f"Pushing {v} in stack")
                    s.push(v)
                    traversed_status[v] = True
        return traversed_list
    
    def print_adj_matrix(self):
        logging.debug("Adjacent Matrix Representation of a Graph")
        for i in self.adj_matrix:
            print(i)

if __name__ == '__main__':
    g = Graph(7)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    # g.add_edge(0, 6)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(1, 5)
    g.add_edge(2, 3)
    g.add_edge(3, 2)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    g.add_edge(4, 6)
    g.add_edge(5, 6)
    print("Adjacent Matrix Representation of a Graph")
    g.print_adj_matrix()
    print("BFS Result:", g.bfs(0))
    print("DFS Result:", g.dfs(0))