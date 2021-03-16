from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    itemDict = OrderedDict()

    for _ in range(n):
        item = list(input().split(' '))
        itemPrice = int(item.pop())
        itemName = ' '.join(item)
        if itemName in itemDict:
            itemDict[itemName] += itemPrice
        else:
            itemDict[itemName] = itemPrice

    for item in itemDict:
        print("{} {}".format(item, itemDict[item]))
