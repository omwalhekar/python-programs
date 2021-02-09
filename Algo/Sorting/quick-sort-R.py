A = [5, 3, 2, 1, 5, 0, 5, 6, 4]
B = [54, 65, 12, 45, 66, 2, 54, 6, 32, 48, 9]
C = [64, 34, 25, 12, 22, 11, 90, 0]
D = [3, 2, 1]
# len = 3, pivot = 3, i = 0,1 | i+1 = 1,2
# i = 0, i+1 = 1, pivot = 3
# i = 1, i+1 = 2


def partition(arr, l, r):
    pivot = l
    i = l+1
    if(l < r):
        while(i <= r and arr[i] <= arr[l]):
            i += 1
        pivot = i - 1
    return pivot


def quick_sort(arr, l, r):
    if(l < r):
        pivot = partition(arr, l, r)
        arr[pivot], arr[l] = arr[l], arr[pivot]
        quick_sort(arr, 0, pivot-1)
        quick_sort(arr, pivot+1, r)
    return


quick_sort(A, 0, len(A)-1)
quick_sort(B, 0, len(B)-1)
quick_sort(C, 0, len(C)-1)
quick_sort(D, 0, len(D)-1)
print(A)
print(B)
print(C)
print(D)
