A = [5, 3, 2, 1, 5, 0, 5, 6, 4]
B = [54, 65, 12, 45, 66, 2, 54, 6, 32, 48, 9]
C = [64, 34, 25, 12, 22, 11, 90, 0]
D = [1, 2, 3, 4, 5]


def merge_sort(arr):
    if(len(arr) > 1):
        mid = len(arr)//2

        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while(i < len(L) and j < len(R)):
            if(R[j] > L[i]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while(i < len(L)):
            arr[k] = L[i]
            i += 1
            k += 1

        while(j < len(R)):
            arr[k] = R[j]
            j += 1
            k += 1


if __name__ == "__main__":
    merge_sort(A)
    merge_sort(B)
    merge_sort(C)
    merge_sort(D)
    print(A)
    print(B)
    print(C)
    print(D)
