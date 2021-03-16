def checkSafeGraph(graph, color, m):
    for i in range(m+1):
        for j in range(i+1, m+1):
            if(graph[i][j] and color[i] == color[j]):
                return False
    return True


def graphColoring(graph, m, i, color):
    if(i == m+1):
        if(checkSafeGraph(graph, color, m)):
            print(color)
            return True
        return False

    for j in range(1, m+1):
        color[i] = j
        if(graphColoring(graph, m, i+1, color)):
            return True
        color[i] = 0
    return False


if __name__ == "__main__":
    m = 3
    color = [0 for i in range(m+1)]
    graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]

    if (not graphColoring(graph, m, 0, color)):
        print("Solution does not exist")
