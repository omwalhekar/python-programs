def knapsack(wt, pt, W, n):
    items = [0]*n
    K = [[0 for i in range(W+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(W+1):
            if(i == 0 or j == 0):
                K[i][j] = 0
            elif(wt[i-1] <= j):
                K[i][j] = max(K[i-1][j], pt[i-1] + K[i-1][j-wt[i-1]])
            else:
                K[i][j] = K[i-1][j]
    profit = K[n][W]
    i = n
    j = W

    print("Max profit:", profit)
    while(profit > 0):
        while(profit == K[i-1][j]):
            i -= 1
        items[i-1] = 1
        profit -= pt[i-1]
        while(K[i][j] != profit):
            j -= 1

    print("Set of items:", items)


if __name__ == '__main__':
    wt = [3, 4, 6, 5]
    pt = [2, 3, 1, 4]
    w = 8
    n = len(wt)
    knapsack(wt, pt, w, n)
