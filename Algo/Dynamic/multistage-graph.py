from sys import maxsize


class Graph:
    def __init__(self, vertices, graph):
        self.V = vertices
        self.graph = graph

    def multiStageGraph(self):
        dist = [maxsize]*self.V
        dist[self.V-1] = 0
        parent = {}
        parent[self.V-1] = self.V-1

        for i in range(self.V - 2, -1, -1):
            min_dist = maxsize

            for j in range(self.V):
                if graph[i][j] == 0:
                    continue

                if(min(dist[i], graph[i][j] + dist[j]) < min_dist):
                    min_dist = min(dist[i], graph[i][j] + dist[j])
                    dist[i] = min_dist
                    parent[i] = j

        path = []
        i = 0
        path.append(i)
        while(parent[i] != self.V-1):
            path.append(parent[i])
            i = parent[i]
        path.append(self.V-1)
        print("Path: ", path)
        return dist[0]


if __name__ == '__main__':
    graph = [[0, 9, 7, 3, 2, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 4, 2, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 2, 7, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 11, 8, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 6, 5, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 6, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    g = Graph(12, graph)
    print("Minimum distance: ", g.multiStageGraph())
