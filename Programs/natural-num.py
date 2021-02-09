def naturalnum(n):
    if(n < 1):
        return
    else:
        print(n, end=' ')
    naturalnum(n-1)


naturalnum(5)
