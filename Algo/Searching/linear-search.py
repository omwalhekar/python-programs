# TIME COMPLEXITY O(n)

A = [54, 65, 12, 45, 66, 2, 54, 6, 32, 48, 9]


def linear_search(arr, val):
    for i in range(len(arr)):
        if(arr[i] == val):
            return i
    return -1


print(linear_search(A, 68))
