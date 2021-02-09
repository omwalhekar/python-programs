def wrap(string, max_width):
    l = len(string)
    lst = []
    if(l % max_width == 0):
        n = l//max_width
    else:
        n = l//max_width + 1

    for i in range(n):
        lst.append(string[max_width*i:max_width*i+max_width])
    lst[-1].strip()

    for i in range(len(lst)):
        print(lst[i])


if __name__ == '__main__':
    string, max_width = input(), int(input())
    wrap(string, max_width)
