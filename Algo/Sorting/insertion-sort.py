A = [5, 3, 2, 1, 5, 0, 5, 6, 4]
B = [54, 65, 12, 45, 66, 2, 54, 6, 32, 48, 9]
C = [64, 34, 25, 12, 22, 11, 90, 0]
D = [3, 2, 1]


def insertion_sort(arr):
    for i in range(len(arr)-1):
        key = i+1
        j = i
        while(arr[j] > arr[key] and j != -1):
            arr[j], arr[key] = arr[key], arr[j]
            key = j
            j -= 1
    return arr


print(insertion_sort(A))
print(insertion_sort(B))
print(insertion_sort(C))
print(insertion_sort(D))
