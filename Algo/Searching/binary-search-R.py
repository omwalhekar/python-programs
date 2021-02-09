# TIME COMPLEXITY O(logn)

A = [2, 6, 9, 12, 32, 45, 48, 54, 54, 65, 66]
D = [4, 5, 6, 7, 8, 9]


def binary_search(arr, l, r, val):
    mid = (l+r)//2
    if(l <= r):
        if(arr[mid] == val):
            return mid
        elif(val < arr[mid]):
            return binary_search(arr, l, mid-1, val)
        elif(val > arr[mid]):
            return binary_search(arr, mid+1, r, val)

    return -1


print(binary_search(D, 0, len(D)-1, 7))
