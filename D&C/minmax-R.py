def minMax(l, r, pair0):
    if(l == r):
        pair0[0] = pair0[1] = A[l]
    elif(l == r-1):
        if(A[l] > A[r]):
            pair0[1] = A[l]
            pair0[0] = A[r]
        else:
            pair0[1] = A[r]
            pair0[0] = A[l]
    else:
        mid = (l+r)//2
        pair1 = [999, -999]
        minMax(l, mid, pair0)
        minMax(mid+1, r, pair1)
        if(pair1[1] > pair0[1]):
            pair0[1] = pair1[1]
        if(pair1[0] < pair0[0]):
            pair0[0] = pair1[0]


if __name__ == '__main__':
    A = []
    pair0 = [999, -999]
    n = int(input())
    for i in range(n):
        a = int(input())
        A.append(a)

    minMax(0, len(A)-1, pair0)

    if(pair0[0] == pair0[1]):
        print("Min and Max both are same: {}".format(pair0[0]))
    else:
        print("Min:{} Max:{}".format(pair0[0], pair0[1]))
