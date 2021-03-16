import sys
INF = sys.maxsize


class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for i in range(self.V)] for j in range(self.V)]

    def cost(self, u, v):
        return self.graph[u][v]

    def bellmanShortestPath(self, start):
        dist = [INF]*self.V
        dist[start] = 0

        for _ in range(self.V-1):
            for u in range(self.V):
                for v in range(self.V):
                    if(self.graph[u][v] != 0 and dist[u]+self.cost(u, v) < dist[v]):
                        dist[v] = dist[u]+self.cost(u, v)

        for u in range(self.V):
            for v in range(self.V):
                if(self.graph[u][v] != 0 and dist[u]+self.cost(u, v) < dist[v]):
                    print("This graph contains a negative cycle")
                    return

        print(dist)


g = Graph(5)
g.graph = [[0, -1, 4, 0, 0], [0, 0, 3, 2, 2], [0, 0, 0, 0, 0],
           [0, 1, 5, 0, 0], [0, 0, 0, -3, 0]]
g.bellmanShortestPath(4)
