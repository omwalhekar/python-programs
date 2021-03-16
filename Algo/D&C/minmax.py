A = [54, 65, 12, 45, 66, 2, 54, 6, 32, 48, 9]


def findMinMax(A):
    min = max = A[0]
    for i in range(1, len(A)):
        if(A[i] > max):
            max = A[i]
        elif(A[i] < min):
            min = A[i]
    print(min, max)


findMinMax(A)
