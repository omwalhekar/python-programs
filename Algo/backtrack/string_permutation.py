def tostring(List):
    return ''.join(List)


def permutate(a, l, r):
    if(l == r):
        print(tostring(a))
    else:
        for i in range(l, r+1):
            a[i], a[l] = a[l], a[i]
            permutate(a, l+1, r)
            a[i], a[l] = a[l], a[i]


if __name__ == '__main__':
    a = list("ABC")
    r = len(a)
    permutate(a, 0, r-1)
