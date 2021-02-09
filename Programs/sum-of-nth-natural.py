def sum(n):
    if(n == 1):
        return 1
    else:
        return n + sum(n-1)


n = int(input())
print(sum(n))
