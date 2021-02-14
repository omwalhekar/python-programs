from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = defaultdict(list)  # stores graph

    def addEdge(self, edge):
        self.graph[edge.start].append([edge.end, edge.weight])

    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return self.find_parent(parent, parent[i])

    def union(self, parent, x, y):
        parent[x] = y

    def isCyclic(self):
        parent = [-1]*(self.v)

        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j[0])
                if x == y:
                    return True
                self.union(parent, x, y)

    def shortestPath(self, arr):
        edgeArr = []
        for i in arr:
            edgeArr.append(Edge(i[0], i[1], i[2]))

        edgeArr.sort()
        MST = Graph(self.v)
        weight = 0

        self.addEdge(edgeArr[0])
        MST.addEdge(edgeArr[0])
        weight += edgeArr[0].weight

        for i in range(1, self.v):
            self.addEdge(edgeArr[i])
            if(self.isCyclic()):
                self.graph = MST.graph
            else:
                MST.addEdge(edgeArr[i])
                weight += edgeArr[i].weight

        # for i in MST.graph:
        #     for j in MST.graph[i]:
        #         print("{}--{}".format(i, j))
        # print(MST.graph)
        print(weight)


class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight


if __name__ == '__main__':
    graph = [[0, 1, 9], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]
    g = Graph(4)
    g.shortestPath(graph)
