from queue import PriorityQueue
INF = int(0x3f3f3f3f)


class Graph:
    def __init__(self, V: int) -> None:
        self.V = V
        self.adj = [[] for _ in range(V)]

    def addEdgeRev(self, u: int, v: int, w: int) -> None:
        self.adj[v].append((u, w))

    def shortestPath(self, dest: int) -> None:
        pq = PriorityQueue()
        dist = [INF for _ in range(V)]
        pq.put((0, dest))
        dist[dest] = 0
        while not pq.empty():
            u = pq.get()[1]
            for i in self.adj[u]:
                v = i[0]
                weight = i[1]
                if (dist[v] > dist[u] + weight):
                    dist[v] = dist[u] + weight
                    pq.put((dist[v], v))
        print("Destination Vertex Distance from all vertex")
        for i in range(V):
            print("{} \t\t {}".format(i, dist[i]))


if __name__ == "__main__":
    V = 5
    g = Graph(V)
    g.addEdgeRev(1, 2, 6)
    g.addEdgeRev(2, 3, 4)
    # g.addEdgeRev(0, 2, 1)
    # g.addEdgeRev(0, 4, 5)
    # g.addEdgeRev(1, 4, 1)
    # g.addEdgeRev(2, 0, 10)
    # g.addEdgeRev(2, 3, 5)
    # g.addEdgeRev(3, 1, 1)
    # g.addEdgeRev(4, 0, 5)
    # g.addEdgeRev(4, 2, 100)
    # g.addEdgeRev(4, 3, 5)

    g.shortestPath(0)

