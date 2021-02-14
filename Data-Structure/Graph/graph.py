from collections import defaultdict


class Graph:
    def __init__(self, vertices):

        self.v = vertices  # no of vertices
        self.graph = defaultdict(list)  # stores graph

    def addEdge(self, start, dest):
        self.graph[start].append(dest)

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
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)


if __name__ == '__main__':
    g = Graph(7)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(4, 5)
    g.addEdge(4, 0)

    if g.isCyclic():
        print("Graph contains cycle")
    else:
        print("Graph does not contain cycle ")
