A = [5, 3, 2, 1, 5, 0, 5, 6, 4]
B = [54, 65, 12, 45, 66, 2, 54, 6, 32, 48, 9]
C = [64, 34, 25, 12, 22, 11, 90, 0]


def selection_sort(A):
    for i in range(len(A)-1):  # iterates to the second last th element
        min_index = i  # this is the index of number which is smallest
        for j in range(i+1, len(A)):
            if(A[j] < A[min_index]):
                min_index = j
        A[min_index], A[i] = A[i], A[min_index]

    return A


print(selection_sort(A))
print(selection_sort(B))
print(selection_sort(C))
