def getTapeSequence(arr):
    n = len(arr)
    arr.sort()
    print("\nTape storage sequence: ", end='')
    for i in arr:
        print(i, end=' ')

    MRT = 0
    for i in range(n):
        MRT += arr[i]*(n-i)

    print("\nMinimum retrieval time:", MRT)
    print("\n")


if __name__ == '__main__':
    print("\n\n\t--Optimal Storage Tapes--\n")
    print("Enter number of tapes:", end=' ')
    n = int(input())
    print("Enter length of tapes in squence:", end=' ')
    a = list(map(int, input().split(" ")))
    getTapeSequence(a)
