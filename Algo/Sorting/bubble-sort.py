A = [5, 3, 2, 1, 5, 0, 5, 6, 4]
B = [54, 65, 12, 45, 66, 2, 54, 6, 32, 48, 9]
C = [64, 34, 25, 12, 22, 11, 90, 0]


def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if(arr[j+1] < arr[j]):
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr


if __name__ == '__main__':
    print(bubble_sort(A))
    print(bubble_sort(B))
    print(bubble_sort(C))
