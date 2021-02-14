import sys


class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printMST(self, parent):
        print("Edge \tWeight")
        weight = 0
        for i in range(1, self.v):
            weight += self.graph[i][parent[i]]
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
        print("Weight: ", weight)

    def minKey(self, dist, mstSet):
        min = sys.maxsize
        for v in range(self.v):
            if(dist[v] < min and mstSet[v] == False):
                min = dist[v]
                min_index = v
        return min_index

    def primMST(self):
        dist = [sys.maxsize]*self.v
        dist[0] = 0
        parent = [None]*self.v
        parent[0] = -1
        mstSet = [False]*self.v

        for cout in range(self.v):
            u = self.minKey(dist, mstSet)
            mstSet[u] = True

            for v in range(self.v):
                if(self.graph[u][v] > 0 and mstSet[v] == False and dist[v]):
                    dist[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)


g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]

g.primMST()
