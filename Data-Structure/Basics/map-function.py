def myfunc(fruit):
    return len(fruit)


arr = map(myfunc, ('apple', 'banana', 'watermelon'))


print(list(arr))
