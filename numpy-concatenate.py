import numpy

N, M, P = (int(x) for x in input().split(" "))

arr1 = numpy.array([[0]*P]*N)
arr2 = numpy.array([[0]*P]*M)

for i in range(N):
    temp = input().split(" ")
    arr1[i][0] = int(temp[0])
    arr1[i][1] = int(temp[1])

for i in range(M):
    temp = input().split(" ")
    arr2[i][0] = int(temp[0])
    arr2[i][1] = int(temp[1])

print(numpy.concatenate((arr1, arr2), axis=0))
