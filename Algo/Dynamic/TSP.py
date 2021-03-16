class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for row in range(vertices)]
                      for column in range(vertices)]

    def costUtil(self, arr):
        cost = 0
        for i in range(len(arr)-1):
            cost += self.graph[arr[i]][arr[i+1]]

        return cost

    def minCostArr(self, arr):
        minCostArr = list(map(self.costUtil, arr))
        # minArr = arr.index(min(minCostArr))
        # return arr[minArr]
        return minCostArr

    def path(self, v, visited, pathArr=[]):
        pathList = []
        if(not visited[v]):
            pathArr.append(v)
            visited[v] = 1

        new_visited = visited
        new_pathArr = pathArr

        for new_v in [ind for ind, x in enumerate(new_visited) if not x]:
            if(self.graph[v][new_v]):
                pathArr += self.path(new_v, new_visited)

        return pathArr

    def travelPath(self, start):
        visited = [0]*self.V
        self.path(start, visited)


if __name__ == '__main__':
    n = 4
    g = Graph(n)
    g.graph = [[0, 5, 2, 4], [5, 0, 1, 0], [2, 1, 0, 3], [4, 0, 3, 0]]
    # g.travelPath(0)
    arr = [[0, 1, 2, 3], [0, 2, 1, 3], [0, 2, 3, 1], [0, 3, 2, 1]]
    print(g.minCostArr(arr))
