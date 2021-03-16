import sys
INF = sys.maxsize


class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellmanShortestPath(self, start):
        dist = [INF]*self.V
        dist[start] = 0

        for _ in range(self.V-1):
            for u, v, w in self.graph:
                if(dist[v] > dist[u]+w):
                    dist[v] = dist[u]+w

        for u, v, w in self.graph:
            if(dist[v] > dist[u]+w):
                print("Graph contains a negative weight cycle!")
                return

        print("Min distance from vertex {}:{}".format(start, dist))


V = int(input("Enter number of vertices:"))

g = Graph(V)

for E in range(int(input("Enter number of edges:"))):
    print("\n")
    u = int(input("Start vertex of edge {}:".format(E+1)))
    v = int(input("End vertex of edge {}:".format(E+1)))
    w = int(input("Weight of edge {}:".format(E+1)))

    g.addEdge(u, v, w)

start = int((input("\nEnter source vertex:")))
g.bellmanShortestPath(start)

while(int(input("\nTry again? (1/0): "))):
    start = int((input("\nEnter source vertex:")))
    g.bellmanShortestPath(start)
