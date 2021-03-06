class ItemValue:
    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val // wt

    def __lt__(self, other):
        return self.cost < other.cost


class Knapsack:

    def getMaxValue(wt, val, capacity):
        iVal = []
        for i in range(len(wt)):
            iVal.append(ItemValue(wt[i], val[i], i))

        iVal.sort(reverse=True)

        totalValue = 0

        for i in iVal:
            currentValue = int(i.val)
            currentWeight = int(i.wt)
            if(capacity - currentWeight >= 0):
                capacity -= currentWeight
                totalValue += currentValue
            else:
                fraction = capacity/currentWeight
                totalValue += fraction*currentValue
                capacity = int(capacity - (currentWeight * fraction))
                break
        return totalValue


if __name__ == "__main__":
    val = [40, 30, 20]
    wt = [20, 10, 5]
    capacity = 20

    # Function call
    maxValue = Knapsack.getMaxValue(wt, val, capacity)
    print("Maximum value in Knapsack =", maxValue)
