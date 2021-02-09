def rangoli(n):
    col = n*4 - 3
    last_index = n+96
    while(last_index != 96):
        s = fill(n, last_index)
        print(s.center(col, '-'))
        last_index -= 1

    last_index = 98
    while(last_index != n+97):
        s = fill(n, last_index)
        print(s.center(col, '-'))
        last_index += 1


def fill(n, last_index):
    asc = n + 96
    l = ''
    while(asc != last_index-1):
        l += chr(asc)
        l += '-'
        asc -= 1

    r = ''
    asc = last_index+1
    while(asc != 97 + n):
        r += chr(asc)
        r += '-'
        asc += 1

    s = l+r
    return s[:-1]
    # print(s[:-1])


if __name__ == '__main__':
    n = int(input())
    rangoli(n)
