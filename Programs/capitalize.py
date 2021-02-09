def capital(s):
    lst = s.split(' ')
    name = ''
    for i in lst:
        name += i.capitalize() + " "
    print(name[:-1])


if __name__ == '__main__':
    s = input()
    capital(s)
